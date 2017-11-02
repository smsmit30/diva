##################################################################
Welcome to The Dating Diva roundup formatter README for MAC users
##################################################################

Version 1.1 changes:
Now supports an optional source column! If the file you are formatting has the optional source column it will add the source to the HTML. If it does not have the optional source column it will format it the same as it normally does.

Contents:
-diva_roundup_README.txt: this file :)
-diva_roundup_formatter.pyw: Python script that will format your text file into formatted HTML.
-DEMO.mov: Movie showing how to use the script.
-sample google sheet layout.png: Sample of how to set up your google sheet. 
-sample.tsv: Sample of the tab delimited file.

Setup:
Organize roundup Excel/Google sheet in the following four columns (see sample below):

Number	Title	Link	Source (optional)	Description (The script will ask if your file has this header line or not)
1	Avocado Fries	http://www.link1.com	Source 1	Wow! So these not only look great… 
2	Shamrock Chips	http://www.link2.com	Source 2	Chips and dip are the perfect party treat…
3	Pea Soup	http://www.link3.com	Source 3	This would be a great dinner option for a party…
4	Spinach Quiche	http://www.link4.com	Source 4	This is a party favorite… 
5	Cheese Crostini	http://www.link5.com	Source 5	What a sophisticated and delicious party snack!

Once all roundup items are organized in a single spreadsheet export your excel file as tab delimited file (.txt) or if in google sheets download as tab separated values (.tsv). Make sure there are no spaces in the filename. If you have spaces (or special characters) in your filename change them to underscores “_” (keep everything to 0-9 a-z and _). The directory you save the file in can not have spaces or special characters either. This goes for ALL parent directories of the chosen save location. The Desktop is always a good safe place to save it so you don’t have to worry about this problem! Then after you run the program you can move it to a new location or discard.

Executing the script:

Double click on diva_roundup_formatter.pyw and follow the on screen directions.

Copy the contents of the new file the script created and paste into txt mode of wordpress post editor.

voila!