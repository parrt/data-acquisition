# Building web servers

## Goal

The goal of this homework is to build a dynamic website using [Flask](http://flask.pocoo.org/) that displays stock history in an HTML table.  Given "file" `/history/stockname`, your server will pull stock history for `stockname` from Yahoo finance as you did in a previous lab and display it in table form. You will learn both GET and POST HTTP "methods".

Here is what your webpage looks like for `/history/AAPL`:

<img src=figures/pythonanywhere.png width=400>

Your server is like a proxy for Yahoo finance.

## Description

###  A basic stock history table

First, get the `readcsv` function from your previous pipeline project into your new file `server.py`:

```python
def readcsv(data):
    """
    Read CSV with header from data string and return a header list
    containing a list of names and also return the list of lists
    containing the data.
    """
    ... same code from a previous project ...
```

You also need a function that uses `urllib2` or [requests](http://docs.python-requests.org/en/master) package to fetch stock history from Yahoo finance:

```python
def gethistory(ticker):
    """
    Return header list, data (list of lists) for ticker,
    obtained from Yahoo finance.
    """
    ...
```

Using your previous functionality, create a function that returns HTML based upon a list of header names and a list of rows of data read from Yahoo finance:

```python
def htmltable(headers, data):
    """Return an HTML table representing the headers and data."""
    ...
```

Your main program for the `server.py` script looks like the following.
 
```python
app = Flask(__name__)

@app.route(...) <-- fill this in too
def history(ticker):
    """
    In response to url /history/ticker, get data from Yahoo finance on
    ticker and return an HTML table representing that data.
    """
    ...
    
app.run() # kickstart your flask server
```

Run your server then verify that when you go to URL `http://localhost:5000/history/AAPL` in your browser you get AAPL's history.

### POST and forms

Now, add a new method and `route` for a landing page that answers to URL `/`. For the local host, that would look like: `http://localhost:5000/`. That method should serve a static file using `send_static_file()`. Please call that file `index.html`, which must be stored in a directory called `static` underneath your project directory.

Create an html `form` in `index.html` so that it looks like this:

<img src=figures/stock-form.png width=350>

The target of the form submission should be URL `/history` and **use POST not GET**. Then create a method and route to handle that URL:

```python
@app.route(...) <-- fill this in
def post_history():
    ...
```

In response to a POST, the method should pull out the `ticker` form value and do the same functionality as your previous `history` function. You can search for [How to obtain values of request variables using Python and Flask](https://www.google.com/#q=How+to+obtain+values+of+request+variables+using+Python+and+Flask), to get some help.

You can test POST from the commandline with `curl` and `--data` option:

```bash
$ curl --data "ticker=TSLA" http://localhost:5000/history
    <html>
    <body>
    <table>
    <tr><th>Date</th><th>Open</th><th>High</th><th>Low</th><th>Close</th><th>Volume</th><th>Adj Close</th></tr>
<tr><td>2016-08-25</td><td>223.110001</td><td>223.800003</td><td>220.770004</td><td>220.960007</td><td>1756800</td><td>220.960007</td></tr>
<tr><td>2016-08-24</td><td>227.050003</td><td>227.149994</td><td>222.220001</td><td>222.619995</td><td>2564100</td><td>222.619995</td></tr>
...
```

That does a POST not get to that URL.

### JSON output

Let's also generate some JSON, not just an HTML table.

Add methods and routes as necessary so that URL `/data/`*ticker* such as `/data/TSLA` returns JSON output for the indicated stock ticker. It should look something like this in your browser:

<img src=figures/tsla-json.png width=200>

```bash
$ curl http://localhost/data/TSLA
{  "headers":["Date", "Open", "High", "Low", "Close", "Volume", "Adj Close"],
"data":[ ...
```