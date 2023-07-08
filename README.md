# Morninng-Mesaage
A script that makes a morning message with the bare bones details you need in the morning.

## Setup
you will need to do some work in order to get the program up and running.
### Packages
- beutiful soup 4 to compile parts of the webpages
- lxml for understanding the xml

### Code that will need to be edited
- Token: lines 13 & 48, will need your telagram bot token
- Weather link: line 22 & 65, go to weather.com and get the link that cordinates to your city.
- API key: line 30, get an API key from https://api-ninjas.com/
- Date: line 41, the date of your graduation or other event(you can just edit the message veriable to change the event name)
- Chat ID: line 50, this code can be found in a couple of ways i suggest using this guide https://www.alphr.com/find-chat-id-telegram/
- Name: line 71 the name that will be in the message

### Server setup
I recomend using cron to automate when the message gets sent. For making the format for cron you can use https://crontab-generator.org/ to make it simpler.

## Conclusion
Thank you so much for spending your time here. I would love to hear any feedback. If you have any questions feel free to ask.
