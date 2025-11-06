# main.py

from scraper import get_countries
from database import save_to_db

def main():
    print("🧭 Starting scraper...")
    records = get_countries()
    print(f"✅ Scraped {len(records)} records.")

    print("💾 Saving to database...")
    save_to_db(records)
    print("✅ Done.")

if __name__ == "__main__":
    main()
