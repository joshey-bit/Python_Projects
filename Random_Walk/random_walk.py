'''create random walk class'''
from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
	def __init__(self, num_points = 5000):
		self.num_points = num_points
		#start from origin
		self.x_values = [0]
		self.y_values = [0]

	def get_step(self):
		'''method to increase the steps'''
		direction = choice([-1,1])
		distance = choice([0,1,2,3,4])
		step = direction * distance
		return step

	def fill_walk(self):
		'''method to create random steps'''
		while len(self.x_values) < self.num_points:
			#create xstep and y step:
			x_step = self.get_step()
			y_step = self.get_step()

			#reject no walk
			if x_step == 0 and y_step == 0:
				continue

			#create next values for list
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			#append the new values
			self.x_values.append(next_x)
			self.y_values.append(next_y)



#creating an instance and plotting it
#creatinging multiple walks
while True:
	rw = RandomWalk() #create an instance for random walk
	rw.fill_walk()

	#set size of plot window
	plt.figure(dpi= 120,figsize= (10,6))

	point_numbers = list(range(rw.num_points))
	# plt.scatter(rw.x_values,rw.y_values,s = 5, c=point_numbers, cmap= plt.cm.Blues , zorder = 1)
	plt.plot(rw.x_values,rw.y_values, linewidth= 1, color = 'blue',zorder= 1) 

	#create starting and ending points od diffrernt color and size
	plt.scatter(0,0,color='green',s=100, zorder = 2)
	plt.scatter(rw.x_values[-1],rw.y_values[-1],color='red',s=100, zorder = 2)

	#hiding the axes
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	plt.show()

	#ask wheter to continue runnign
	keep_running = input("continue runnign? (y/n): ")
	if keep_running == 'n':
		break