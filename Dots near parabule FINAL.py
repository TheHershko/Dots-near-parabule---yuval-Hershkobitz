import matplotlib.pyplot as plt
import numpy as np


def plot(a, b, c):
    #creates a parabule using inputed values
    x = np.linspace(-50, 50, 100) #my x range is from -50 to 50 in Dina's approvement
    y = a * np.square(x) + b * x + c
    plt.plot(x, y)
    plt.xlabel("point num")
    plt.ylabel("sin function")
    plt.title("SOME CHART")
    plt.show()


def dotsOnGraph(arr, a, b, c):
    #counts how many of the dots given in arr are on the parabule drawn by a, b, and c
    counter = 0
    for i in arr:
        if i[0] >= -50 and i[0] <= 50:
            if i[1] == a * np.square(i[0]) + b * i[0] + c:
                counter += 1
    return counter
    

def dotsNearGraph(arr, a, b, c):
    #returns the sum of the y-distances between each dot given in arr and the parabule
    sum = 0
    for i in arr:
        y = a * np.square(i[0]) + b * i[0] + c
        sum += np.abs(y - i[1])
    return sum


def getABC():
    #Gets the function input from the user
    a = int(input('Please enter a: '))
    b = int(input('Please enter b: '))
    c = int(input('Please enter c: '))
    return a, b, c
    

def getArr():
    #Gets the dots collection from the user
    arr = np.array([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]])
    for i in range(10):
        arr[i, 0] = input('Please enter a dot x value: ')
        arr[i, 1] = input('Please enter a dot y value: ')
    return arr


def main():
    arr = getArr()
    a, b, c = getABC()
    plot(a, b, c)
    best = np.array([a, b, c, dotsNearGraph(arr, a, b, c)]) #first three numbers represent the a, b, c of the parabule and the forth represent the sum of distances
    for i in range(49):
        a, b, c = getABC()
        plot(a, b, c)
        current = dotsNearGraph(arr, a, b, c)
        if current < best[3]:
            best[0] = a
            best[1] = b
            best[2] = c
            best[3] = current
    print('\n' ,str.format('Best match: \n A: {0}, B: {1}, C: {2}, Distances: {3}', best[0], best[1], best[2], best[3]))

    
if __name__ == '__main__':
    main()