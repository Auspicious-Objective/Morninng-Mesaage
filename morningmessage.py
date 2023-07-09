import telebot
import datetime
import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
from threading import Thread

name = ""
token = ""
weatherLink = "https://weather.com/"
#Date should be organized as Year-Month-Day
Date = ""
event = ""
APIKey = ""
chatID = 

bot = telebot.TeleBot(token)

#xml paths
weatherFXpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "CurrentConditions--tempHiLoValue--3T1DG", " " ))]//span[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]'
weatherConditionsXpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "CurrentConditions--phraseValue--mZC_p", " " ))]'
wordDayXpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "word-header-txt", " " ))]'

links = [weatherLink, "https://www.merriam-webster.com/word-of-the-day"]

def getQuote():
    global quoteAuthor
    global quote
    category = 'life'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={"X-Api-Key": APIKey})
    response.encoding = "utf-8"
    jsonData = json.loads(response.text)
    dict = jsonData[0]
    quote = dict["quote"]
    quoteAuthor = dict["author"]


def dateDif():
    global dif
    today = str(datetime.date.today())
    d1 = datetime.datetime.strptime(today, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(Date, "%Y-%m-%d")
    dif = d2 - d1

def sendMessage(message):
    bot.send_message(chatID, message)

def getTodaysDate():
    global todaysDate
    todaysDate = datetime.datetime.now()
    todaysDate = todaysDate.strftime("%a %b %d")

def log():
    todaysDateLog = datetime.datetime.now()
    with open("MorningMessageLog.txt", 'a') as file1:
        file1.write(f"{todaysDateLog}]- Program has been ran successfully")
        file1.close()

def main(links):
    for links in links:
        global weather
        global wordOfTheDay
        global weatherConditions
        response = requests.get(links)
        soup = BeautifulSoup(response.content, "html.parser")
        body = soup.find("body")

        parse = etree.HTML(str(body))

        if links == weatherLink:
            weather = parse.xpath(weatherFXpath)[0].text
            weatherConditions = parse.xpath(weatherConditionsXpath)[0].text
        else:
            wordOfTheDay = parse.xpath(wordDayXpath)[0].text

    quoteThread = Thread(target=getQuote)
    quoteThread.start()

    todaysDateThread = Thread(target=getTodaysDate)
    todaysDateThread.start()

    dateDifThread = Thread(target=dateDif)
    dateDifThread.start()

    quoteThread.join()
    todaysDateThread.join()
    dateDifThread.join()

    message = f'Good morning {name} 👋. today is {todaysDate}. The weather for today is {weather} and {weatherConditions}. The word of the day is {wordOfTheDay}. {quoteAuthor} once said, "{quote}" There is {dif.days} days till {event}!'

    logThread = Thread(target=log)
    logThread.start()

    sendMessageThread = Thread(target=sendMessage(message))
    sendMessageThread.start()

main(links=links)
