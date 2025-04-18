import pandas;
import requests;
from os import path;
from zipfile import ZipFile;

class utilities:
	DEBUG = False;

	def log(string):
		if utilities.DEBUG == True:
			print(str(string));

	def downloadUrl(url, save_path, chunk_size = 128):
		utilities.log("Download file.");
		headers = {
			"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
		};
		r = requests.get(url, headers = headers, stream = True);
		with open(save_path, "wb") as fd:
			for chunk in r.iter_content(chunk_size = chunk_size):
				fd.write(chunk);

	def extractZip(filePath, destination):
	    utilities.log("Extract files from ZIP.");
	    if path.exists(filePath):
	        with ZipFile(filePath, "r") as zipObj:
	            zipObj.extractall(destination);
	    else:
	        print("File " + filePath + " does not exists.");

	def readCsvFile(filePath):
	    utilities.log("Read CSV file.");
	    if path.exists(filePath):
	        return pandas.read_csv(filePath);
	    else:
	        print("File " + filePath + " does not exists.");
