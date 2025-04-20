import csv
import os
import sys

# Ensure access to manager class
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.guests import GuestManager

OUTPUT_FILE = os.path.join('data', 'guest_list_export.csv')

def export_guests_to_csv():
    gm = GuestManager()
    guests = gm.list_all()

    if not guests:
        print("❌ No guests found to export.")
        return

    with open(OUTPUT_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=[
            'id', 'name', 'email', 'phone', 'rsvp_status', 'dietary_notes', 'seating_table'
        ])
        writer.writeheader()
        writer.writerows(guests)

    print(f"✅ Guest list exported to {OUTPUT_FILE}")

if __name__ == '__main__':
    export_guests_to_csv()
