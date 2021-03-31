"""
Problem3

Function to parse a log file & extract details of Errors & Warnings recorded into a separate file.
In python log file errors and warnings are represented with headers "ERROR" and "WARN"
"""
with open('logfile.log','r') as file: # Logfile
	errorFile = open('error.txt', 'w')
	for line in file: 
	    if ('ERROR' in line) or ('WARN' in line): # Search for ERROR in line
	        errorFile.write(line) # Writing to new file.
	errorFile.close()