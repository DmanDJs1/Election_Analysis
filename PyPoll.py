# Import the datetime class from the datetime module.
import datetime as dt
import os
import csv 
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)


#Resources/election_results.csv

#dir()

# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources/election_results.csv')
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
#election_data.close()

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

     #print(dir(os))


# Open the election results and read the file
#with open('Resources/election_results.csv') as election_data:

     # To do: perform analysis.
     print(election_data)


# Create a filename variable to a direct or indirect path to the file.
     file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
     open(file_to_save, "w")

# Using the with statement open the file as a text file.
     outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")

# Close the file
#outfile.close()

# Write three counties to the file.
#outfile.write("Arapahoe")
#outfile.write("Denver")
#outfile.write("Jefferson")

# Write three counties to the file.
     outfile.write("Arapahoe\nDenver\nJefferson")

# Read the file object with the reader function.
     file_reader = csv.reader(election_data)

# Print each row in the CSV file.
     for row in file_reader:
          print(row)