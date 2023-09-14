# Black Jack 21 game

BlackJack21 is a python terminal game, which is run on the Code Institute mock terminal on Heroku. 

It is a betting game that is played against a dealer which in this case is the computer. It is played with playing cards and the aim is to get as close to 21 as possible without exceeding it. You win if you get 21 or beat the value of the dealers cards without exceeding 21.

[Here is the live version of the project](https://black-jack21-fa4b7e8cb0bf.herokuapp.com/)

Black Jack is a card game played at casinos against a dealer. As it only requires a pack of cards it has also been popular family entertainment with or without the betting. This version includes betting. For a more complete history see [Wikipedia](https://en.wikipedia.org/wiki/Blackjack)

## Flow chart

### Initial flow chart 

I proposed the initial design of the game using a flow-chart and document that I put together with my thoughts.

![flowchart](document/flowchart.png)

[idea document page 1](document/design-thoughts-1.png)

[idea document page 2](document/design-thoughts-2.png)

## How to play

1. Initially you enter your name so the experience can be personalised
2. Then you place a bet without knowing the cards by typing a whole number that is less than or equal to your credit.
3. The cards will then be dealt. Two each for you and the dealer, one of the dealers cards will be held in the hole until his turn (So you can't see his second card).
4. You can Hit (get one more card then decide again), Stick (stay where you are and it is the dealers turn) or Double down (which doubles the bet and gives you only one more card - before the dealers turn).
5. Your cards are worth their face value if they are a number card. Jack, Queen and King are worth 10 and Ace can be worth 1 or 11 depending on what is best for the hand.
6. If you exceed 21 then you will lose your bet. If you get 21 there is an instant payout.
7. If you don't exceed 21 and have stuck or doubled down then the dealers(computers) turn commences. You will get to see the dealers cards and if he gets additional cards you will see those dealt.
8. If the dealer gets higher than you without exceeding 21 he wins, if he exceeds 21 you get your money back and if you have the higher value you win. 
9. If you win the winnings will be paid into your credit.
10. 21 gets a higher return than just beating the dealer.

## Features

### Existing Features

- List comprehension was used to create the deck of cards and then it was held in a constant. This works with a nested for in for loop. One for loop works through the suits and one works through the values, each time outputting a dictionary entry for the suit and value/name.

- These cards are shuffled using To shuffle the cards used utube video :https://www.youtube.com/watch?v=0YkEy17Dz-M

- Betting was done via an input, which was then validated to ensure that it was an integer not a special character, letter etc. It was also necessary to ensure that it was a positive number and there was sufficient credit in the game to allow the bet to be made.

- the number was validated by validate number https://pynative.com/python-check-user-input-is-number-or-string/ also put the code in here.

- the next user input that was required was a menu to decide whether to hit, stick, double down or quit. This was done from information gathered from https://pypi.org/project/simple-term-menu/
This third party module provides all the required validation which makes the code more efficient.

- It was important for the game to have appropriate timing. So that everything was on the screen for long enough for the player to read or build suspense when the cards are being dealt. This was performed from the sleep function from the built in library of time.

[time](https://www.simplilearn.com/tutorials/python-tutorial/sleep-in-python#:~:text=The%20sleep()%20function%20in,the%20given%20number%20of%20seconds) 

https://www.geeksforgeeks.org/make-python-wait-for-a-pressed-key/ press enter to continue on the instructions

- also for readability it was essential to remove extraneous information from the screen once it was no longer required. OS clear screen adapted from [clear](https://www.geeksforgeeks.org/clear-screen-python/)

- Readability also was improved by the use of colours from [colorama](https://pypi.org/project/colorama/).

validate number and name contains https://www.askpython.com/python/string/python-string-contains

- Simplistic reading of the cards was aided by the use of emojis. The initial idea to use the cards emojis was quickly disregarded when it became apparent that they were unreadable due to size on the terminal output so a crown and the emojis for the suits were used instead. This was taken from [emoji](https://pypi.org/project/emoji/). It was attempted to also do the Jack, King and Queen with their own emoji's but the available emoji's didn't make that clear. So it was decided just to have a crown to show that they were court cards.

It is possible that if the player wins or breaks even and continues through several rounds that the deck of cards will run out. Therefore, when this occurs an additional deck of cards is shuffled and added to the end of the pack. This was done using [W3](https://www.w3schools.com/python/gloss_python_join_lists.asp) to extend list to add two decks together
 
https://www.scaler.com/topics/exit-in-python/ - quit function

### Potential Future features

- It would be possible to add several players to the game by asking how many players there were, up to a set number, then setting up those players hands separately, with a reference to the name that they gave initially.

Then when the first player had gone bust or stuck it could ask the players to hand the game over to the next named player and use a menu to confirm when they had.

This would be more similar to a casino version of the game when usually several people sit around a table with one dealer and the dealer only goes once everyone has finished their turn.

- Split is also something that could be added to the game where if the player has two identical value cards they are allowed to make the cards the first card in two hands and place their original bet against both hands. This was in the original idea for the game, but it was decided to leave till last or not to be completed as it was a nice to have rather than a requirement to meet the project assessment criteria.

## Bugs

### Ace 1 or 11

Developing a function that would allow me to either produce a value of 1 or 11 when the Ace was dealt was quite challenging.

Initial strategy was to add everything up and they try both the 1 and the 11. However, this proved to be extremely complicated and required excessive code. So being as I had not successfully completed this code when the calculations showed me that there were specific number limits each time I stopped this approach.

Using a combination of the specific total values prior to adding the Aces and the number of aces being added (which can only be 0 to 4) gave a significant simplification of the code. It also aligns with Dealers always stopping at 17 as that is the point where the probability of winning changes. So this made sense.

The final simplification involved using just a couple of lines of code with addition in the line of code, rather than many lines of for and if, when the value was only changing by one.

### Not using equal to or greater than just greater than
I had two examples where the greater than logic was not what was intended. In both cases I had intended equal to or greater than and only used greater than.

1. When checking that the player had sufficient credit to be able to place a bet I put > 1, but obviously there is not reason why a bet of 1 could not be placed. The logic should either be > 0 or >=1. This was discovered when a player tried to bet 1.
2. During the development of the Ace function I used greater than for my limit numbers when they should have been >= which meant that for Black Jack (21) my calculation was giving the Ace a value of 1 when it should be 11 to equal 21.

### Initial input held instead of latest input

Due to the ordering of the actions in my code the input of a bet took a value and then validated it. If the value failed validation then it asked for another value. During various attempts at the code it either held the initial input (which was the first bug to deal with) and ignored later inputs or as I moved through improving the code either the calculations or the values given to the player on screen were from the wrong iteration. This was eventually worked through by working step by step thorough the code with each error till I found where it was in the wrong order. Eventually, although not best practise it was decided to put Bet as a global variable so that all the other functions were working from the same source, rather than returning the value. Potentially with additional work this could be sorted out in to a return again, but currently as it is working and there were more important errors it was left to be improved if time later.

### Infinite loop

The dealer time was stuck in an infinite loop while the function was being developed as the part of the function that dealt an extra card hadn't been put in so it kept checking if the value exceeded 17 and as no action had occurred to change the value (no new cards to add in) it went round the loop. This took a few times to realise as sometimes the initial draw was above 17 so it was an intermittent fault.

Due to an issue with code institute credits on codeanywhere not being set to infinite before this project, there is a slight gap when I couldn't commit to Git. During this time I just worked on the README, to reduce loss of traceability.



## Testing

check|intended outcome|comment|pass y/n
---|---|---|----
User name only accepts letters|specific error for anything that isn't automatically corrected| | |
Bet input only accepts positive numbers|specific error for anything that isn't a positive number within credit|Tried letters special characters and 0 and negative numbers and blank space| |
Game runs in correct order of functions |Plays as expected| | |
Adding up of card values gives correct person winning|User or Dealer wins or loses correctly against cards| | |
Credit system has correct amount added and subtracted| credit relates to bets won and lost| | |
No issues with moving to second deck|next deck cards play without interruption||
Menus give correct action|correct function called from choice| | |
Play another round works|next round has cleared hands and bet to work as an independent round while credit retained| | |
Ends as expected when requested|says goodbye and tell you credit| | |
When you run out of credit it ends the game|says goodbye but doesn't tell you your credit just that you ran out| | |


## Validator

[PEP8Online.com](https://pep8ci.herokuapp.com/) was used to validate this project. No errors was found in the final deployed version.

## Technology used

### Language

- [python 3.11.5](https://docs.python.org/3/)

### Other technologies

- [codeanywhere](https://codeanywhere.com/beta) was used to write the code
- [pythontutor](https://pythontutor.com/visualize.html#mode=edit) to allow me to work through my code in small sections
- [Heroku](heroku.com) was used to deploy.
- [Github](https://docs.github.com/en) used for version control.
- code institute mock terminal

### Third part libraries

- [colorama 0.4.6](https://pypi.org/project/colorama/) was used to highlight signficant text so that it would be more readable.
- [emoji 2.8.0](https://pypi.org/project/emoji/) was used to introduce images that made the information more easily interpreted by the user.
- [numpy 1.24.4](https://numpy.org/doc/stable/reference/) allows the sequencing of arrays.
- [simple-term-menu 1.6.1](https://pypi.org/project/simple-term-menu/) gave a simple menu that could be adapted to allow for relevant menus


## Deployment

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

- Code institute for the knowledge base that I developed from their course material and the deployment terminal.

- The ASCII larger writing was taken from [patorjk.com](http://patorjk.com/software/taag/#p=display&h=2&v=2&f=Univers&t=BlackJack21) and cut and paste into print f string statements using the style Calvin S.

- My grandparents for amazing patience teaching me the game when I was learning to add up.

- Pat Walmsley and Ian Harris - My mother and partner for their patience.

- My Mentor - Juliia Konn has been enthusiastic and provided encouragement and spotted details that I was only vaguely aware of and taught me to look for them.

- [Wikipedia](https://en.wikipedia.org/wiki/Blackjack) for reminding me to the details of the game.

- [pythontutor](https://pythontutor.com/visualize.html#mode=edit) for working through my code.

- [Heroku](heroku.com) for deployment.

- [Github](https://docs.github.com/en) for version control
- [colorama 0.4.6](https://pypi.org/project/colorama/) for coloured text.
- [emoji 2.8.0](https://pypi.org/project/emoji/) for emoji's.
- [numpy 1.24.4](https://numpy.org/doc/stable/reference/) to work with arrays.
- [simple-term-menu 1.6.1](https://pypi.org/project/simple-term-menu/) for menus.

