# database.py

import sqlite3

def save_to_db(records):
    conn = sqlite3.connect("data/population.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        country TEXT,
        population TEXT,
        year TEXT,
        population_millions REAL
    )
    """)

    for record in records:
        country, population, year, population_millions = record

        cursor.execute(
            "SELECT 1 FROM countries WHERE country = ? AND year = ?",
            (country, year)
        )

        if cursor.fetchone() is None:
            cursor.execute(
                "INSERT INTO countries (country, population, year, population_millions) VALUES (?, ?, ?, ?)",
                record
            )

    conn.commit()
    conn.close()
