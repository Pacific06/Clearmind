# Clearmind
Code for an assignment using backtrader

### Question:
Perform a backtest using the backtrader library by making the indicator as mentioned below and provide the following output.
- Trade list output in CSV
- Indicator value output in CSV
- Basic Screener output - Image
- Indicator & Trade plotting - Image


### Installation:
- python 3.7
- pandas
- matplotlib
- backtrader
- xlrd


### Solution:
###### Preprocess the data from excel to text using pandas (preprocessing.py): 
- Dropped columns - SYMBOL and INTERVAL.
- Converted DATE values to a single format of %Y-%m-%d.
- Exported dataframe to comma separated format in a text file **data.txt**.

###### Ran backtrader functions on data.txt (solution.py):
- Used cerebro class with initial cash of 100000 and broker commission of 0.1%.
- Ran the strategy on whole data from 1994 to 2020. 
- Added a MovingAverageSimple indicator
- Trade list and indicator value at **tradeList.csv**
- Plotting at **plot.png**.

###### Output:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 102455923.69


