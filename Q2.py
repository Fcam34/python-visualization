# CMT309 Coursework 2
# student number:C1966881

# 2.1 Visualisation
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def sale_history(df):
	df = pd.read_csv('G:\\新建文件夹\\新建文件夹\\orders_cardiff_drinks.csv')
	df['order_date'] = pd.to_datetime(df['order_date'])
	df['order_date'] = df['order_date'].dt.year
	plt.bar(df['order_date'].astype(float) - 0.3, df['soda_qty'], alpha=0.9, width=0.25, color='Skyblue',
			label='soda_qty')
	plt.bar(df['order_date'].astype(float), df['wine_qty'], alpha=0.9, width=0.25, color='Orange', label='wine_qty')
	plt.bar(df['order_date'].astype(float) + 0.3, df['juice_qty'], alpha=0.9, width=0.25, color='lightgreen',
			label='juice_qty')
	plt.legend()
	plt.show()


# 2.2 Visualisation

def heatmap(df):
	df = pd.read_csv('G:\\新建文件夹\\新建文件夹\\orders_cardiff_drinks.csv')
	df['order_date'] = pd.to_datetime(df['order_date'])
	df['order_date'] = df['order_date'].dt.year
	cols = list(df)
	cols.insert(10, cols.pop(cols.index('total')))
	df = df.loc[:, cols]

	C = df.loc[:, 'soda_qty':'total'].corr()
	sns.heatmap(C, cmap="GnBu")
	plt.show()

	# df -> df = pd.read_csv(orders_cardiff_drinks.csv)
	# your code here, should generate a figure and it does not need to return anything


# 2.3: QUESTIONS

# •	How many orders were placed in 2016?

def count_orders_2016(df):
	df = pd.read_csv('G:\\新建文件夹\\新建文件夹\\orders_cardiff_drinks.csv')
	df['order_date'] = pd.to_datetime(df['order_date'])
	df['order_date'] = df['order_date'].dt.year
	numb_orders = ''
	data_2016 = df.loc[df['order_date'] == 2016]
	numb_orders =data_2016['total'].sum()

	# answer:2035449

	return numb_orders



# •	Which client has purchased the most number of soda bottles overall?

def best_client_soda_bottles(df):
	df = pd.read_csv('G:\\新建文件夹\\新建文件夹\\orders_cardiff_drinks.csv')
	df['order_date'] = pd.to_datetime(df['order_date'])
	df['order_date'] = df['order_date'].dt.year

	best_client_id = ''
	Soda = df['soda_qty'].groupby(df['client_id']).sum()
	best_client_id=Soda.idxmax()

	# answer:4161

	return best_client_id

# •	In which weekday is wine sold the most on average
# (across the whole sales history)?

def best_weekday_for_wine(df):
	df = pd.read_csv('G:\\新建文件夹\\新建文件夹\\orders_cardiff_drinks.csv')
	df['order_date'] = pd.to_datetime(df['order_date'])
	df['order_date'] = df['order_date'].dt.strftime("%A")
	Wine = df['wine_qty'].groupby(df['order_date']).mean()
	best_weekday = ''
	best_weekday =Wine.idxmax()

	# answer:Monday

	return best_weekday

# •	Which drink was the most popular (in GBP) in winter
#    (from Dec 21st to March 21st)? Break your answer down for each year.

def most_popular_drink(df):
	df = pd.read_csv('G:\\新建文件夹\\新建文件夹\\orders_cardiff_drinks.csv')
	df['order_date'] = pd.to_datetime(df['order_date'])
	df['order_date'] = df['order_date'].dt.strftime("%Y-%m-%d")
	d = {} # d could be {2009:'wine',2010:'soda',2011:'soda' ... }
	df = df.groupby(df['order_date']).sum()
	Drink_2013 = df.loc["2013-12-21":"2014-03-21", "soda_gbp":"juice_gbp"].sum()
	Drink_2014 = df.loc["2014-12-21":"2015-03-21", "soda_gbp":"juice_gbp"].sum()
	Drink_2015 = df.loc["2015-12-21":"2016-03-21", "soda_gbp":"juice_gbp"].sum()
	Drink_2016 = df.loc["2016-12-21":"2017-03-21", "soda_gbp":"juice_gbp"].sum()
	d={2013:Drink_2013.idxmax(),2014:Drink_2014.idxmax(),2015:Drink_2015.idxmax(),2016:Drink_2016.idxmax()}

	#answer:{2013:'soda',2014:'soda',2015:'soda' ,2016:'juice' }

	# your code here
	return d

# •	In which year-month (e.g. January 2015) was there the
#   highest number of orders in which the quantity of wine bottles
#   was higher than the average for that year?

def best_yearmonth_aboveavg_wine(df):
	df = pd.read_csv('G:\\新建文件夹\\新建文件夹\\orders_cardiff_drinks.csv')
	df['order_date'] = pd.to_datetime(df['order_date'])
	df['order_date'] = df['order_date'].dt.strftime("%Y-%m")
	drink_month = df.groupby(df['order_date']).sum()
	wine_month = drink_month["wine_qty"]

	average_2014 = wine_month.loc['2014-01':'2014-12'].mean()
	max_2014 = wine_month.loc['2014-01':'2014-12'].max()
	maxmonth_2014 = wine_month.loc['2014-01':'2014-12'].idxmax()
	number_2014 = max_2014 - average_2014

	average_2015 = wine_month.loc['2015-01':'2015-12'].mean()
	max_2015 = wine_month.loc['2015-01':'2015-12'].max()
	maxmonth_2015 = wine_month.loc['2015-01':'2015-12'].idxmax()
	number_2015 = max_2015 - average_2015

	average_2016 = wine_month.loc['2016-01':'2016-12'].mean()
	max_2016 = wine_month.loc['2016-01':'2016-12'].max()
	maxmonth_2016 = wine_month.loc['2016-01':'2016-12'].idxmax()
	number_2016 = max_2016 - average_2016

	data = {'Answer': {maxmonth_2014: number_2014, maxmonth_2015: number_2015, maxmonth_2016: number_2016}}
	answer = pd.DataFrame(data)

	best_ym = ''
	best_ym =answer.idxmax()

	#answer:2016-12

	# your code here
	return best_ym


# Test
df = pd.read_csv('G:\\新建文件夹\\新建文件夹\\orders_cardiff_drinks.csv')
sale_history(df)
heatmap(df)
print('How many orders were placed in 2016?')
print(count_orders_2016(df))
print('Which client has purchased the most number of soda bottles overall?')
print(best_client_soda_bottles(df))
print('In which weekday is wine sold the most on average?')
print(best_weekday_for_wine(df))
print('Which drink was the most popular (in GBP) in winter?')
print(most_popular_drink(df))
print('In which year-month (e.g. January 2015) was there the highest number of orders in which the quantity of wine bottles was higher than the average for that year?')
print(best_yearmonth_aboveavg_wine(df))