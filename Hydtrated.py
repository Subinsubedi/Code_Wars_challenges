'''
Description:
Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

For example:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5


'''
#there is a better method to do this I think but this is what I first came up with for now

import math

def litres(time):
    if time == 1:
        return time
    else:
        time=time*0.5
        num=int(math.floor(time))
        return num
    return 0


