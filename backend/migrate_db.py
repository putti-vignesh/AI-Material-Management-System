#!/usr/bin/env python3
"""Migrate existing database - add new columns"""

import pymysql
from pymysql.err import ProgrammingError

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='Mohith@123',
    database='ai_material_management'
)

cursor = conn.cursor()

# Alter tables to add new columns (proper MySQL syntax)
migrations = [
    """
    ALTER TABLE materials
    ADD COLUMN specifications TEXT
    """,
    """
    ALTER TABLE materials
    ADD COLUMN storage_rules TEXT
    """,
    """
    ALTER TABLE purchase_requests
    ADD COLUMN urgency VARCHAR(50) DEFAULT 'Normal'
    """,
    """
    ALTER TABLE purchase_requests
    ADD COLUMN project_reference VARCHAR(255)
    """
]

for i, migration_sql in enumerate(migrations, 1):
    try:
        cursor.execute(migration_sql)
        print(f"✓ Migration {i} completed successfully")
    except ProgrammingError as e:
        # Ignore "duplicate column" errors
        if "Duplicate column name" in str(e):
            print(f"✓ Migration {i} skipped (column already exists)")
        else:
            print(f"✗ Migration {i} error: {e}")

print("\n✓ Database migration complete!")
cursor.close()
conn.commit()
conn.close()
