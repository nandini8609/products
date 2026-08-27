import sqlite3

DB_NAME = "product.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_product(name, category, price, quantity):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO products (name, category, price, quantity)
        VALUES (?, ?, ?, ?)
    """, (name, category, price, quantity))

    conn.commit()
    conn.close()


def get_products():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products ORDER BY id")
    products = cursor.fetchall()

    conn.close()
    return products


def search_products(keyword):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM products
        WHERE name LIKE ? OR category LIKE ?
        ORDER BY id
    """, (f"%{keyword}%", f"%{keyword}%"))

    products = cursor.fetchall()

    conn.close()
    return products


def update_product(product_id, name, category, price, quantity):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE products
        SET name = ?, category = ?, price = ?, quantity = ?
        WHERE id = ?
    """, (name, category, price, quantity, product_id))

    updated = cursor.rowcount > 0

    conn.commit()
    conn.close()

    return updated


def delete_product(product_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (product_id,)
    )

    deleted = cursor.rowcount > 0

    conn.commit()
    conn.close()

    return deleted

def get_inventory_value():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(price * quantity)
        FROM products
    """)

    result = cursor.fetchone()[0]

    conn.close()

    return result or 0
