![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

# Black Jack 21 game

Black Jack is a card game played at casinos against a dealer. As it only requires a pack of cards it has also been popular family entertainment without the betting. This version includes betting. For a more complete history see [Wikipedia](https://en.wikipedia.org/wiki/Blackjack)

## flow chart

### initial flow chart 

To shuffle the cards used utube video :https://www.youtube.com/watch?v=0YkEy17Dz-M

validate number https://pynative.com/python-check-user-input-is-number-or-string/


https://pypi.org/project/simple-term-menu/
by using this menu most of the validation is done for me

https://www.simplilearn.com/tutorials/python-tutorial/sleep-in-python#:~:text=The%20sleep()%20function%20in,the%20given%20number%20of%20seconds. for sleep function.

https://www.w3schools.com/python/gloss_python_join_lists.asp for extend list to add two decks together

OS clear screen and colours adapted from madlibs

## bugs

Bet when input letter it would return the letter and the eventual number that got validated. needed to put bet as a global variable in the function rathr than try and define it outside using a return

dealer time infinite loop, forgot to add the new card to the dealer total so it always stayed below 17 if it started there.

## deployment

1. [Heroku](heroku.com) was used to deploy.
2. Once logged onto the website, using the drop down menu in the top right we went to the dashboard.
![dashboard](document/go-to-dashboard.png)
3. From here we are able to create a new app either by clicking on the icon (which is what we did)

![icon](document/create-new-app.png)

or the drop down menu

![dropdown](document/create-new-app-dropdown.png)

4. Next the app was named black-jack21 and the Europe region chosen in these feilds

![name](document/name-and-region.png)

and the purple 'create' button was pressed.

5. In the menu navigation bar the settings was selected

![settings](document/settings.png)

6. The section with Config Vars was then opened up by clicking the Reveal Config Vars button

![reveal](document/reveal.png)

7. The port was set to 8000

![port](document/port.png)

8. The build packs were then chosen, firstly the purple button add build packs was pressed, then the icon for python. The purple button for add build packs was pressed again and the icon for JSNode

![packs](document/build-packs.png)

![pythonJSNode](document/icons.png)

9. Now we used the menu navigation bar again, this time to select deploy

![nav](document/nav-bar.png)

10. The deployment method was selected by clicking on the GitHub icon and it stated that it was connected to github

![method](document/choose-git.png)

11. The repository was chosen by searching my github

![find](document/find.png)
![connect](document/connect.png)
![connected](document/connected.png)

12. Automatic deployment was chosen so that it would update every time the changes were pushed to git

![auto](document/auto.png)

13. It was deployed

![deployed](document/deployed.png)

## Credit

ASCII http://patorjk.com/software/taag/#p=display&h=2&v=2&f=Univers&t=BlackJack21 univers