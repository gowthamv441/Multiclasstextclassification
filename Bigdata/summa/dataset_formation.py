import glob
import csv

def form_dataset():
	file_list=glob.glob("../CrisisLexT6/*/*.csv")
	n_f=open("dataset.csv",'a')
	writer=csv.writer(n_f)
	for file in file_list:
		event=file.split("\\")
		print (event[1])
		try:
			with open(file, 'r') as csvFile:
				reader=csv.reader(csvFile)
				for row in reader:
					if "on-topic" in row:
						row[2]=event[1]
						writer.writerow(row)
					elif "off-topic" in row:
						row[2]="random"
						writer.writerow(row)
		except:
			print ("ERROR --> Data Processing")

"""2012_Sandy_Hurricane
2013_Alberta_Floods
2013_Boston_Bombings
2013_Oklahoma_Tornado
2013_Queensland_Floods
2013_West_Texas_Explosion
random
"""
def find_proportion():
	labels=["2012_Sandy_Hurricane","2013_Alberta_Floods","2013_Boston_Bombings",
	"2013_Oklahoma_Tornado","2013_Queensland_Floods","2013_West_Texas_Explosion",
	"random"]
	labels_proportion=[0,0,0,0,0,0,0]
	with open("dataset.csv") as csvFile:
		reader=csv.reader(csvFile)
		row_count=0
		for row in reader:
			row_count+=1
			if '2012_Sandy_Hurricane' in row:
				labels_proportion[0]+=1
			elif '2013_Alberta_Floods' in row:
				labels_proportion[1]+=1
			elif '2013_Boston_Bombings' in row:
				labels_proportion[2]+=1
			elif '2013_Oklahoma_Tornado' in row:
				labels_proportion[3]+=1
			elif '2013_Queensland_Floods' in row:
				labels_proportion[4]+=1
			elif '2013_West_Texas_Explosion' in row:
				labels_proportion[5]+=1
			elif 'random' in row:
				labels_proportion[6]+=1
	print (row_count,sum(labels_proportion))
	print ("\n====labels distribution=====\n")
	for i in range(0,len(labels)):
		print ("label :: {} \ncount :: {} \n\n".format(labels[i],labels_proportion[i]))

if __name__=='__main__':
	#form_dataset()
	#find_proportion()