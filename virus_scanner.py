import subprocess
import fnmatch
import re
filename= str(raw_input('Enter filename :'))

#getting all the strings in the file
#calling strings command in shell using python
res = subprocess.check_output(["strings",filename])

str_list = res.splitlines()

dll_list=[]
websites=[]
def check_for_attributes(str_list):
	for line in str_list:
		#finding the dll files that the virus contains
		if ((fnmatch.fnmatch(line, '*.DLL')) or (fnmatch.fnmatch(line, '*.dll'))):
			if(line not in dll_list):
				dll_list.append(line)
		#finding the urls inside the virus
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
		if urls:
			websites.extend(urls)
		
	return 0;
used_dll=check_for_attributes(str_list)
i=0
if dll_list:
	i=1
	print ("***************************************************************")
	print ("DLLS that the virus may be using")
	print ("***************************************************************")
	for dll in dll_list:
		print (dll)
if websites:
	i=1
	print ("***************************************************************")
	print ("Urls that the virus may access")
	print ("***************************************************************")
	for website in websites:
		print (website)
if i==0:
	print ("Not a virus")




