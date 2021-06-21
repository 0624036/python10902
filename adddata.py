import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings')
django.setup()

import csv
from mainsite.models import Visitor_202105, Visitor_202104, Visitor_202103, Visitor_202102, Visitor_202101

with open("database/202105.csv", "r",encoding='UTF-8-sig') as fp:
	rows = csv.DictReader(fp)
	for row in rows:
		print("1")
		date = row['date']
		number = row['number']
		c = Visitor_202105(date=date, number=number)
		c.save()
print("Done~~")

with open("database/202104.csv", "r",encoding='UTF-8-sig') as fp:
	rows = csv.DictReader(fp)
	for row in rows:
		date = row["date"]
		number = row["number"]
		c = Visitor_202104(date=date, number=number)
		c.save()
print("Done~~")
with open("database/202103.csv", "r",encoding='UTF-8-sig') as fp:
	rows = csv.DictReader(fp)
	for row in rows:
		date = row["date"]
		number = row["number"]
		c = Visitor_202103(date=date, number=number)
		c.save()
print("Done~~")
with open("database/202102.csv", "r",encoding='UTF-8-sig') as fp:
	rows = csv.DictReader(fp)
	for row in rows:
		date = row["date"]
		number = row["number"]
		c = Visitor_202102(date=date, number=number)
		c.save()
print("Done~~")
with open("database/202101.csv", "r",encoding='UTF-8-sig') as fp:
	rows = csv.DictReader(fp)
	for row in rows:
		date = row["date"]
		number = row["number"]
		c = Visitor_202101(date=date, number=number)
		c.save()
print("Done~~")