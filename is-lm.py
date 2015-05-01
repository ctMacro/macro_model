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
Time_frame = 1 # number of years the program will run plus the initial year.

f, this = plt.subplots(2, 2)

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
	intercept_vector = np.array([(B + G)/D + pi,LM(0)]) #Solved IS and LM for their Constants
	matrix = np.array([[-(1-0)/(IS(1) - IS(0)), 1], [-(LM(1) - LM(0))/(1-0), 1]]) #Put IS and LM into a matrix where variables are output and interest rate
	equilibrium = np.linalg.solve(matrix, intercept_vector) #Solving for the equilibrium output and interest rate
	I_S = this[p, q].plot([IS(pi), IS(30 + pi)], [pi + 0, pi + 30], label='IS') #Plotting the IS line
	L_M = this[p, q].plot([30, 60], [LM(30), LM(60)], label='LM') #Plotting the LM line
	this[p, q].text(45, -5, 'Output', ha='center', va='center')
	this[p, q].text(-5, 15, 'Nominal Interest Rate', ha='center', va='center', rotation='vertical')
	this[p, q].legend([I_S, L_M])
	this[p, q].plot([equilibrium[0], 0], [equilibrium[1], equilibrium[1]], 'r--', label='r '+ repr(year)) #Graphically show the equilibrium interest rate
	this[p, q].plot([equilibrium[0], equilibrium[0]], [equilibrium[1], 0], 'k--', label='Y '+ repr(year)) #Graphically show the equilibrium output
	equibrium_interest_rate = '%.0f' % equilibrium[1]
	equilibrium_output = '%.0f' % equilibrium[0]
	this[p, q].text(equilibrium[0], 0, equilibrium_output)
	this[p, q].text(0, equilibrium[1],equibrium_interest_rate)
	this[p, q].legend(handler_map={LM: HandlerLine2D(numpoints=4)})
	
temp_M = M   #These are so we can reset the values once the loops are done
temp_year = year
temp_G = G
temp_MPC = MPC
temp_T = T
#plt.figure(1)
#plt.subplot(411)
# p & q are placeholders for the grid coordinates for the four graphs
while Time_frame != (year-1):
	p = 0
	q = 0
	plot_IS_LM()
	this[0,0].set_title('10% Increase in Real Money Supply')
	new_M = M * 1.1 #10% increase in the money supply
	M = new_M
	year = year + 1
M = temp_M
year = temp_year

#plt.subplot(412)
while Time_frame != (year-1):
	p = 0
	q = 1
	plot_IS_LM()
	this[0, 1].set_title('Increase in Government Spending by $1 trillion')
	G = G + 1 #Demo what happens when there's an increase in government spending by 1 trillion
	year = year + 1
G = temp_G
year = temp_year

#plt.subplot(413)
while Time_frame != (year-1):
	p = 1
	q = 0
	plot_IS_LM()
	this[1, 0].set_title('Consumers Prefer Saving Over Spending')
	MPC = .7 #Demo what happens when people's preferences shift towards saving
	year = year + 1
MPC = temp_MPC
year = temp_year

#plt.subplot(414)
while Time_frame != (year-1):
	p = 1 
	q = 1
	plot_IS_LM()
	this[1, 1].set_title('Increase in the Tax Rate from 20% to 30%')
	T = .3 #Demo what happens when there is an increase in the tax rate
	year = year + 1
T = temp_T
year = temp_year

plt.show()