import glob
import csv

def refine_dataset():
	n_f=open("updated_dataset.csv",'a')
	writer=csv.writer(n_f)
	csvFile=open("dataset.csv", 'r')
	reader=csv.reader(csvFile)
	for row in reader:
		n_row=[]
		if row != []:
			n_row=[row[2],row[1]]
			if '2012_Sandy_Hurricane' in row:
				n_row.append(1)
			elif '2013_Alberta_Floods' in row:
				n_row.append(2)
			elif '2013_Boston_Bombings' in row:
				n_row.append(3)
			elif '2013_Oklahoma_Tornado' in row:
				n_row.append(4)
			elif '2013_Queensland_Floods' in row:
				n_row.append(5)
			elif '2013_West_Texas_Explosion' in row:
				n_row.append(6)
			elif 'random' in row:
				n_row.append(7)
			writer.writerow(n_row)
if __name__=="__main__":
	refine_dataset()