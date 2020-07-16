# Roadmap

![Code Architecture](https://raw.githubusercontent.com/nickkeesG/market_game/master/images/market_game_skeleton.png?token=AJPNG4NOZH3AIQ6N6D5LL7C7CC5YQ)

## main.py
Calls simulator to obtain individual data points, and then analyses that data. 

## simulator.py
Runs a full simulation where a game is set up, and a NE is obtained by means of best response dynamics.

## set_up.py
Sets up an instance of the class Game, which will contain everything pertaining to the details of the game, as well as any functions needed later.

## parameters.py
Contains any variable parameters pertaining to the setup of the Game object. Some of these parameters may later be passed down from main.py if necessary.

## game.py
Code for the class Game. A Game object is composed of agents, as well high level functions for those agents.

##agent.py
Code for the class Agent. Includes the beliefs of the agents, as well as code pertaining to their behavior.

## iterated_best_response.py
Takes a Game object and iteratively allows agents to change their strategies to improve their expected utility, and does so until either convergence or some failure condition is met.

## custom_math.py
Any calculations that are used multiple times or would cause clutter in the code.
