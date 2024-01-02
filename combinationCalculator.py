import itertools
alternatives = ["BOW", "CLAP"]
length = 5
tried = []

combinations = list(itertools.product(alternatives, repeat=5))

run = True
while run:
    print("(1) Input an attempt")
    print("(2) Exit")
    tempStr = input()
    print()
    tempList = []
    if tempStr == "1":
        print("Choose the attempts you tried")
        print("(1) BOW")
        print("(2) CLAP")
        for i in range(5):
            if input() == "1":
                tempList.append("BOW")
            else:
                tempList.append("CLAP")
        print("How many were correct?")
        tempInt = int(input())
        print()
        tried.append([(tempList[0], tempList[1], tempList[2], tempList[3], tempList[4]), tempInt])
    else:
        run = False

for attempt in tried:    
    for x in range(len(combinations)-1, -1, -1):
        tempInt = 0
        for i in range(5):
            if combinations[x][i] == attempt[0][i]:
                tempInt += 1
        if tempInt != attempt[1]:
            combinations.pop(x)

print(combinations)