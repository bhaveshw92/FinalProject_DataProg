from flask import Flask, render_template
import pandas as pd
import numpy
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/google-charts/second-chart")
def google_bar_chart():
    # Read the Nobel Prize data from the Excel file
    df = pd.read_excel('prize.xlsx')
   # print(df.head())

    # Group the data by category and count the number of laureates in each category
    category_counts = df.groupby('category')['laureates.id'].count().reset_index()

    # Group the data by year and count the number of prizes in each year
    year_counts = df.groupby('year')['Name'].count().reset_index()


    # Convert the data to a format that can be used by Google Charts
    category_data  = category_counts.values.tolist()
    category_data.insert(0, ['Category', 'Number of Laureates'])
    
    # Convert the year counts to a list
    year_data = year_counts.values.tolist()
    year_data.insert(0, ['Year', 'Number of Prizes'])

    # Render the template with the chart data
    
    # Create a pivot table with category as the rows, year as the columns, and the count of prizes as the values
    prize_table = pd.pivot_table(df, values='year', index='category', aggfunc=pd.Series.count)


    prize_table = prize_table.rename(columns={'year': 'Count of Year'})
    prize_table['Count of Year'] = pd.to_numeric(prize_table['Count of Year'])  # convert to numeric data type

    # Compute grand total and append it to the DataFrame
    grand_total = prize_table['Count of Year'].sum()
    prize_table.loc['Grand Total'] = grand_total

    # Convert the pivot table to a list of lists for use in Google Charts
    prize_data = prize_table.reset_index().values.tolist()
   
    print(prize_data)
    #sys.exit()
    return render_template('chart2.html', category_data=category_data, year_count=year_data, prize_data=prize_data)
    
if __name__ == "__main__":
    app.run(debug=True)
