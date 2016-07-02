# this imports the script ability
from sys import argv 
import sys
import time

# argv = argument vector ... this expects a parameter to run correctly...
# In this one it's a filename.
script, filename = argv 

print "We are going to erase and write to %r." % filename
#print "If you don't want that, hit CTRL-C (^C)."
#print "If you do want this, hit RETURN."

# This waits for either CTRL-C or RETURN(Enter)
raw_input("Press Enter to continue or press CRTL-D to quit.") 

#print "\nOpening the file:\n"
# opens the filename and adds the 'w' or write attribute.
target = open(filename, 'w') 

#print "Truncating the file.\n"
# displays ERASING FILE one letter at a time
string = "ERASING FILE...\n"
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.15)
# this erases the file
target.truncate() 

print "\nErasing file completed.\n"
print "Now I am going to ask you for three lines."

#  lines 19 thru 21 ask for user input
line1 = raw_input("line 1: ") 
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "\nI'm going to write these to the file.\n"
string = "WRITING TO FILE...\n"
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.25)

# prints line 1
target.write(line1)
# makes a new line 
target.write("\n")
# and so on ...  
target.write(line2) 
target.write("\n")
target.write(line3)
target.write("\n")

#print "And finally, we close the file for future mods.\n"
# closes the file... 
target.close()

# Ok, so for this one I am opening the file but I am doing it with a cool little loading bar.
print "\nDo you want to read the file you have just created?"
#print "If so hit RETURN, if not CTRL-D"
# waits for RETURN or CTRL-D
raw_input("Press Enter to continue or press CRTL-D to quit.")

print "Reading file, please wait:\n"
# asterik counter
string = "READING FILE...\n"
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.15)

txt = open(filename)

print "\nHere's your file %r:\n" % filename
print txt.read() 

txt.close()
target.close()
