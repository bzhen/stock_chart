# from flask import Flask, flash, redirect, render_template, request, session, abort
import quandl
from flask import Flask, render_template
app = Flask(__name__)

quandl.ApiConfig.api_key = "zC992yeEkw5VTye5PFJY"
 
@app.route("/")
def index():
    return render_template('stock_chart.html')

@app.route("/data")
def aapl_data():
    data = quandl.get("EOD/AAPL", returns="pandas", paginate=True)
    return data.to_csv()
 
if __name__ == "__main__":
    app.run(port=7777)
