from os import system 
import csv 

with open('test.csv', 'w') as file:
    mywriter = csv.writer(file)
    mywriter.writerow(['spam'] * 5)
    mywriter.writerow(['spam'])


