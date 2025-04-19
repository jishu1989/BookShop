import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "http://books.toscrape.com/catalogue/"
MAIN_URL = "http://books.toscrape.com/"

all_books = []

def get_book_details(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    description_tag = soup.find('div', id='product_description')
    description = description_tag.find_next_sibling('p').text if description_tag else 'N/A'

    table = soup.find('table', class_='table table-striped')
    rows = table.find_all('tr')
    product_info = {row.th.text: row.td.text for row in rows}

    category = soup.select_one('ul.breadcrumb li:nth-of-type(3) a').text

    return {
        'UPC': product_info.get('UPC', ''),
        'Product Type': product_info.get('Product Type', ''),
        'Price (excl. tax)': product_info.get('Price (excl. tax)', ''),
        'Price (incl. tax)': product_info.get('Price (incl. tax)', ''),
        'Tax': product_info.get('Tax', ''),
        'Number of reviews': product_info.get('Number of reviews', ''),
        'Category': category,
        'Description': description
    }

# Loop through first 10 pages
for page in range(1, 5):
    print(f"📄 Scraping page {page}...")
    url = f"{BASE_URL}page-{page}.html"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        relative_url = book.h3.a['href'].replace('../../../', '')
        product_url = BASE_URL + relative_url

        details = get_book_details(product_url)

        all_books.append({
            'Title': title,
            'Price': price,
            'Availability': availability,
            'URL': product_url,
            **details
        })

        time.sleep(0.2)  # gentle delay

# Save to CSV
df = pd.DataFrame(all_books)
df.to_csv('C:/Users/Soumya Das/Documents/projects/git projects/Finnish-Retails/data/booklistings_5.csv', index=False)
print("✅ Done! Saved to 'books_first_10_pages.csv'")
