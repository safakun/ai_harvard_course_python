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

