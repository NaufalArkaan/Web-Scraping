import requests
from bs4 import BeautifulSoup
import csv
import time

# URL target (pastikan ini URL halaman yang benar dan berisi data)
BASE_URL = "Masukin Link Web Disini"

# Header HTTP untuk meniru browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/90.0.4430.93 Safari/537.36"
}

def fetch_page(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        print(f"Fetched {url} successfully.")
        return BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_data(soup):
    data_list = []
    # Cari semua elemen h1 di halaman
    headers = soup.find_all('h1')
    
    if not headers:
        print("No <h1> elements found on the page.")
        return data_list
    
    for header in headers:
        title_text = header.get_text(strip=True)
        
        # Jika ada elemen deskripsi yang ingin diambil, misal <p> setelah <h1>
        description = header.find_next_sibling('p')
        description_text = description.get_text(strip=True) if description else 'N/A'
        
        data_list.append({
            'Title': title_text,
            'Description': description_text
        })
    return data_list

def scrape():
    print("Starting scraping process...")
    soup = fetch_page(BASE_URL)
    if not soup:
        print("Failed to fetch the main page. Exiting.")
        return []

    data = parse_data(soup)
    if not data:
        print("No data extracted from the page.")
    else:
        print(f"Extracted {len(data)} items from the page.")
    return data

def save_to_csv(data, filename='scraped_data.csv'):
    if not data:
        print("No data to save.")
        return
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    scraped_data = scrape()
    save_to_csv(scraped_data)
