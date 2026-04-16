"""
Script to generate 100k lead records as a CSV file for testing.
Usage: python generate_data.py
Output: leads_100k.csv
"""

import csv
import random
from datetime import datetime, timedelta

AGENTS = [
    "Sarah Johnson", "Mike Chen", "Lisa Williams", "James Brown",
    "Emily Davis", "Robert Wilson", "Jessica Martinez", "David Anderson",
    "Amanda Taylor", "Chris Thomas", "Rachel Garcia", "Kevin Jackson",
    "Michelle Lee", "Brian Harris", "Stephanie Clark", "Andrew Lewis",
    "Nicole Robinson", "Daniel Walker", "Laura Hall", "Ryan Young"
]

SOURCES = [
    "Google Ads", "Facebook", "LinkedIn", "Referral",
    "Cold Call", "Website", "Email Campaign", "Trade Show",
    "Partner", "Organic Search"
]

STATUSES = ["New", "Contacted", "Qualified", "Converted", "Lost"]

# Weighted probabilities for status
STATUS_WEIGHTS = [0.25, 0.20, 0.20, 0.20, 0.15]

NUM_RECORDS = 100_000
OUTPUT_FILE = "leads_100k.csv"


def random_date(start_year=2023, end_year=2024):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)


def generate_leads(num_records):
    leads = []
    for i in range(1, num_records + 1):
        agent = random.choice(AGENTS)
        source = random.choice(SOURCES)
        status = random.choices(STATUSES, weights=STATUS_WEIGHTS, k=1)[0]

        # Revenue: only converted leads have meaningful revenue
        if status == "Converted":
            revenue = round(random.uniform(500, 50000), 2)
        elif status == "Qualified":
            revenue = round(random.uniform(0, 5000), 2)
        else:
            revenue = 0.0

        created_at = random_date().strftime("%Y-%m-%d %H:%M:%S")

        leads.append({
            "LeadID": i,
            "Agent": agent,
            "Source": source,
            "Status": status,
            "Revenue": revenue,
            "CreatedAt": created_at
        })

    return leads


def main():
    print(f"Generating {NUM_RECORDS} lead records...")
    leads = generate_leads(NUM_RECORDS)

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["LeadID", "Agent", "Source", "Status", "Revenue", "CreatedAt"])
        writer.writeheader()
        writer.writerows(leads)

    print(f"Done! Saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
