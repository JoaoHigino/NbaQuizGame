# NBA Quiz Game

NBA Quiz Game refers to a short test of knowledge, with 20 questions in length with multiple choice. This Quiz has no commercial intention.

[Link to my code via Github repository](https://github.com/JoaoHigino/NbaQuizGame)

[Link to my Application deployed by Heroku](https://nbaquizgame.herokuapp.com)

![diferent views](documents/iamresponsive.png)

## How To Play

First, you will need to enter your name to start the game. 

Then the quiz will start, it is a multiple choice game (A,B,C,D).

There are 20 questions and you get 5% for right answers and 0 for wrong. If you answer all the 20 questions correctely you get 100%.

The restart button is always available to reset the game and start over.

At the end of each game, you will be asked if you want to play again.


## Features

### Existing Features

- Restart Game Button

  - This button allows the player to reset the game.

 ![restart button](documents/restart.png)

- Username

 ![Username](documents/username.png)

- Quiz

  - The beginning menu will introduce you to the game and ask you to write your username.

![main](documents/main.png)

  - When the game starts a question will appear and the player needs to choose an option between A, B, C, D.

![question](documents/question.png)

  - All 20 questions are different with different options to choose from.

![question2](documents/question2.png)

  - When the player answers correctly a CORRECT! will show on the top of the screen.

![correct answer](documents/correct.png)

  - When the player answers incorrectly a WRONG! will show on the top of the screen.

![wrong answer](documents/wrong.png)

  - When the player tries to answer a different option outside the valid ones(A, B, C, D) an error message will show up and asks the player to try again.

![invalid answer](documents/wronganswer.png)


![invalid answer](documents/error.png)


![invalid answer](documents/error2.png)


  - When the game concludes the results are presented with all the player answers and the correct answers, which will give a score out of 20 and a total %.

![final](documents/final.png)

  - After the final result a message asks if the player wants to play again, if the answer is "yes" the game will restart and if the answer is "no" a BYE message shows and the program ends. If the answer is anything besides "yes" or "no" an error message will show up and asks the player to try again.

![play again](documents/playagain.png)


![play again](documents/error3.png)


## Features Left to Implement

- Create a scoreborad to compile all time results. 

## Technologies Used

- [Python3](https://www.python.org/)
- [Heroku](https://heroku.com) - was used to deploy the application.
- [Gitpod](https://www.gitpod.io) - was used to create the website
- [Github](https://github.com) - was used to store repository of website and deploy the website
- [Create Ascii](https://www.devdungeon.com/content/create-ascii-art-text-banners-python#use_pyfiglet_python) - was used to art text banners
- [NBA Wallpaper](https://wallpaperaccess.com/nba-laptop) - provided the wallpaper image
- [Grammarly](https://app.grammarly.com) - was used to check typography.
- [Am I Responsive](https://ui.dev/amiresponsive?url=https://nbaquizgame.herokuapp.com/) - was used to produce the website mockup.
- [Whitenoise](https://pypi.org/project/whitenoise) - Used to static files on Heroku


## Testing

### Browser testing

 - Chrome

 ![chrome checker](documents/chrome.png)

 - Opera

 ![opera checker](documents/opera.png)

 - Edge

 ![edge checker](documents/edge.png)

 - Safari

 ![safari checker](documents/safari.png)




### Validator Testing 

  - Built into Code Institute template. Add-ons allow for error checking.
  - Pep8 website down for testing.

![problems](documents/terminal.png)  


### Unfixed Bugs

  - I am aware when you press control+c the game stops, it was a helpfull feature used during testing.

![bug](documents/controlerror.png)


## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser. This is to improve the accessibility of the project to others.

The live deployed application can be found at [nbaquizgame](https://nbaquizgame.herokuapp.com/).

### Local Deployment

*Gitpod* IDE was used to write the code for this project.

To make a local copy of this repository, you can clone the project by typing the follow into your IDE terminal:
- `git clone https://github.com/JoaoHigino/NbaQuizGame.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JoaoHigino/NbaQuizGame)

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select *Create App*.
- From the new app *Settings*, click *Reveal Config Vars*, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- Further down, to support dependencies, select *Add Buildpack*.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`. If you have your own packages that have been installed, then the requirements file needs updated using: `pip3 freeze --local > requirements.txt`

The Procfile can be created with the following command: `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <app_name>` (replace app_name with your app, without the angle-brackets)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type: `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku.

## Credits

### Media

 - [Background Image](https://wallpaperaccess.com/full/103106.jpg)

### Sources

- [Interactive Quiz Game](https://www.makeuseof.com/python-make-interactive-quiz-game/)

- [Hangman](https://github.com/Kaylaesmith1/python-hangman/blob/main/views/layout.html)

- [Python Tutorial - Multiple Choice Quiz](https://www.youtube.com/watch?v=myJ36xIR7Yg)

- [How to Generate Multiple Choice Questions with Python](https://pythonprogramming.altervista.org/how-to-generate-multiple-choice-questions-with-python/?doing_wp_cron=1665429912.8629679679870605468750)

- [Football Quiz](https://github.com/mikyrenato/3rd_Project_Quiz_Game)

- [Most Embarassing NBA Records](https://basketballforever.com/2020/06/12/the-most-embarrassing-nba-records-of-all-time-2)

- [Most Umbreakable Records NBA History](https://www.nbcsports.com/chicago/bulls/10-most-unbreakable-records-nba-history)

- [NBA Stats](https://www.nba.com/stats)

- [Basketball Reference](https://www.basketball-reference.com/)


### Acknowledgements

- To my amazing wife Sandra, my best friend, my mentor, and my safe haven, without her, all my dreams will be impossible to achieve. She is everything.
- To my two kids, Maria and Thomas, with them life is easy and light. They make me laugh and think that our future is bright. 
- To my family and friends - for being a great support and providing a lot of the user testing for me, especially my friends from "Liga 7 BP" with their craziness helped me to clean my head.
- To my mentor Tim Nelson for all his guidance, support, tips, and feedback.
- The Code Institute community on slack and my classmates its been a pleasure so far.