
import matplotlib.pyplot as plt
import sys
import pandas
import numpy as np
import os


def CSV_Parser():   
        directory =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if(len(sys.argv) == 1):#Basically, the default file argument
           CSV_data = pandas.read_csv(os.path.join(directory,"CSV_DATA/wa082.csv"))
        else:#user would put the custom 
            
            CSV_data = pandas.read_csv(os.path.join(directory,"CSV_DATA",sys.argv[1]))

        return CSV_data
def stats(data):#Full stats
        print(data.columns[1:]) #Prints the different columns, excluding the year
        print(f"Number of dated series:{len(data.columns)-1}")
        #will be abusing panda's datafram maniulation for the next few lines
        print(f"Avg series length: {((data.shape[0])-data.isna().sum()).mean()}")
        #Shape[0] gives the num of rows, isna() is the same format as data just with True where the
        #data is not a number. So, .sum gives the number of non-numbers in each column. 
        numDataPoints = data.shape[1]*data.shape[0]-data.isna().sum().sum() #BxH - a sum of a sum of the NAN values in each column
        print(f"Number of data points: {numDataPoints}")
        print(f"Some kind of avg std deviation {data.std().mean()}")

        for i in data.columns[1:]:
            idx = data[i].isnull()
            it = 0
            print(i+" years with missing data -- ",end='')
            for n in idx.array:
                if(n == True):
                    print(data.at[it,data.columns[0]],end=',')
                it+=1
            print()
            print()
def stats_summary(data, nums):
    print(f'{"##   series first last year  mean  median  stdev   skew":20}')
    row = 0
    for i in data.columns[1:]:
        row+=1
        ##https://stackoverflow.com/questions/22403469/locate-first-and-last-non-nan-values-in-a-pandas-dataframe to find inital year
        first = data.at[data[i].index.get_loc(data[i].first_valid_index()),data.columns[0]]
        last = data.at[data[i].index.get_loc(data[i].last_valid_index()),data.columns[0]]
        print(f"{f'## {row} {i} {first}  {last}      {data[i].mean():.4f} {data[i].median():.4f} {data[i].std():.4f} {data[i].skew():.4f}':20}")
        if row == nums:
            break

def Spaghetti_Plot(data,Selected_Range = 0, Selected_Columns = []):
    # Change the style of plot
       #Copied from here https://python-graph-gallery.com/124-spaghetti-plot
        plt.style.use('seaborn-darkgrid')
        # Create a color palette
        palette = plt.cm.twilight(np.linspace(0, 1, len(data.columns)+1))
        # Plot multiple  lines
        num = 0
        for column in data.columns:
            if num == 0:
                num +=1
                xAxis = column
            else:
                plt.plot(data[xAxis], data[column], marker='', linewidth=.75, alpha=0.9, label=column, color = palette[num])
                num+=1
        # Add legend
        plt.legend(loc='best', ncol=6, markerscale=.5,fontsize='small')
        
        # Add titles
        plt.title(f"Spaghetti Plot of {xAxis[0]}", loc='left', fontsize=12, fontweight=0, color='orange')
        plt.xlabel(data.columns[0])
        plt.ylabel("Not Sure what this data represents (tree ring series?)")
        plt.show()
if __name__ == '__main__':
    fData = CSV_Parser()
    length = 5
    for i in range(len(sys.argv)):
        if(sys.argv[i].isnumeric()):
            length = int(sys.argv[i])
        if sys.argv[i] == "stats":
            stats(fData)
    stats_summary(fData,length)
    Spaghetti_Plot(fData)
    exit
