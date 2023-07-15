# AutomaticSurveyFiller2.0

## About this Bot
This bot was made to automatically fill the Tim Horton's survey. This will allow you to save a lot of time and let the survey be filled for you!

## Usage
Start by Installing the libraries mouse and keyboards.
        Pip Install mouse
        Pip install keyboard
Once they are installed, you can run the the SurveyBot.py file
Keep in mind, this bot is using coordinates for a 15' screen. if your screen is smaller or bigger, you must run main.py first to find all the coordinates for the butons and instert them in the SurveyBot.py before running the file.

In order to get the button coordinates for your own screen size, run the follwoing command in the terminal:
        python3 main.py
This will will run the script that gives the position of your mouse pointer every four seconds. 
With this, go through the survey and get all the coordinates you need for your bot. 
Once you have all the coordiantes, in the terminal do: ctrl + c to stop the script.

Next modify the the SurveyBot.py file with your own coordinates and then run that file in the terminal:
        python3 SurveyBot.py

Now just watch the bot do its job!

## How it works?
Everywhere your mouse goes on the screen, it has a coordinate. This coordinate can be used to do various tasks.
I am utilizing these coordiantes to press specific butons on the screen to fill a survey for me. 
