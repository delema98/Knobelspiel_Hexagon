import matplotlib.pyplot as plt
import ast
from random import randint


colors = []
for i in range(20):
    colors.append('#%06X' % randint(0, 0xFFFFFF))

fig, ax = plt.subplots() 

with open("../findAllSolutions/results_edit.txt") as f:
    allSolutions = f.read().splitlines() 


allCoordinates = [
            [4,6], [5,6], [6,6],
    [3.5,5], [4.5,5], [5.5,5], [6.5,5],
    [3,4], [4,4], [5,4], [6,4], [7,4],
    [3.5,3], [4.5,3], [5.5,3], [6.5,3],
            [4,2], [5,2], [6,2]
]

x = 0
for solution in allSolutions:

    i = 0
    for entry in ast.literal_eval(solution):

        circle = plt.Circle((allCoordinates[i][0], allCoordinates[i][1]), 0.5, color= colors[entry])
       
        ax.add_patch(circle)
        plt.text(allCoordinates[i][0] - 0.125, allCoordinates[i][1] - 0.125, entry)
        i = i + 1


    plt.xlim([0,10])
    plt.ylim([0,10])

    x = x + 1
    fig.savefig("{}.png".format(x))