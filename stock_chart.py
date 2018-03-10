import quandl
from flask import Flask, render_template
from werkzeug.contrib.cache import SimpleCache

app = Flask(__name__)
cache = SimpleCache()
quandl.ApiConfig.api_key = "zC992yeEkw5VTye5PFJY"
 
@app.route("/")
def index():
    return render_template('stock_chart.html')

@app.route("/data/<string:ticker>/")
def display_data(ticker):
    def retrieve_data(ticker):
        return quandl.get("EOD/{}".format(ticker), paginate=True)
    
    data = cache.get(ticker)
    if data is None:
        data = retrieve_data(ticker)
        data['200Day_Avg'] = data['Close'].rolling(200).mean() # add moving average
        cache.set(ticker, data)
    return data.to_csv()
 
if __name__ == "__main__":
    app.run(port=7777)
