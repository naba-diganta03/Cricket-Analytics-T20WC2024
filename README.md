# Cricket Analytics - T20 World Cup 2024

This project performs analytics on ICC Men's T20 World Cup 2024 data using web scraping and visualization tools. It scrapes match data from ESPN Cricinfo and prepares it for analysis in Power BI.

---

## Features

- **Web Scraper** to collect match-level player data using Selenium.
- **Power BI Dashboard** to visualize batting performance metrics.
- **Focus on Best XI**: Dashboard aims to help in identifying and fixing the **best playing XI** based on player performances.
---

## Tools & Technologies Used

- Python 
  - `Selenium`
  - `Pandas`
- Microsoft Edge WebDriver
- Power BI
- ESPN Cricinfo as the data source

---

## How to Run the Scraper

1. Install dependencies:
    ```bash
    pip install selenium pandas webdriver-manager
    ```

2. Run the scraper:
    ```bash
    python scripts/scraper.py
    ```

3. CSV will be saved in the `data/` folder.

---

## Power BI

- Open the `.pbix` file.
- Includes the best playing XI from the tournament.

---

## Author

Developed by [Nabadiganta Acharjee](https://github.com/naba-diganta03)

