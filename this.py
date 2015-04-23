from __future__ import division

import matplotlib.pyplot as plt

G = 3
MPC = .94 
T = .2
pi = 3
B = 10
D = .5

def IS(r):
	i = r - pi
	I = B - D * i #Investment increases as interest rate decreases
	#Y = MPC * (Y - T * Y) + I(i) + G This is the function for the IS curve
	Y = (I + G) / (1 - MPC * (1 - T)) #Algebraically solved for Y as function of i
	return Y
def plot_IS():
	plt.plot([IS(pi), IS(10 + pi)], [pi + 0, pi + 10])
	plt.title('This')
	plt.ylabel('Nominal Interest Rate')
	plt.xlabel('Output')
	
plot_IS()
plt.show()​
