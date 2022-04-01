# -*- coding: utf-8 -*-
"""
@author: Chloe Yong
"""
"""
This program:
    > draws an elliptic curve
    > draws two points P and Q
    > draws the line intersecting the two points
    > draws and finds the third point that intersects the line and the elliptic curve
"""

import matplotlib.pyplot as plt
import numpy as np
import math

def gradientLine (P_x, P_y, Q_x, Q_y):
    #y = mx + c
    m = (Q_y - P_y)/(Q_x - P_x)
    return m 

def intersectLine (x, y, m):
    c = y - (m*x)
    return c

def intersectPoint(P_x, Q_x, b, c):
        x = (b - c**2)/(P_x * Q_x)
        return -x

def drawGraph(a, b, P_x, Q_x):
    #scaling
    y, x = np.ogrid[-5:5:100j, -5:5:100j]
    
    #Assigning points P and Q
    #P_x =  -1.5
    P_y = float("{:.2f}".format(-math.sqrt((P_x**3) + (P_x*a) + b)))
    #Q_x = 0.75
    Q_y = float("{:.2f}".format(math.sqrt((Q_x**3)+ (Q_x*a) + b)))
    
    #Plots points P and Q
    plt.scatter(P_x, P_y, label = 'P')
    plt.scatter(Q_x, Q_y, label = 'Q')
    
    #Plots Elliptic Curve
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x,3) - x * a - b, [0])
    
    #Calculates values for the line intersecting points P and Q
    m = gradientLine(P_x, P_y, Q_x, Q_y)
    c = intersectLine(Q_x, Q_y, m)
    #scaling
    x = np.linspace (-3, 3, 100)
    y = float("{:.2f}".format(m))*x + float("{:.2f}".format(c))
    #Plots the line intersecting the points P and Q
    plt.plot(x, y, '-r', label='y = mx + c')
    
    #Plots the points R and -R, and the line that joins them together
    nR_x = intersectPoint(P_x, Q_x, b, c)
    nR_y = (m*nR_x) + c
    R_x = nR_x
    R_y = -nR_y
    plt.scatter(nR_x, nR_y)
    plt.scatter(R_x, R_y)
    plt.plot([R_x, nR_x], [R_y, nR_y])
    
    plt.grid()
    plt.show()
    
    #prints equation of the line
    print('E:' + 'y^2 = x^3 + '+ str(a) + "x^2 + "+ str(b))
    print('P = (' + str(P_x) + ', ' + str(P_y )+')')
    print('Q = (' + str(Q_x) + ', ' + str(Q_y )+')')
    print('y = ' + str(float("{:.2f}".format(m))) + 'x + ' + str(float("{:.2f}".format(c))))
    print('R = (' + str(float("{:.2f}".format(R_x)))+ ', ' + str(float("{:.2f}".format(R_y))) + ')')
    print('-R = (' + str(float("{:.2f}".format(nR_x)))+ ', ' + str(float("{:.2f}".format(nR_y))) + ')')


drawGraph(-2, 3, -1.5, 0.75)

    
