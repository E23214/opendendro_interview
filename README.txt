To analyze CSV data, place the file you want in the folder CSV_DATA. Then, call the python program from 
the command line with the name of the file you want to analyze. For the statistics summary,
enter the number of columns you want to analyze. If you want a full stats summary (similar to that given in
the R example) also add "stats"
example commandline argument using files already existing in the folder:
python3 CSV_Tree.py TTHH_raw.csv 3

To end the program, exit out of the graph generated.

The program works by parsing the csv file into the pandas DataFrame data structure. This section mainly
explains how the pandas library is working (or at least my understanding of how it working). I apologize
if I both under and over explain, as this is the first time I am using the pandas library. Instead of 
going through each line, I'm going to try and explain the things necesarry to understand the other
parts of the code and avoid the more self explanatory parts.

For the stats summary, most use the pandas dataframe methods (e.g., DataFrame[Column_Name].std() 
 give the std deviation of the number values in the column) to get the result. To find the first year
 where data occurs I used data[i].index.get_loc(data[i].first_valid_index()) to find the index of the row
 of the first and just put the data.at[index_of_first_valid_input, 'Year'] to find the year of that first 
 instance.

For the full stats, it's similar. To find the total numver of valid inputs, 
 I used (data.shape[0])-data.isna().sum()).mean(). In order to explain this, I need to the way the pandas dataframe
 methods work.Many of the dataframe methods (e.g., .mean()) return a dataframe with 
 the first column being column names and then the performed operation as the second column.
 So, the operations where I do .sum().sum() returns the total sum of whatever dataframe I am referring 
 to. .isna() returns a dataframe where the invalid inputs (non numbers) 
 are True and valid inputs are False. data.isna().sum().sum() retruns the total number of invalid inputs.
 data.shape[0] gives the number of rows, data.shape[1] gives the number of columns. So, the whole
 statement "data.shape[0])-data.isna().sum()).mean()" gives the total number of valid inputs.


For the graph, I copied it almost whole cloth from a post about making a spaghetti graph.
    palette = plt.cm.twilight(np.linspace(0, 1, len(data.columns)+1))
    This line generates a color palette with using matplotlib using matplotlib.cm.twilight() method.
    I changed the color palette from rainbow to twilight because I thought it was slightly more readable
        The numpy.linspace((0, 1, len(data.columns)+1)) generates (len(data.columns)+1) equally spaced values
        between 0 and 1

    The line of code:
        plt.plot(data[xAxis], data[column], marker='', linewidth=.75, alpha=0.9, label=column, color = palette[num])
        uses the matplotlib.plot method instead of the pandas dataframe.plot() since the pandas one made individual
        graphs for each one. I used data[xAxis] to make it be able to read ANY csv file (but the rest of my code doesnt so
        kind of a moot point)

    The legend needed to be sort of dynamic so the arguemnt loc='best' places it in the location which
    minimizees the overlap with the lines on the graph. If I were to iterate on it, I would make the ncol
    dynamic to the number of columns
         plt.legend(loc='best', ncol=6, markerscale=.5,fontsize='small')

To make the program work better with other csv files I used dataframe.columns[0] instead of "Year" so that 
it doesn't need the same capitalization. 

To make the requirements.txt, I found this 
https://stackoverflow.com/questions/31684375/automatically-create-requirements-txt 
    So, I just put in the command line
    pip install pipreqs

    pipreqs /path/to/project
