from logic import *

rain = Symbol("rain") # it is raining
hagrid = Symbol("hagrid") # Harry visited Hagrid 
dumbledore = Symbol("dumbledore") # Harry visited Dumbledore 

# sentense = And(rain, hagrid)
knowledge = Implication(Not(rain), hagrid) 


print(knowledge.formula())



