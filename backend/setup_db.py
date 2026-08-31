#!/usr/bin/env python3
"""Setup MySQL database for AI Material Management System"""

import pymysql
from pymysql.err import ProgrammingError

# Connection without database
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='Mohith@123'
)

cursor = conn.cursor()

# Create database
try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS ai_material_management")
    print("✓ Database created successfully")
except ProgrammingError as e:
    print(f"✗ Error creating database: {e}")
    cursor.close()
    conn.close()
    exit(1)

# Switch to the database
cursor.execute("USE ai_material_management")

# Create tables
tables = [
    """
    CREATE TABLE IF NOT EXISTS users (
      id INT AUTO_INCREMENT PRIMARY KEY,
      username VARCHAR(100) UNIQUE NOT NULL,
      email VARCHAR(255) UNIQUE NOT NULL,
      password_hash VARCHAR(255) NOT NULL,
      role VARCHAR(50) NOT NULL,
      is_active BOOLEAN DEFAULT TRUE,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS materials (
      id INT AUTO_INCREMENT PRIMARY KEY,
      material_id VARCHAR(100) UNIQUE NOT NULL,
      name VARCHAR(255) NOT NULL,
      category VARCHAR(100) NOT NULL,
      unit VARCHAR(50) NOT NULL,
      quantity FLOAT DEFAULT 0,
      minimum_stock FLOAT DEFAULT 0,
      reorder_level FLOAT DEFAULT 0,
      storage_location VARCHAR(255),
      supplier VARCHAR(255),
      status VARCHAR(50) DEFAULT 'Active',
      specifications TEXT,
      storage_rules TEXT,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS suppliers (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      contact_person VARCHAR(255),
      email VARCHAR(255),
      phone VARCHAR(50),
      address VARCHAR(500),
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS warehouses (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      location VARCHAR(255),
      capacity FLOAT DEFAULT 0,
      manager VARCHAR(255),
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS purchase_requests (
      id INT AUTO_INCREMENT PRIMARY KEY,
      request_number VARCHAR(100) UNIQUE NOT NULL,
      material_name VARCHAR(255) NOT NULL,
      quantity FLOAT DEFAULT 0,
      supplier VARCHAR(255),
      priority VARCHAR(50) DEFAULT 'Medium',
      urgency VARCHAR(50) DEFAULT 'Normal',
      project_reference VARCHAR(255),
      status VARCHAR(50) DEFAULT 'Pending',
      requested_by VARCHAR(100),
      remarks VARCHAR(500),
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS inventory_transactions (
      id INT AUTO_INCREMENT PRIMARY KEY,
      material_name VARCHAR(255) NOT NULL,
      transaction_type VARCHAR(50) NOT NULL,
      quantity FLOAT DEFAULT 0,
      reference VARCHAR(255),
      remarks VARCHAR(500),
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS reports (
      id INT AUTO_INCREMENT PRIMARY KEY,
      title VARCHAR(255) NOT NULL,
      report_type VARCHAR(100) NOT NULL,
      summary VARCHAR(2000),
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS quality_inspections (
      id INT AUTO_INCREMENT PRIMARY KEY,
      grn_number VARCHAR(100) UNIQUE NOT NULL,
      purchase_request_id VARCHAR(100) NOT NULL,
      material_name VARCHAR(255) NOT NULL,
      ordered_quantity FLOAT NOT NULL,
      received_quantity FLOAT NOT NULL,
      accepted_quantity FLOAT DEFAULT 0,
      rejected_quantity FLOAT DEFAULT 0,
      batch_number VARCHAR(100),
      inspection_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      inspector_name VARCHAR(255),
      inspection_remarks TEXT,
      defects_found TEXT,
      quality_status VARCHAR(50) DEFAULT 'Pending',
      warehouse_location VARCHAR(255),
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS goods_receiving (
      id INT AUTO_INCREMENT PRIMARY KEY,
      grn_number VARCHAR(100) UNIQUE NOT NULL,
      po_number VARCHAR(100) NOT NULL,
      supplier_name VARCHAR(255) NOT NULL,
      material_name VARCHAR(255) NOT NULL,
      batch_number VARCHAR(100),
      ordered_quantity FLOAT NOT NULL,
      received_quantity FLOAT NOT NULL,
      unit VARCHAR(50) NOT NULL,
      receiving_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      received_by VARCHAR(255),
      warehouse_location VARCHAR(255),
      invoice_number VARCHAR(100),
      invoice_date DATETIME,
      remarks TEXT,
      transport_details VARCHAR(500),
      damage_or_short TEXT,
      receiving_status VARCHAR(50) DEFAULT 'Received',
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
    """
]

for i, table_sql in enumerate(tables, 1):
    try:
        cursor.execute(table_sql)
        print(f"✓ Table {i}/9 created successfully")
    except ProgrammingError as e:
        print(f"✗ Error creating table {i}: {e}")

print("\n✓ Database setup complete!")
cursor.close()
conn.commit()
conn.close()
