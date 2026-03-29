from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except Exception:
        return []


def read_csv():
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception:
        return []
    return products


def read_sql():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
    except Exception:
        return None  # special case for DB error
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # ❌ Invalid source
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # 📦 Load data
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:  # sql
        data = read_sql()
        if data is None:
            return render_template('product_display.html', error="Database error")

    # 🔍 Filter by id
    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p.get('id') == product_id]
        except ValueError:
            data = []

        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
