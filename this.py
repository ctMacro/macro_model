from __future__ import division
 
import matplotlib.pyplot as plt
 
import numpy as np
from numpy import linalg
 
G = 3 #Government Spending
MPC = .94 #Marginal Propensity to Consume
T = .2 #Average Tax Rate
pi = 3 #Average inflation rate (in percentage points)
B = 15 #Investment Line y-intercept
D = .5 #Investment Line slope
M = 12 #Money Supply
k = .2
h = .8
 
 
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
 
intercept_vector = np.array([(B + G)/D + pi,LM(0)])
matrix = np.array([[(1-0)/(IS(1) - IS(0)), 1], [(LM(1) - LM(0))/(1-0), 1]])

equilibrium = abs(np.linalg.solve(matrix, intercept_vector))



def plot_IS_LM():
	I_S = plt.plot([IS(pi), IS(30 + pi)], [pi + 0, pi + 30], label='IS')
	L_M = plt.plot([30, 100], [LM(30), LM(100)], label='LM')
	plt.legend([I_S, L_M])
	plt.title('IS-LM Model')
	plt.ylabel('Nominal Interest Rate')
	plt.xlabel('Output')
	I_S = plt.axes()
	I_S.arrow(equilibrium[0] - 20, equilibrium[1], 15, 0, head_width = 2, head_length = 2, fc='k', ec='k')
	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

	
print LM(0)




print equilibrium
plot_IS_LM()
plt.show()