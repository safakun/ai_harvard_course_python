from logic import *

rain = Symbol("rain") # it is raining
hagrid = Symbol("hagrid") # Harry visited Hagrid 
dumbledore = Symbol("dumbledore") # Harry visited Dumbledore 

sentense = And(rain, hagrid)

print(sentense.formula())



