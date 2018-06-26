
###############################################################################
#                                                                             #
#    Document parser for Apache web server error log files. Transforms        #
#    error log into CSV file for easier viewing and manipulation.             #
#                                                                             #
###############################################################################



import datetime
import sys

input_file = input('Input the path of the Apache log file you would like to parse (e.g. /etc/Apache2/logs/error.log): \n \n')
output_file = input('Input the path to the CSV file you will write t (e.g. /home/username/output.csv \n '
                   'WARNING. If you enter the name of an existing file it will be overwritten.: \n \n')

num_lines = sum(1 for line in open(input_file))

counter = 0

process_option = int(input('The .log file you have selected contains ' + str(num_lines) + '\n'
      'Please select an option to continue:\n 1. Parse entire file \n 2. Specify the number of lines \n 3. EXIT \n \n'))

if process_option == 1:
    start_line = 0
elif process_option == 2:
    desired_lines = int(input("How many lines would you like to output? The most recent lines will be outputted (e.g. 5000). \n \n"))
    if desired_lines > num_lines:
        start_line = 0
    else:
        start_line = num_lines - desired_lines
elif process_option == 3:
    print("You have chosen to terminate the program")
    sys.exit(0)
else:
    print("You have selected an invalid option. The program will now terminate")
    sys.exit(0)

csv_file = open(output_file,'w')
csv_file.write("LINE,DATE, TIME,ERROR TYPE,PID,CLIENT,ERROR\n")

clean_list = ["," , "pid", "client", ",", "["]


with open(input_file) as f:
    for line in f:
        for item in clean_list:
            line = line.replace(item,"")
            sections = line.split("]", maxsplit=4)
            timeInfo = sections[0].split(" ")

        if counter >= start_line:
            outLine = str(counter+1) + "," + timeInfo[4].replace(" ","") + \
                      datetime.datetime.strptime(timeInfo[1], "%b").strftime("%m").replace(" ","") + \
                      timeInfo[2].replace(" ","") + "," +  timeInfo[3].replace(" ","") + "," + \
                      sections[1].replace(" ","") + "," + sections[2].replace(" ","") + "," + sections[3].replace(" ","") +\
                      "," + sections[4].replace("]","")
            csv_file.write(outLine)
            print(counter)
            print(outLine)
        counter+=1
csv_file.close()








