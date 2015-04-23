import os, csv
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


# exports csv files for a folder of .txt essays
# input must be a string

def main(directory):
	os.chdir(directory)
	fileList = [item for item in os.listdir(os.getcwd())]
	fileList.remove('.DS_Store'), fileList.remove('case-refs.csv')

	for i in fileList:
		os.chdir(directory)
		data = open(i).read()
		tokenizer = RegexpTokenizer(r'\w+')
		token = tokenizer.tokenize(data)
		stop = [str(word) for word in stopwords.words('english')]
		data = [j for j in token if j not in stop]

		uniData = [word.decode("utf-8", "ignore") for word in data]
		allData = [word.encode("ascii", "ignore") for word in uniData]
		allCountDict = {}

		for word in allData:
			allCountDict.update({word: allData.count(word)})
		print allCountDict
		os.chdir('/Users/Andrew/Dropbox/python/focus/Word_Analysis/output/')

		writer = csv.writer(open(str(i[:-4]) + '.csv', 'wb'))
		for key, value in allCountDict.items():
		   writer.writerow([key, value])
