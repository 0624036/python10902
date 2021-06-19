import os
import csv

class Station():
	stations = []
	with open('station_TPTC.csv','r', encoding='utf-8-sig') as csvFile:
		rows = csv.reader(csvFile, delimiter=',')
		for row in rows:
			print(row)
			stations.append(row)

