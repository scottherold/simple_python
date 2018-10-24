def beCheerful(repeat=98):
        print("good morning!"*repeat)

def randInt(min=0,max=100):
    x = -1
    import random
    while x < min:
        x = int(random.random()*max)
    return x



