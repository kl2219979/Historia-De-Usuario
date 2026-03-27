from models.inventory import inventory
import csv 

with open('data/data.csv','w',encoding="utf-8",newline="") as f:
    writer = csv.DictWriter(f, fieldnames=['name','price','quantyti'])
    writer.writeheader()
    writer.writerows(inventory)
    