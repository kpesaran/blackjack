# blackjack


## Overview

This project allows a user to play Blackjack on their command line interface. 

## Getting Started




### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation
1) Clone the repository

2) Navigate to the project directory
    cd blackjack

How to Play

Run the game by executing the following command in your terminal
    python main.py 

## Learning Objectives
Further explore and deepen my understanding of Object Oriented Programming (OOP) 


# Concepts used:

Inheritance:
Both Dealer and Player classes are subclasses that inherit from the Participant class. Player class includes methods to allow for betting. 

Encapsulation:
Each class manages its own data and behavior

Composition:
- The Game class is composed of Participants subclasses and a Deck instance.
- A Deck is composed of 52 instances of the Card class
- The subclasses, Player and Dealer, are composed of Bank and Hand classes. 

Abstraction 
- Complexity of handling hands, decks, and banks is hidden behind method calls. 


##Optimizations:

1) Enhanced Error Handling
2) Refactor game flow
3) Unit testing
4) Add UI

