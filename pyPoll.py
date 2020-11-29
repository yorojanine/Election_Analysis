# 1.Total Number of Votes Cast
# 2. A complete list of candidates who rec'd votes
# 3. Total Number of votes each candidate rec'd
# 4. Percentage of votes each candidate rec'd (# of votes per candidate/Total number of votes)
# 5. The winner of the election based on popular vote

#the path to the csv can be written like this:
#Windows: Uses a backward slashes to separate folders and files. "\"
#resources\election_results.csv
             ##this is not working for me -- need some help

    # import the datetime class from the datatime module
#import datetime as dt
    # use the now() attribute on the datetime class to get the present time || now = (firstdoll.seconddoll.thirddoll)
#now = dt.datetime.now()
    # print the present time
#print ("The time right now is ", now)

##opening a file
#general format for opening a file
#file_variable  = open(filename,mode)
    #file_variable is the name of the variable that will reference the file object
    #filename is the string specifying the name of the file
    #mode specifys the mode for reading - "r" means read, "w" means write, and it will overwrite,
    #"x" if file doesn't exist, it will not create it, "a" means append, it will only add to an existing file. 
    #"+" opens a file for reading and writing

#set a variable for our path
#file_to_load = 'resources\election_results.csv' 
#open the election results and read the file
   #election_data = open(file_to_load,'r')
#with open(file_to_load) as election_data:
#    print(election_data)
#to do: perform the analysis

#close the file
#election_data.close() ## no longer needed because we used "with" statement

# add our dependencies
import csv
import os

file_to_load = os.path.join("resources","election_results.csv")
#with open(file_to_load) as election_data:
#    print(election_data) 

#create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")
    #using the open() function with the "w" mode we will write data to the file
#outfile=open(file_to_save,"w")
#outfile.write("Hello World")
#outfile.close()

#with open(file_to_save,"w") as txt_file:
    #txt_file.write("arapahoe, ")
    #txt_file.write("denver, ")
    #txt_file.write("jefferson")
#    txt_file.write("counties in the election\n-----------------------\narapahoe\ndenver\njefferson")

with open(file_to_load) as election_data:
    #to do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    #print the header row
    headers = next(file_reader)
    print(headers)
    # print each row in the csv file
   # for row in file_reader:
      #  print(row)