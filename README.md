<h1>Group 25-Assignment 2</h1>
<h1>Project name: AutoBot</h1>

<h2>About the project</h2>
Our project is called Autobot and is essentially an AI that assists a user in picking a vehicle. This is done by asking the user a series of questions which helps Autobot predict what the user will prefer. Autobot is mainly for users who may have limited knowledge of what type of vehicle they are interested in.

<h2>Navagation for software</h2>
We organized all code in one class (VehicleList) for simplicity and ease of access. VehicleList initiates a database and adds all vehicles available. 
<h2>Code organization</h2>
In VehicleList.py the codes are organized into 4 parts sepearted by comments.
1. Database of cars
2. Text input for text matching check
3. FUnction for text finding 
4. methods for compiling

<h2>Code Update Documentation</h2>
3 points: README file in your repository describing what you've done. If you've cloned your A2, you are likely to just add onto the README in this case. If you've changed a lot since A2, you will have to rewrite the README so it reflects your current submission.

1. I added two parts to this project. I added the Stanford core NLP for sentiment analysis. I also added a spell checker to correct words. I did not add anything else at this moment.

5 points: At the end of your README file, include: a list of each feature you programmed for this assignment
for each item on that list, explain briefly how you used that feature to improve your agent's conversation or your overall system
for each explanation, give a snippet of a conversation that demonstrates your feature

1. I added a spell checker.

I used the spell check to correct spelling mistakes a user will encounter. These spelling mistakes are corrected and the corrected word is shown to the user so they are aware of the change. This improved the bots ability to understand users that make common mistakes which allows for the program to run more seamlessly.

This is a code snippet:
            ...
            -Price 
            -Type of vehicle
            -Brand
            brnad
            Auto Correcting brnad to brand ...
            What brand are you after?
            Brand:
  
2. I added a sentiment analysis tool.

The sentiment analysis tool helps by taking the users input after the bot asks "How they day is" and proceeds to give a reasonable response to how that user feels. This creates a more streamline response which is not hardcoded. The bot can judge how the user is experiencing their day when it asks and then proceeds to response accordingly.

This is a code snippet:
            ...
            Pleasure to meet you Tayler Verhaegen
            How is your day going?
            bad
            . 
            . 
            Aw, well I'm sure a car will cheer you up!
            What are some important aspects you want in 
            your vehicle?
