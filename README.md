# InventoryApp

An Inventory Management System with login authentication, product master, supplier selection, goods receiving, stock tracking, and sales processing. Built with Python, PySide6, and MySQL.

## Features

- 👥 User roles: Admin and Operator (Cashier)
- 🔒 Hashed password login (offline-ready)
- 📦 Product Master: SKU, barcode, category, images, GST, etc.
- 📥 Goods Receiving: Updates stock and calculates tax
- 📊 Inventory Management with min/max stock checks
- 💰 Sales Form: Updates stock and calculates totals
- 🧰 Built using PySide6 (GUI) and MySQL

## Setup

1. Clone this repo
2. Run MySQL and import `db_schema.sql`
3. Run `insert_user.py` to create initial users
4. Run `main.py` to start the app

## Sample Logins

- Admin: `admin` / `123456`
- Operator1: `operator1` / `123456`
- Operator2: `operator2` / `123456`

---

Made as part of a candidate assignment for **InfowareIndia**
