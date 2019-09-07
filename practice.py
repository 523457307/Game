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



x = [100,200,300]
print(x[1])
def foo (x):
    x[1] = 21312



foo(x)
print(x)


w = "www"
w = xx
xx = "asdasd"
import random
real_width = 10
real_height = 10
snake_pos = [random.randint(0,real_width),random.randint(0, real_height)]
print(snake_pos)

print (w)





snake_pos = [random.randint(3,real_width),random.randint(3, real_height)]

snake_body = [snake_pos, [snake_pos[0]-1,snake_pos[1]], [snake_pos[0]-2,snake_pos[1] ]]

print(snake_body)

for body in snake_body[1:]:
    print(body)
x = False
print(x)
