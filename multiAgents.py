# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"     
        

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"


        def maxValue(ghosts,gameState, depth):

          #an game over tote xrhsimopoiw th self.evaluationfunction
          if  depth>self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)
        
         #initializing
          play = float("-inf")

          #kalw thn minValue sunarthsh gia otan paizoun ta ghosts h opoia me th seira ths kalei pali th maxValue gia to Pacman
          #h diadikasia auth sunexizetai mexri na oloklhrw8ei to anadromiko dentro
          for action in gameState.getLegalActions():
            play = max(play, minValue(ghosts,gameState.generateSuccessor(0, action), depth, 1));
            
          return play


        
        def minValue(ghosts,gameState, depth,agentIndex):

          #paromoia
          if gameState.isWin() or gameState.isLose() or depth > self.depth:
            return self.evaluationFunction(gameState)

          play = float("inf")

          #an teleiwsan tis kinhseis tous ta ghosts
          if agentIndex == ghosts:
              
            #tote spaw th loopa kai kalw thn maxvalue me depth+1 
            for action in gameState.getLegalActions(agentIndex):
              play = min(play, maxValue(ghosts,gameState.generateSuccessor(agentIndex, action), depth + 1))
              
          else:
              
            #alliws xrhsimopoiw th minvalue gia to ka8e ghost
            for action in gameState.getLegalActions(agentIndex):
              play = min(play, minValue(ghosts,gameState.generateSuccessor(agentIndex, action), depth, agentIndex + 1))
              
          return play




        ghosts = gameState.getNumAgents() - 1               #afairw ton Pacman agent
        
        next_score = float("-inf")
        stop = Directions.STOP

        #edw koitazei to pacman to state tou sthn epomenh kinhsh tou kai an exei xeirotero apo auto pou hdh exei tote stamataei
        for action in gameState.getLegalActions():
            
          play = max(next_score, minValue(ghosts,gameState.generateSuccessor(0, action), 1, 1))
          if play > next_score:
              
            next_score = play
            stop = action
            
        return stop

    
        #util.raiseNotDefined()



    

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        
        #h basikh ulopoihsh tou alphabeta einai paromoia me tou minimax
        def maxValue(ghosts,gameState, depth,a, b):
            
          if  depth>self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)
        
          play = float("-inf")
          
          for action in gameState.getLegalActions():
            #ulopoiw algori8mo alpha beta
              
            play = max(play, minValue(ghosts,gameState.generateSuccessor(0, action), depth, 1,a, b));
            a = max(a, play)
            
            if play > b:
              return play
            
          return play



        
        def minValue(ghosts,gameState, depth, agentIndex,a,b):
            
          if gameState.isWin() or gameState.isLose() or depth > self.depth:
            return self.evaluationFunction(gameState)
        
          play = float("inf")
          
          if agentIndex == ghosts:
              
            for action in gameState.getLegalActions(agentIndex):
                
              play = min(play, maxValue(ghosts,gameState.generateSuccessor(agentIndex, action), depth + 1,a,b))
              b = min(b, play)

              
              if play < a:
                return play
            
          else:
              
            for action in gameState.getLegalActions(agentIndex):
                
              play = min(play, minValue(ghosts,gameState.generateSuccessor(agentIndex, action), depth,agentIndex + 1,a,b))
              b = min(b, play)
              
              if play < a:
                return play
            
          return play

        a = float("-inf")
        b = float("inf")
        next_score = float("-inf")
        
        ghosts = gameState.getNumAgents() - 1
        stop = Directions.STOP
 

        for action in gameState.getLegalActions():
            
          play = max(next_score, minValue(ghosts,gameState.generateSuccessor(0, action), 1, 1,a, b))
          
          if play > next_score:
              
            next_score = play
            stop = action
          a = max(a, play)
          
        return stop

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"

       #util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

