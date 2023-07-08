




import telebot
import datetime
import requests
from bs4 import BeautifulSoup
from lxml import etree
import json

token = ""
bot = telebot.TeleBot(token)

weatherFXpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "CurrentConditions--tempHiLoValue--3T1DG", " " ))]//span[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]'
weatherConditionsXpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "CurrentConditions--phraseValue--mZC_p", " " ))]'
wordDayXpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "word-header-txt", " " ))]'
wordDeffinitionXpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "wod-definition-container", " " ))]//h2+//p'
quoteXpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "support-sentence", " " ))]'

links = ["https://weather.com/", "https://www.merriam-webster.com/word-of-the-day"]

def getQuote():
    global quoteAuthor
    global quote
    category = 'life'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    #API key from api ninja
    response = requests.get(api_url, headers={'X-Api-Key': ''})
    response.encoding = "utf-8"
    jsonData = json.loads(response.text)
    dict = jsonData[0]
    quote = dict["quote"]
    quoteAuthor = dict["author"]


def dateDif():
    global dif
    # date should be organised as Year-Month-Day
    Date = ""
    today = str(datetime.date.today())
    d1 = datetime.datetime.strptime(today, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(Date, "%Y-%m-%d")
    dif = d2 - d1

def sendMessage(message):
    token = ""
    bot = telebot.TeleBot(token)
    chatID = 

    bot.send_message(chatID, message)

def main(links):
    for links in links:
        global weather
        global wordOfTheDay
        global weatherConditions
        response = requests.get(links)
        soup = BeautifulSoup(response.content, "html.parser")
        body = soup.find("body")

        parse = etree.HTML(str(body))

        if links == "https://weather.com/":
            weather = parse.xpath(weatherFXpath)[0].text
            weatherConditions = parse.xpath(weatherConditionsXpath)[0].text
        else:
            wordOfTheDay = parse.xpath(wordDayXpath)[0].text


    name = 

    todaysDate = datetime.datetime.now()
    todaysDate = todaysDate.strftime("%a %b %d")

    getQuote()
    dateDif()

    message = f'Good morning {name} 👋. today is {todaysDate}. The weather for today is {weather} and {weatherConditions}. The word of the day is {wordOfTheDay}. {quoteAuthor} once said, "{quote}" There is {dif.days} days till graduation 🎓!'

    sendMessage(message=message)
    
    todaysDateLog = datetime.datetime.now()
    with open("pythonMorningMessagScriptLog.txt", 'a') as file1:
        file1.write(f"{todaysDateLog}]- {message}")
        file1.close()

main(links=links)
