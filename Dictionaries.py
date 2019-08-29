x = (1,2,3,4,5)
y = (6,7,8,9)
#tuples are the default in python
a,b,c = 1,2,3

list = [x,y]
(age, school) = "30,17".split(',')

dict = {'k1': 'pink', 'k2': 'red', 'k3': 'purp', 'k4': 'yellow'}
print(dict['k1']) #putputs the definitons that you assigned

#alternative way to set up dictionary
team = {}
team['player1'] = 'ben'
team['player2'] = 'frank'

prices = {
    "Box of Spag" : 4,
    "lasagna" : 5,
    "hamburger" : 6
}

quantity = {
    "box of Spag" : 10,
    "lasagna" : 20,
    "hamburger" : 30
}
# the initial money spent is zero and then the method calls for the number of spag,las and hamburger and their
# quantities and the output is the total amount spent  
money_spent = 0
for i in prices:
    money_spent = money_spent + (prices[i]*quantity[i])
print(money_spent)

