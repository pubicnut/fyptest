from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run()
# Defining the home page of our site
@app.route("/")  # this sets the route to this page
def home():
	return "<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div id="tradingview_7cf13"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/NASDAQ-AAPL/" rel="noopener" target="_blank"><span class="blue-text">AAPL Chart</span></a> by TradingView</div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {
  "width": 980,
  "height": 610,
  "symbol": "NASDAQ:AAPL",
  "interval": "D",
  "timezone": "Etc/UTC",
  "theme": "light",
  "style": "1",
  "locale": "en",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": false,
  "allow_symbol_change": true,
  "container_id": "tradingview_7cf13"
}
  );
  </script>
</div>
<!-- TradingView Widget END -->"  # some basic inline html
