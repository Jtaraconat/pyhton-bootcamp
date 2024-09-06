import requests
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_SID = "twilio_sid"

STOCK_API_KEY = "api_key"
NEWS_API_KEY = "api_key"
TWILIO_API_KEY = "api_key"

STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval":"60min",
    "apikey": STOCK_API_KEY
}
NEWS_PARAMS = {
    "apiKey" : NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,

}

formatted_articles = []

def send_sms():
    client = Client(TWILIO_SID, TWILIO_API_KEY)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from="twilio_phone_number",
            to="phone_number"
            )
    for article in formatted_articles:
        print(article)

def get_news():
    global formatted_articles
    response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMS)
    articles = response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"Headline: {article["title"]}. \nBrief: {article["description"]}" for article in three_articles]
    send_sms()


def stock_price():
    response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMS)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]
    yesterday_data = data_list[0]
    yesterday_closing_price = yesterday_data["4. close"]

    day_before_yesterday_data = data_list[1]
    day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

    difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
    different_percent = (difference / float(yesterday_closing_price)) * 100

    if different_percent > 5:
        get_news()
        

stock_price()

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 





## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

