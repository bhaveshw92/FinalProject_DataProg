# We tried to display data in google charts with the help of JSON String that we were getting from MongoDb output
# but as it was difficult to to process the output we switched to accessing the data from an Excel file.
 
from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/google-charts/chart')
def google_bar_chart():
    client = MongoClient("mongodb+srv://admin:Admin%40123@nobelprize.ktic81z.mongodb.net/NobelPrize?ssl=true&ssl_cert_reqs=CERT_NONE")
    db=client.get_database('NobelPrize')
    records = db.NobelPrizeCollection
    chart_data = list(records.find({}))

    # Query the data from the prizes collection
    data = []
    for prize in records.find():
        print(prize)  # Debug statement
        for laureate in prize['laureates']:
            data.append({'year': prize['year'], 'category': prize['category'], 'share': float(laureate['share'])})
    print(data)

#     # Aggregate the data by year
#     year_data = {}
#     for item in data:
#         if item['year'] not in year_data:
#             year_data[item['year']] = []
#         year_data[item['year']].append(item['share'])
#     print(year_data)

#     # Calculate the average share by year
#     avg_data = []
#     for year, shares in year_data.items():
#         avg_share = sum(shares) / len(shares)
#         avg_data.append({'year': year, 'avg_share': avg_share})
#     print(avg_data)

#     # Render the template with the chart data
#     return render_template('chart.html', data_table=avg_data)

if __name__ == '__main__':
    app.run(debug=True)
