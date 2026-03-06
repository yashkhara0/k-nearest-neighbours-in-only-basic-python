import matplotlib.pyplot as plt
import random as ran
import math as m

#creating each point and its values    
def createVals():
    x = ran.randint(0,100)
    y = ran.randint(0,100)
    return x,y

database = [["vanilla", ()],
            ["chocolate",()],
            ["toffee",()],
            ["applesauce",()],
            ["orange sorbet",()],
            ["cinnamon",()],
            ["strawberry",()],
            ["dairy-free choc",()]
            ]

for i in range(len(database)-1):
    x,y = createVals()
    database[i][1] = (x,y)
    plt.plot(database[i][1][0] ,database[i][1][1], marker = 'o', markersize = 6)
    
database[-1][1] = (5,5)   
plt.plot(database[-1][1][0] ,database[-1][1][1], marker = 'o', markersize = 6)

#knn implementation
x = int(input("Enter the x value of your flavour"))
y = int(input("Enter the y value of your flavour"))

# pythagoras - a^2 + b^2 = c^2 -- thus distance is m.sqrt((x**2)+(y**2))

dists = []

for data in database:
    x1 = x - data[1][0]
    y1 = y - data[1][1]
    dist = (m.sqrt((x1**2) + (y1**2)))
    dists.append([dist, data[0]])
    
mindist = dists[0]
for dist in dists:
    if dist[0] < mindist[0]:
        mindist = dist

print(f"This is likely {mindist[1]}")





plt.show()
