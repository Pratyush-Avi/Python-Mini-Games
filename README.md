# Python-Mini-Games
A simple playable game just for fun time 

This game is for everyone who has desire to learn Python. The game complexity increases with every level and we will be able to rise our knowledge throughout the game.

I have develop amazing games and I have done Python working by moving things on screen and objects interaction. I have also create and import pictures used in the games and get familiar with creating randomly movable enemies, animating the game characters and playing music and sounds while playing the game. This makes game more interesting while playing.

I have use Python and visual studio to create games with progressively increased difficulty. In this game I will be able to fully design operational game including creation of objects and positioning of custom pictures and other components on the gameplay.

This variety of games covers the following Python libraries and packages such as animating game objects as tkinter, implementing loops and classes, using Pygame package to simplify game development, animating game text using custom fonts, development of menu screens and buttons, taking input from the mouse/touch/keyboard, randomizing game events, resizing game objects.

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#Tic-Tac-Toe">Tic Tac Toe</a></li>
    <li><a href="#Guess-The-Number">Guess The Number</a></li>
    <li><a href="#Brick-Breaker">Brick Breaker</a></li>
    <li><a href="#Bunny-Hitman">Bunny Hitman</a></li>    
  </ol>
</details>

### Tic Tac Toe

Its very beginner-friendly game and it covers almost all the functions and collections of python. So, while implementing I came across TicTacToe game implementation in python.
The board is numbered like the keyboard’s number pad. And thus, a player can make their move in the game board by entering the number from the keyboard number pad alternatively.
I will be using dictionary which is an primitive data type in python which stores data in “key: value” format. and thus, I will create a dictionary of length 9 and each key will represent a block in the board and its corresponding value will represent the move made by a player. and than I will create a function printBoard() which I can use every time I want to print the updated board in the game.

![image](https://user-images.githubusercontent.com/75266216/121560458-25baab00-ca35-11eb-8a15-3c540ab09a50.png)


## Guess The Number

This is going to be a simple guessing game where the computer will generate a random number between 1 to 1000, and the user has to guess it in ultimate attempts. Based on the user’s guess computer will give various hints if the number is high or low. When the user guess matches the number computer will print the answer along with the number of attempts. To generate a random number I will use a Python module named random to use this module in our program, we just need to import it. I will be defining the controlling expression of the while loop and I have already assigned the number_of_guesses variable to 1. Within the loop, we are taking the input from the user and storing it in the guess variable. However, the user input I am getting from the user is a string object and to perform mathematical operations on it and than need to convert it to an integer which can be done by the Python’s inbuilt randint() method. This is just a beginner level game.

![image](https://user-images.githubusercontent.com/75266216/121563788-636d0300-ca38-11eb-8448-ecbcda6dd610.png)


## Brick Breaker

I will be using Tkinter Package which is an developing GUI(Graphical User Interface). Out of all the GUI methods, it is the most commonly used method. It is a standard python interface to the Tk GUI toolkit which is shipped with python. Python with tkinter gives the output is the fastest and easiest way to create GUI. I have used different function such as:
> The 'self' keyword is used for instance of the class. By using the ‘self ‘ keyword we can access all the attributes and methods of class python.

> Than there is 'def' keyword used as a function header of all the function which is used to define a function.

> There is also an ‘__init__’ which is a reserved method in python. It other words is called as constructor. When this method is called an object is created from the class and it allows the class to initialize the attributes of the class.

![image](https://user-images.githubusercontent.com/75266216/121652381-36146980-cab9-11eb-85f2-de8d8a057d93.png)

## Bunny Hitman

A simple game in python where the hero, the bunny, has to defend a castle against an attacking horde of badgers. In this game, we’ll create a simple game called Bunny Hitman Badgers, where the hero, the bunny, has to defend a castle against an attacking horde of badgers. Some of main function used while creating the game are:

> Import the PyGame library. This allows you to use functions from the library in your program.
> Initialize PyGame and set up the display window.
Load the image that you will use for the bunny.
Keep looping over the following indented code.


Fill the screen with black before you draw anything.
Add the bunny image that you loaded to the screen at x=100 and y=100.
Update the screen.
Check for any new events and if there is one, and it is a quit command, exit the program.

#### How to play?

1. Install [Python](http://www.python.org/download/). Make sure you grab the 2.7.x version and NOT the 3.3.x version!
2. Download the [PyGame](http://www.pygame.org/download.shtml) installer appropriate for your system. Make sure you download a Python 2.7 version.

To verify that you have configured your system correctly, open IDLE or run Python via the Terminal and type in "import pygame" at the python prompt. If this doesn't result in any output, then you're all set up and good to go. If, on the other hand, it outputs an error, then PyGame is not installed or not set up correctly. 

![image](https://user-images.githubusercontent.com/75266216/121849990-bcbf8580-cd09-11eb-91d2-9120b8f7fdb7.png)

