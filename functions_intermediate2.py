# Question 1
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]["last_name"] = "Bryant"
sports_directory["soccer"][0] = "Andres"
z[0]["y"] = 30

# Question 2
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(arr):
    i = 0
    for element in arr:
        print("first_name -",arr[i]["first_name"]+",","last_name -",arr[i]["last_name"])
        i = i+1
iterateDictionary(students)

# Question 3
def iterateDictionary2(x,arr):
    i = 0
    for element in arr:
        print(arr[i][x])
        i = i + 1
iterateDictionary2('first_name',students)

# Question 4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printDojoInfo(arr):
    i = 0
    print(len(arr["locations"]),"LOCATIONS")
    for element in arr["locations"]:
        print(arr["locations"][i])
        i = i + 1
    print('')
    i = 0
    print(len(arr["instructors"]),"INSTRUCTORS")
    for element in arr["instructors"]:
        print(arr["instructors"][i])
        i = i + 1
printDojoInfo(dojo)