import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import psycopg2  # ابزار اتصال به دیتابیس


load_dotenv()


def save_to_db(books_list):
    try:
        # ۱. اتصال به دیتابیس (اطلاعات خودت را جایگزین کن)
        db_pass = os.getenv("DB_PASSWORD")
        
        conn = psycopg2.connect(
            dbname="scraper_db",
            user="postgres",
            password=db_pass, # پسورد دیتابیس خودت را اینجا بزن
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # ۲. ساخت جدول (اگر از قبل وجود نداشته باشد)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS scraped_books (
                id SERIAL PRIMARY KEY,
                title TEXT,
                price TEXT,
                availability TEXT
            )
        """)

        # ۳. وارد کردن داده‌ها
        for book in books_list:
            cur.execute(
                "INSERT INTO scraped_books (title, price, availability) VALUES (%s, %s, %s)",
                (book['title'], book['price'], book['stock'])
            )
        
        conn.commit() # تایید نهایی برای ذخیره
        print("✅ All data was successfully saved to the database.!")

        cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ Error connecting to database: {e}")

def scrape_books():
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    
    extracted_data = []

    for book in books:
        data = {
            'title': book.h3.a['title'],
            'price': book.find('p', class_='price_color').text,
            'stock': book.find('p', class_='instock availability').text.strip()
        }
        extracted_data.append(data)
        print(f"Extracted: {data['title']}")
    
    # حالا داده‌ها را به جای فایل، به دیتابیس می‌فرستیم
    save_to_db(extracted_data)

if __name__ == "__main__":
    scrape_books()