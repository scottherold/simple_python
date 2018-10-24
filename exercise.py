def beCheerful(repeat=98):
        print("good morning!"*repeat)

# def randInt(max='', min=''):
#     x = -1
#     import random
#     if max is None:
#         max = 100
#     if min is None:
#         min = 0
#     while x < int(min):
#         x = int(random.random()*int(max))
#     return(x)

# print(randInt())

def randInt(min=0,max=100):
    x = -1
    import random
    while x < min:
        x = int(random.random()*max)
    return x

print(randInt(min=50,max=500))



