#use sys modules
from sys import argv
#get cli input
script, filename = argv
#open a file
txt = open(filename)
#output file name
print "Here's your file %r:" % filename
# output the file content
print txt.read()
txt.close()
#output notice
print "Type the filename again:"
#get cli input
file_again = raw_input('>')
#open a file
text_again = open(file_again)
#output file content
print text_again.read()
text_again.close()
