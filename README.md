
# Morninng-Mesaage
A script that makes a morning message with the bare bones details you need in the morning.

## Setup
you will need to do some work in order to get the program up and running.

### Packages
- beutiful soup 4 to compile parts of the webpages
- lxml for understanding the xml

### Code that will need to be edited

All lines that will be needed to change are located at the top of the file bellow the imported packages. You will edit the following lines:

- Name: the name that will be in the message
- Token: your telagram bot token
- Date: the date of your event. **You will need to format the date as: Year-Month-Day all in numerical forum**
- Event: name of your event example- wedding, graduation
- Weather link: go to weather.com and get the link that cordinates to your city.
- API key: get an API key from https://api-ninjas.com/
- Chat ID: this code can be found in a couple of ways i suggest using this guide https://www.alphr.com/find-chat-id-telegram/
### Server setup
I recomend using cron to automate when the message gets sent. For making the format for cron you can use https://crontab-generator.org/ to make it simpler.

## Conclusion
Thank you so much for spending your time here. I would love to hear any feedback. If you have any questions feel free to ask.

