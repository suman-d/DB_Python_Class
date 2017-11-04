
import csv


total = 0.0
with open("../Data/portfolio2.csv", "r") as f:
	rows = csv.reader(f)
	header = next(rows)

	for row in rows:

		row[2] = int(row[2])
		row[3] = float(row[3])

		total += row[2] * row[3]
		#print(row)

print ("Total Stocks worth: ", total)


