cont = True
entries = []
while(cont):
    try:
        label = input("enter the name:")
        quadrant = int(input("enter quadrant:"))
        ring = int(input("enter rint:"))

        temp = {
        "quadrant": quadrant,
        "ring": ring,
        "label": label,
        "active": True,
        "moved": 0
        }
        entries.append(temp)

        yes = input("do you want to continue (y/n)?")
        if(yes=="n"):   cont=False
        else : cont = True
    except :
        break


import json
with open('data.json', 'w') as f:
    json.dump(entries, f)
