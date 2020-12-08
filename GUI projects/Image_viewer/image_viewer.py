from tkinter import *
#to add images
from PIL import ImageTk, Image

root = Tk()
#add atitle
root.title('Image viewer')
#custom icon
# root.iconbitmap('tt.ico')


my_img_1 = ImageTk.PhotoImage(Image.open('images/1.jpg'))
my_img_2 = ImageTk.PhotoImage(Image.open('images/2.jpg'))
my_img_3 = ImageTk.PhotoImage(Image.open('images/3.jpg'))

img_lst = [my_img_1 , my_img_2 , my_img_3]

my_label = Label(image= my_img_1)
my_label.grid(row=0, column=0, columnspan= 3)

#CREATE A STATUS BAR
status_bar = Label(root, text= 'image 1 of ' + str(len(img_lst)), bd= 1, relief= SUNKEN, anchor= E)

#defining button action
def forward(image_number):
	global my_label
	global back_button
	global forward_button

	my_label.grid_forget()
	my_label = Label(image= img_lst[image_number-1])
	forward_button = Button(root, text= '>>',bg= 'green', command= lambda: forward(image_number+1))
	back_button = Button(root, text= '<<',bg= 'green',command= lambda: back(image_number-1))

	if image_number == 3:
		forward_button = Button(root, text= '>>',bg= 'green', state= DISABLED)

	my_label.grid(row=0, column=0, columnspan= 3)
	back_button.grid(row=1,column=0)
	exit_button.grid(row=1,column=1)
	forward_button.grid(row=1,column=2)

	#update status bar
	status_bar = Label(root, text= 'image ' +str(image_number) + ' of ' + str(len(img_lst)), bd= 1, relief= SUNKEN, anchor= E)
	status_bar.grid(row=2, column=0, columnspan=3, sticky= W+E)

def back(image_number):
	global my_label
	global back_button
	global forward_button

	my_label.grid_forget()
	my_label = Label(image= img_lst[image_number-1])
	forward_button = Button(root, text= '>>',bg= 'green', command= lambda: forward(image_number+1))
	back_button = Button(root, text= '<<',bg= 'green',command= lambda: back(image_number-1))

	if image_number == 1:
		back_button = Button(root, text= '<<',bg= 'green', state= DISABLED)
	my_label.grid(row=0, column=0, columnspan= 3)
	back_button.grid(row=1,column=0)
	exit_button.grid(row=1,column=1)
	forward_button.grid(row=1,column=2)

	#update status bar
	status_bar = Label(root, text= 'image ' +str(image_number) + ' of ' + str(len(img_lst)), bd= 1, relief= SUNKEN, anchor= E)
	status_bar.grid(row=2, column=0, columnspan=3, sticky= W+E)

#create buttons
back_button = Button(root, text= '<<',bg= 'green',command= back, state=DISABLED)
exit_button = Button(root, text= 'EXIT',bg= 'green', command= root.quit)
forward_button = Button(root, text= '>>',bg= 'green', command= lambda: forward(2))

#call them on screen
back_button.grid(row=1,column=0)
exit_button.grid(row=1,column=1)
forward_button.grid(row=1,column=2, pady= 10)
status_bar.grid(row=2, column=0, columnspan=3, sticky= W+E)

root.mainloop()