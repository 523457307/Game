import random
x = random.randint(0,500)
print(x)

body = [[100,100], [100,80], [100,60]]
body.insert(0,[120,100])
body.pop()
print(body)

startx = 100
starty = 100
cood = [{'x' : startx, 'y' : starty},
        {'x' : startx -1, 'y' : starty},
        {'x' : startx -2, 'y' : starty}]

cood[2]['y']
