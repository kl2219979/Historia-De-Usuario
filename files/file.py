from models.data import inventory
from pathlib import Path
import csv

ruta = Path("data/file.csv")

def save_file():
    with ruta.open('w', encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name","price","quantyti"])
        writer.writeheader()
        writer.writerows(inventory)

def upload_file():
    with ruta.open('r', encoding="utf-8",newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['name']
            price = float(row['price'])
            quantyti = int(row['quantyti'])
            product = {"name":name,"price":price,"quantyti":quantyti}
            inventory.append(product)