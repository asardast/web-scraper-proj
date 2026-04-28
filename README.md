# Web Book Scraper to PostgreSQL

A robust Python-based web scraping tool designed to extract book information from online stores and store the data in a structured PostgreSQL database.

Features:
- Data Extraction: Scrapes book titles, prices, and availability using `BeautifulSoup`.
- Database Integration: Automatically creates tables and inserts data into `PostgreSQL`.
- Security: Uses environment variables (`.env`) to protect sensitive database credentials.
- Data Export: Also generates a `books.csv` file for quick data viewing.

Tech Stack:
- Language: Python 3.x
- Libraries: Requests, BeautifulSoup4, Psycopg2, Python-dotenv
- Database: PostgreSQL

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone [https://github.com/asardast/web-scraper-proj.git](https://github.com/asardast/web-scraper-proj.git)
   cd web-scraper-proj
