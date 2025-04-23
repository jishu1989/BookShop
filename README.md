#### BookShop

Like many other book lovers, I am also a book lover. Passionate about reading different genres. 
Since my childhood I have been an avid reader of story books. Till to date I keep visiting various libraries,
bookshops in search of my favorite genres. For example, science fiction( 20,000 leagues under the Sea, Conan Doyle's
Lost World, Journey to the center of the earth), thrillers(Sherlock Holmes, Tintin and so on) and
adventures(f.e Jack London's Call of the wild, Count of Monte Cristo) are my favorite.
Gradually growing up I became extremely hooked with historical thrillers like Dan Brown's Da Vinci Code, Inferno 
and so on. Even after moving to Finland I continue to go to Oodi Library quite frequently. Therefore I am always curious
about finding a new book which I find really interesting. The interest in this project comes from the same passion.
Here I try to scrape an online bookstore. Collect the booklistings, descriptions, categories, availability, prices, with
and without tax from the online webstore. Trying to make some fun analysis on book availability and genres which are mostly found
in the bookstore. Some sentiment analysis based on the description available on the books. 

#### Scraping

Scraped the bookstore: https://books.toscrape.com/ . It has wide range of genres. f.e : historical, classics, fiction,.. 
Also detailed scraping included parameters like: UPC,Product Type,Price (excl. tax),Price (incl. tax),Tax, Availability
and Number of reviews.

Some of the libraries(like beautifulsoup,requests,pandas and time) used were downloaded in python virtual environment.

Couple of scraper scripts are created: one scrapes based on number of page input to be scraped. The other scrapes all the pages.
Using append function we append all the information and create a dataset using pandas dataframe.


#### Dashboard
**Category Overview**

Here we get an insight of what kind of books we have, and the number of books in each genre and a corresponding visualization
which helps to understand which genre of books are mostly available in the bookstore, and a corresponding visualization for 
understanding price distribution of the genres.

<img width="569" alt="image" src="https://github.com/user-attachments/assets/fd2258ab-6db6-47bf-965d-d7dce2b5fe2a" />



