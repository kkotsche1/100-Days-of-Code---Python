import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API_KEY = "NBCHPY486UJZLQNX"
NEWSAPI_API = "95e452b93b774c82a4876c94e1de44a1"

import requests
stock_moved = False

# ----------- Accessing Quote Information---------------- #

stock_quote_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY

}

stock_request = requests.get(url="https://www.alphavantage.co/query", params=stock_quote_params)
stock_data = stock_request.json()
stock_data = stock_data["Time Series (Daily)"]

# ---------------- Obtaining Yday and Tday Close ----------------- #

stock_data_list = list(stock_data)
todays_date = stock_data_list[0]
yesterdays_date = stock_data_list[1]

todays_close = float(stock_data[f"{todays_date}"]["4. close"])
yesterdays_close = float(stock_data[f"{yesterdays_date}"]["4. close"])

# ----------- Checking if Stock Price moved more than 5% --------- #

delta_stock_price = round(((todays_close-yesterdays_close)/yesterdays_close)*100, 2)


if delta_stock_price < -0.1 or delta_stock_price > 0.1:
    stock_moved = True
else:
    stock_moved = False


## STEP 2: Use https://newsapi.org - Accessing most popular Article from Today ##

def get_stock_news(delta_stock_price):
    import html

    news_request_params = {
        "apiKey" : NEWSAPI_API,
        "q" : COMPANY_NAME,
        "from" : todays_date,
        "sortBy" : "popularity",
        "pageSize" : 1
    }

    news_request = requests.get(url="https://newsapi.org/v2/everything", params=news_request_params)
    news_request = news_request.json()
    news_articles = news_request["articles"]
    news_article = news_articles[0]
    news_title = news_article["title"]
    news_description = html.unescape(f"{news_article['content']}")
    news_url = news_article["url"]

    ## STEP 3: Formatting Text Message

    if delta_stock_price > 0:
        text_headline = f"{STOCK}: 🔺{delta_stock_price}%"
    if delta_stock_price < 0:
        text_headline = f"{STOCK}: 🔻{delta_stock_price}%"

    text_body = f"""
    \n
    {text_headline}
    Headline: {news_title}
    Brief: {news_description}
    Link: {news_url}
    
    """

    return text_body

# ---------- Sending news via Twilio --------- #

def send_message(message):
    import os
    from twilio.rest import Client

    API_KEY_TWILIO = "29ab14e21da397b163590918e0d4da11"
    SID_TWILIO = "AC85b4dccb465482509b8b7dc2d653e166"

    client = Client(SID_TWILIO, API_KEY_TWILIO)

    message= client.messages.create(
        to="+4915123916438",
        from_="+19127158761",
        body= f"{message}"

    )
    print(message.status)


if stock_moved:
    message = get_stock_news(delta_stock_price)
    send_message(message)