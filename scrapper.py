from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Initialize the Edge WebDriver
driver = webdriver.Edge()

# ESPN Cricinfo match URL (Replace with actual match URL)
match_url = "https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/match-schedule-fixtures-and-results"
driver.get(match_url)

# Wait for the page to load
time.sleep(5)

# Find the first match link (Modify if needed to get specific matches)
match_links = driver.find_elements(By.XPATH, "//a[contains(@href, '/full-scorecard')]")
if match_links:
    first_match_url = match_links[0].get_attribute("href")
    driver.get(first_match_url)
    time.sleep(5)

# Locate the batting summary table
batting_tables = driver.find_elements(By.XPATH, "//table[contains(@class, 'ds-w-full ds-table')]")

# Extract batting summary
batting_data = []

for table in batting_tables:
    rows = table.find_elements(By.XPATH, ".//tbody/tr")
    for row in rows:
        try:
            # Extract batsman name
            batsman = row.find_element(By.XPATH, ".//td[1]//a").text.strip()

            # Extract dismissal (handling "not out" cases)
            try:
                dismissal = row.find_element(By.XPATH, ".//td[2]//span[2]").text.strip()
            except:
                dismissal = "not out"

            # Extract runs, balls, 4s, 6s, and strike rate
            runs = row.find_element(By.XPATH, ".//td[3]").text.strip()
            balls = row.find_element(By.XPATH, ".//td[4]").text.strip()
            fours = row.find_element(By.XPATH, ".//td[6]").text.strip()
            sixes = row.find_element(By.XPATH, ".//td[7]").text.strip()
            strike_rate = row.find_element(By.XPATH, ".//td[8]").text.strip()

            # Append data
            batting_data.append([batsman, dismissal, runs, balls, fours, sixes, strike_rate])

        except Exception as e:
            continue  # Skip non-player rows

# Save to CSV
batting_df = pd.DataFrame(batting_data, columns=["Batsman", "Dismissal", "Runs", "Balls", "4s", "6s", "Strike Rate"])
batting_df.to_csv("final_batting_summary.csv", index=False)

print("Batting summary saved successfully!")

# Close the browser
driver.quit()