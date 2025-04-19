import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = "http://books.toscrape.com/catalogue/"
start_url = "http://books.toscrape.com/catalogue/page-1.html"

all_books = []

def get_book_links(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    
    links = []
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        relative_url = book.h3.a['href']
        book_url = base_url + relative_url.replace('../../../', '')
        links.append({
            'title': title,
            'price': price,
            'availability': availability,
            'url': book_url
        })
    return links

def get_book_details(book):
    response = requests.get(book['url'])
    soup = BeautifulSoup(response.text, 'html.parser')

    # Description
    desc_tag = soup.find('div', id='product_description')
    description = desc_tag.find_next_sibling('p').text if desc_tag else 'N/A'

    # Table info
    table = soup.find('table', class_='table table-striped')
    info = {row.th.text: row.td.text for row in table.find_all('tr')}

    # Category
    category = soup.select_one('ul.breadcrumb li:nth-of-type(3) a').text

    book.update({
        'UPC': info.get('UPC', ''),
        'Product Type': info.get('Product Type', ''),
        'Price (excl. tax)': info.get('Price (excl. tax)', ''),
        'Price (incl. tax)': info.get('Price (incl. tax)', ''),
        'Tax': info.get('Tax', ''),
        'Number of reviews': info.get('Number of reviews', ''),
        'Category': category,
        'Description': description
    })

    return book

# Loop through all pages
page_num = 1
while True:
    page_url = f"http://books.toscrape.com/catalogue/page-{page_num}.html"
    print(f"Scraping page {page_num}: {page_url}")
    
    response = requests.get(page_url)
    if response.status_code != 200:
        break  # Stop if the page doesn't exist

    book_links = get_book_links(page_url)

    for book in book_links:
        try:
            detailed_book = get_book_details(book)
            all_books.append(detailed_book)
            time.sleep(0.5)  # Be polite
        except Exception as e:
            print(f"Failed to scrape book: {book['title']}, error: {e}")
    
    page_num += 1

# Save to CSV
df = pd.DataFrame(all_books)
df.to_csv('all_books_details.csv', index=False)
print("✅ Done! Saved all book data to all_books_details.csv")
