# Harvard Artigivial Intelligence cousr 

https://www.youtube.com/watch?v=5NgNicANyqM 


### Search 

Google maps have search algorithms 
- to find correct shortest way from one point to another

- agent - entity that perceives its environment and acts upon that environment 

- state - a configuration of the anent and its environment 

- initial state - a state when agent begins 

- actions - retutns the set of actions that can be executed in state s 

- transition model - a description of what state results from performing any applicable action in any state 

result(s, a) returns the state resulting from performing action a in state s 

result(s, a) - input number one is state, and input number two is action 

the output is a new state 

the result() function should take care how to figure up how to get actiopns and make a results and this is called teansition model 

transition model describes how states and acrions relate to each other 

state space - the set of all srares reachable from the initial state by any saquence of actions 

### Goal test 
way to determine whether a given state is a goal state 

- **path cost** - numerical cost associated with a given path 

- it can calculate how expensive it is to make such option and tell AI how to minimize numerical values 

ehst metters is a total number of the steps from point a to point b

## Eearch problems
- initial state
- actions 
- transition model
- goal test 
- path cost function 


- Solution - a sequence of actions that leads from the initial state to a goal state 

### Optimal solutions - a solution that has the lowest path cost among the solutions 

### Node - dara structure that keeps track of
- a state 
- a parent (node that generated this node)
- an action (action applied to parent to get node)
- a path cost (from initial state to node)


### Approach
- start with a frontier that contains the initial state
- repeat 
-- if the frontier is empty, then no solution
-- remove a single node from a frontier 
-- if node contains a goal state, return the solution 
-- expand node and add resulting nodes to the frontier 

### Revised Approach 
- Start with a frontier that contains the initial state 
- Start with an empty explored set 
- if node contains goal state, return the solution 
- add a node to the explored state 
- expand node, add resulting nodes to the frontier if they are not already in the frontier or the explored set 

### depth-first search algorithm 
- search algorithm that always expands the deepest node in the frontier 

### Breadth-FIrst search algorithm
- search algorithm that always expands the shallowest node in the frontier 


### Queue 
- first in first out datatype 

Breath for search exploring several optional ways on the same time so it can fund the shortest solution among them 

Deep for seatch exploring only one by time to the end. THen if it is wrong it uses another one, 

### Uninformed search 
- search strategy that uses no problem-specific knowledge 

### Imformed search 
- search strategy that uses problem-specific knowledge to find solutions more effectively 

### Greedy best-first search 
- search algorithm that expands the node that is closest to the goal, as estimated by a heuristic function h(n)

### A^ Search 
- search algorithm that expands node with lowest value of g(n) + h(n)
g(n) = cost to reach node 
h(n) = estimated cost of goal 

optimal if 
- h(n) is admissibale (never overestimates the true cost), and 
- h(n) is consistent (for every node n and successor n' with step cost c, h(n) <= h(n') + c )

### Minimax 
- MAX(x) aims to maximize score
- MIN(O) aims to minimize score 


## Tik-tak toe gane
- So - initial state
- Player(s): returns which player to move in state s
- Actions(s): returns legal moves in state s
- Result(s, a): returns state after action a taken in state s 
- Utility(s): final numerical value for terminal state s

### Alpha-beta pruning

Prune umuesful elements from the search tree

- 255 168 possible tik-tak toe games can be played 

- 288 000 000 000 total possible chess games after four moves each 

- 10 in 29000 total possible chess games (lower bound)

### Depth-limited Minimax 
- **evaluation function** - function that estimates the expected utility of the game from a given state 

- in chess you can write evaluation function how many pieces you hava and how many pieces your oponent has 

## Knowledge
- human make concusions based on knowledge 

- **lnowledge-based agents** - agents that reason by operating on internal representations of knowledge 

Example:
- If it didn't rain, Harry visited Hagrid today 
- Harry visited Hagrid or Dumbledore today but not both
- Harry visited Dumbledore today 

We need some more info to make conclustions
Harry did not visited Hagrid today -> It rained today

### Sentence 
- an assertion about the world in a knowledge representation language 
- **propositional logic** - propositional symbols represent some sentences or facts 
- not, and, or, implication, biconditional 

- **Not** -> p - true; -p - false; p - false; -p - true;

- **AND** -> p - false; q - false; p AND q - false;
- p - false; q - true; p AND q - false;
- p - true; q - false; p AND q - false;
- p - true; q - true; p AND q - true;

- **OR** -> p - false; q - false; p OR q - false;
- p - false; q - true; p OR q - true;
- p - true; q - false; p OR q - true;
- p - true; q - true; p OR q - true; 

- **Implication (-->)** -> p - false; q - false; p --> q - true;
- p - false; q - true; p --> q - true;
- p - true; q - false; p --> q - false;
- p - true; q - true; p --> q - true;  

- **Biconditional (<-->)** -> p - false; q - false; p <--> q - true;
- p - false; q - true; p <--> q - false;
- p - true; q - false; p <--> q - false;
- p - true; q - true; p <--> q - true; 

### model 
- assignment of a truth value to every propotional symbol (a "possibe world")

### Entailement 
- a |= b 
- aplha entails bera 
- entailment means that in every model where a is true, b is also true


- Inference - the process of deriving new sentences from old ones 

- you put some sentences to AI, and using algoruthms AI coniders somt other sentecnes to be true 

- **model checking**  - is it true or false 
- to determine if KB |= a
-- enumerate all possible models 
-- if in every model KB is true, a is true, then KB entails a

### Example
- p: it is a Tuesday; q: it is raining; r: Harry will go for a run 

- KB: (p AND NOT q) --> r   p    not q

Query: r

p        q          r          KB
false    false      false      false
false    false      true       false
false    true      false       false
false    true       true       false
true    false      false       false
true    false      true         true
true    true      false        false
true    true      true         false 



