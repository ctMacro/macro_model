from __future__ import division

import matplotlib.pyplot as plt

from matplotlib.legend_handler import HandlerLine2D

import numpy as np

from numpy import linalg
 
G = 3 #Government Spending
MPC = .94 #Marginal Propensity to Consume
T = .2 #Average Tax Rate
pi = 3 #Average inflation rate (in percentage points)
B = 15 #Investment Line y-intercept
D = .5 #Investment Line slope
M = 12 #Money Supply in trillions
k = .4
h = .4
year = 0
Time_frame = 1



def IS(r):
    i = r - pi
    I = B - D * i #Investment increases as interest rate decreases
    #Y = MPC * (Y - T * Y) + I(i) + G This is the function for the IS curve
    Y = (I + G) / (1 - MPC * (1 - T)) #Algebraically solved for Y as function of i
    return Y
     
def LM(Y):
    i = (k * Y - M)/h
    r = i + pi #L(Y, i) is defined here as M = k*Y - h * i
    return r


def plot_IS_LM():
	intercept_vector = np.array([(B + G)/D + pi,LM(0)])
	matrix = np.array([[-(1-0)/(IS(1) - IS(0)), 1], [-(LM(1) - LM(0))/(1-0), 1]])
	equilibrium = np.linalg.solve(matrix, intercept_vector)
	I_S = plt.plot([IS(pi), IS(30 + pi)], [pi + 0, pi + 30], label='IS')
	L_M = plt.plot([30, 60], [LM(30), LM(60)], label='LM')
	plt.legend([I_S, L_M])
	plt.title('IS-LM Model')
	plt.ylabel('Nominal Interest Rate')
	plt.xlabel('Output')
	I_S = plt.axes()
	plt.plot([equilibrium[0], 0], [equilibrium[1], equilibrium[1]], 'r--', label='r '+ repr(year))
	plt.plot([equilibrium[0], equilibrium[0]], [equilibrium[1], 0], 'k--', label='Y '+ repr(year))
	equibrium_interest_rate = '%.2f' % equilibrium[1]
	equilibrium_output = '%.2f' % equilibrium[0]
	plt.text(equilibrium[0], 0, equilibrium_output)
	plt.text(0, equilibrium[1],equibrium_interest_rate)
	plt.legend(handler_map={LM: HandlerLine2D(numpoints=4)})
	
while Time_frame != (year-1):
	plot_IS_LM()
	M = M + 2
	year = year + 1

plt.grid()
plt.show()