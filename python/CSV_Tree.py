import csv
import matplotlib
import sys
import pandas
import os

def CSV_Parser():
        with open("./CSV DATA/TTHH_raw.csv") as csv_file:
            columns = []
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    columns = row
                    line_count+=1
                else:
                    print(line_count,end=',')
                    line_count+=1

            
        if(len(sys.argv) == 1):
           CSV_data = pandas.read_csv("./CSV DATA/TTHH_raw.csv")
        else:
            CSV_data = pandas.read_csv(sys.argv[1])
        print(CSV_data.columns)
CSV_Parser()