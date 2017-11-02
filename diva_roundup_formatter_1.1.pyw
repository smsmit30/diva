#!/usr/bin/env python

import sys
import os
import subprocess
import re

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   BLINK = '\033[5m'
   PINK_B = '\033[95;1m'
   PINK = '\033[95m'
   END = '\033[0m'

numsize = 24
titlesize = 18
descriptsize = 14
print color.PINK_B + '\n#############################################\nWelcome to The Dating Divas Roundup Formatter\n\t~Written by Scott Smith\n#############################################\n' +color.END
print 'Version 1.1 now supports an additional source column!\n\nHello DIVA!'
tab_file = raw_input(color.PINK + "\n\n** Please drag the file you wish to format into the terminal window and press 'Enter': " + color.END)
tab_file = tab_file.rstrip()

print "\nChecking file path..."
if '\\' in tab_file:
	print '\n!!!!!WARNING!!!!! \nEither the title of your document or one of the folders in its path contains spaces or other unusual characters.'
	print 'Below is the path to your file. if you see \\ in the path the character that follows is the problem.'
	print tab_file
	print'Please rename your file or folder using only a-z 0-9 and _ then try again!\n'
	print color.BLINK + '\n\t***** Formatting FAILED *****\n' + color.END 
	print color.PINK_B + '#############################################\nThanks for using The Divas Roundup Formatter!\n#############################################' + color.END
	quit()
else:
	print "file path: GOOD!"

roundup = open(tab_file).readlines()

pattern = re.compile("^.*\t.*\t.*\t.*")
print "\nChecking file format..."
for line in roundup:
	if pattern.match(line):
		pass
	else:
		print '\n!!!!!WARNING!!!!! \nYour file does not appear to be a tab seperated file.\nPlease make sure you have the correct file and that it is formatted correctly then try again!\n\nnumber{TAB}title{TAB}link{TAB}description\n'
		print color.BLINK + '\n\t***** Formatting FAILED *****\n' + color.END
		print color.PINK_B + '#############################################\nThanks for using The Divas Roundup Formatter!\n#############################################' + color.END
		quit()

print "file format: GOOD!"

answer = str(raw_input(color.PINK + "\n** Does your file have a header? Enter Y for yes or N for no: " + color.END))
proceed= ['y','Y','yes','Yes','YES'] 
if answer in proceed:
	roundup = roundup[1:]
else:
	pass

print '\nDEFAULT font sizes:\nNumber size: ',str(numsize),'\nTitle size: ',str(titlesize),'\nDescription size: ',str(descriptsize),'\n'

answer = str(raw_input(color.PINK + "** Change default sizes? Enter Y for yes or N for no: " + color.END))
proceed= ['y','Y','yes','Yes','YES'] 
if answer in proceed:
	numsize = raw_input(color.PINK + '\n** Enter new NUMBER font size: ' + color.END)
	titlesize = raw_input(color.PINK + '** Enter new TITLE font size: ' + color.END)
	descriptsize = raw_input(color.PINK + '** Enter new DESCRIPTION font size: ' + color.END)
else:
	pass

numsize = str(numsize)
titlesize = str(titlesize)
descriptsize = str(descriptsize)

if answer in proceed:
	print '\nNEW font sizes:\nNumber size: ',str(numsize),'\nTitle size: ',str(titlesize),'\nDescription size: ',str(descriptsize),'\n'
else:
	pass
filename = tab_file
if filename.endswith('.txt'):
    filename = filename[:-4]
    filename = filename+"_"+"roundup_html.txt"
elif filename.endswith('.tsv'):
    filename = filename[:-4]
    filename = filename+"_"+"roundup_html.txt"
else:
	print ('\nunrecognized file type. Please use a .txt or .tsv file\n')
	print color.PINK_B + '#############################################\nThanks for using The Divas Roundup Formatter!\n#############################################' + color.END
	quit()
	
f = open(filename,'w')
for line in roundup:
	rulist = line.strip('\n').split("\t")
	out_line = ""
	if len(rulist) is 5:
		out_line = "<p><span style=\"font-weight: 400;\"></span> <strong> <span style=\"font-size: ",numsize,"pt;\">",rulist[0],". </span></strong><span style=\"font-size: ",titlesize,"pt;\"><a href=\"",rulist[2],"\" target=\"_blank\">",rulist[1],"</a> (",rulist[3],") -</span><span style=\"font-size: ",descriptsize,"pt;\">",rulist[4],"</span></p>","\n"
	elif len(rulist) is 4:
		out_line = "<p style=\"text-align: left;\"><span style=\"font-size: ",numsize,"pt;\"><strong>",rulist[0],". </strong></span><span style=\"font-size: ",titlesize,"pt;\"><a href=\"",rulist[2],"\" target=\"_blank\">",rulist[1],"</a> - </span><span style=\"font-size: ",descriptsize,"pt;\">",rulist[3],"</span></p>","\n"
	else:
		pass
	out_line_str = ''.join(out_line)
	if '<a href="" target="_blank">' in out_line_str:
		final_out_line = out_line_str.replace('<a href="" target="_blank">', '')
	else:
		final_out_line = out_line_str
	f.write(final_out_line)
f.close()

print color.BLINK + '\n\t***** Formatting complete! *****\n' + color.END
print "HTML is in file:",filename,'\n'

answer = str(raw_input(color.PINK + "** Would you like me to show you the file? Enter Y for yes or N for no: " + color.END))
proceed= ['y','Y','yes','Yes','YES'] 
print'\n'
if answer in proceed:
	subprocess.call(["open", "-R", filename])
	subprocess.Popen(['open', filename])
else:
	pass

print color.PINK_B + '#############################################\nThanks for using The Divas Roundup Formatter!\n#############################################' + color.END
quit()