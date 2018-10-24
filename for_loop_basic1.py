num_count=range(0,151)
for i in num_count:
    print(i)

mult_five=range(5,1000005,5)
for i in mult_five:
    print(i)

dojo_count=range(1,101)
for i in dojo_count:
    print(i)
    if i % 5 == 0:
        print('Coding')
    if i % 10 == 0:
        print('Dojo')

huge_sucker=range(1,500001,2)
x=0
for i in huge_sucker:
    x = x + i
print(x)

pos_countdown=range(2018,0,-4)
for i in pos_countdown:
    print(i)

def my_range(lowNum, highNum, mult):
    x = mult
    while x <= highNum:
            if x >= lowNum:
                print(x)
            x = x + mult
list(my_range(2,9,3))

list = [3,5,1,2]
for i in list:
    print(i)
# Output: 3, 5, 1, 2 -- Reason: the loop is iterating through all variables withIN the list.

list = [3,5,1,2]
for i in range(list):
    print(i)
# Output: Error -- Reason: I know this won't work due to my experience trying to get 'Flexible Countdown' to work properly. I think the reason is that that range() will only take a start, stop and step.

list = [3,5,1,2]
for i in range(len(list)):
    print(i)
# Output: 1, 2, 3, 4 -- Reason: the loop is iterating through all variable withIN the range function, using the length of the list object.