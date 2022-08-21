# Sentiment Analysis in Google Sheet Using Python

## Objective 
To create a custom function in Google Sheet so that we can get the sentiment of feedbacks that we receive via Google Forms
and utilize that to create visualization in the spreadsheet.

## Tools used
- Google spreadsheets
- Python
  - FastAPI package
  - NLTK Package
  - Pycharm IDE
- AppScript (Basic)
- Version control - Git using GitHub
- Deployment using Heroku

## Design Architecture
The tool will include 2 services
1. Google spreadsheets
   - We will build a custom function using Google's AppScript which will let us send http requests to an API, to which we will send our input(s), in response we shall get the required output directly in spreadsheet cell.
2. An API
   - With the help of FastAPI we will build and API that will essential ease up the calculation (as it will have the capacity to utilize Python's package) and let the end user use this directly in spreadsheet without ever worrying about learner how to create complex code.

## Learnings from this exercise
- Create Sentiment Analysis Model using NLTK
- Overcome some common challenges while using NLTK package
- Creating API and redirections
- Version Control using Git
- Deployment of web-app
- Creating custom google sheet function

## References
1. [How to download nltk packages in heruko deployement](https://devcenter.heroku.com/articles/python-nltk).
2. https://docs.google.com/forms/d/e/1FAIpQLSd6iqviDaIMt1X6CW4jPZ6OKlMytxmJxh6ZBVZ0VRW_lJypdA/viewform?fbzx=-2130729464828145438
3. https://docs.google.com/spreadsheets/d/1uY9R7kzvtecmAkrJLsXZ0es000J00OCMi5a_SWic9p4/edit?resourcekey#gid=846568907

## Walkthrough
[![Sentiment Analysis in Google Sheets Using Python](https://yt-embed.herokuapp.com/embed?v=Z2h6v5-vlwE)](https://youtu.be/Z2h6v5-vlwE "Sentiment Analysis in Google Sheets Using Python")
