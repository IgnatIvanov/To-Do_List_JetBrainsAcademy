def tallest_people(**peoples):
    for pare in sorted(peoples.items()):
        if pare[1] == max(peoples.values()):
            print(pare[0], ':', pare[1])
