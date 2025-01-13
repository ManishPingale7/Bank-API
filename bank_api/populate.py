# Make sure Django settings are configured
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bank_api.settings")
django.setup()

import sqlite3
from api.models import Bank, Branch
from django.db import transaction

# Connect to the SQLite final.db
sqlite_conn = sqlite3.connect('final.db')
sqlite_cursor = sqlite_conn.cursor()

# Step 1: Fetch data from the SQLite database (final.db)

# Fetching Banks data
sqlite_cursor.execute("SELECT id, name FROM banks")
banks_data = sqlite_cursor.fetchall()

# Fetching Branches data
sqlite_cursor.execute(
    "SELECT ifsc, bank_id, branch, address, city, district, state FROM branches")
branches_data = sqlite_cursor.fetchall()

# Step 2: Insert data into Django models

# Using Django's ORM to insert data into the `Bank` model
with transaction.atomic():  # Ensure that all inserts are in one transaction for efficiency
    for bank_row in banks_data:
        bank, created = Bank.objects.get_or_create(
            id=bank_row[0],
            name=bank_row[1]
        )

    # Insert data into the `Branch` model
    for branch_row in branches_data:
        # Map the bank_id in the SQLite table to the correct Bank instance
        bank_instance = Bank.objects.get(id=branch_row[1])

        Branch.objects.get_or_create(
            ifsc=branch_row[0],
            bank=bank_instance,  # Foreign Key relation
            branch=branch_row[2],
            address=branch_row[3],
            city=branch_row[4],
            district=branch_row[5],
            state=branch_row[6]
        )

# Close the SQLite connection
sqlite_conn.close()

print("Data has been successfully inserted into Django models.")
