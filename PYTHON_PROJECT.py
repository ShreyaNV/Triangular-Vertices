#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from math import sqrt


# In[ ]:


def row_col(p):
	row = 1
	col = 1
	while p >= row + col:
		col += row
		row += 1
	return row,p-col


# In[ ]:


def triangle(points):
	row = [row_col(p)[0] for p in points]
	col = [row_col(p)[1] for p in points]
	if row[0] == row[1]:
		len = col[1] - col[0]
		return col[2] == col[1] and row[2] == row[1] + len
	else:
		len = row[1] - row[0]
		return col[0] == col [1] and row[2] == row[1] and col[2] == col[1] + len



# In[ ]:


def parallelogram(points):
	row = [row_col(p)[0] for p in points]
	col = [row_col(p)[1] for p in points]
	len = col[1] - col[0]
	return row[2] == row[3] and col[3] - col[2] == len and row[2] - row[0] == len and (col[2]==col[0] or col[2] == col[1])


# In[ ]:


def hexagon(points):
	row = [row_col(p)[0] for p in points]
	col = [row_col(p)[1] for p in points]
	len = col[1] - col[0]

	return row[0]==row[1] and col[2] == col[0] and row[2] == row[0] + len and col[3]==col[1]+len and row[3]==row[2] and col[4]==col[1]and row[4] == row[2]+len and col[5]==col[3] and row[5]==row[4]


# In[ ]:


def print_triangle():
    # create the Tkinter window
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    canvas = tk.Canvas(root, bg='midnightblue')
    canvas.pack(fill=tk.BOTH, expand=True)

    # get the screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # create the triangle
    triangle_size = 300
    triangle = canvas.create_polygon(
        screen_width/2-triangle_size/2, screen_height/2+triangle_size/2,
        screen_width/2+triangle_size/2, screen_height/2+triangle_size/2,
        screen_width/2, screen_height/2-triangle_size/2, outline = 'black', width = 3,
        fill='white')

    # add text
    text_label = tk.Label(root, text='Yay!!!The given points form a triangle :)', font=('Comic Sans MS', 24), fg='white', bg='midnightblue')
    text_label.place(relx=0.5, rely=0.2, anchor='center')

    # create confetti
    confetti = []
    for i in range(200):
        # generate a random color
        color = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))

        # generates random position for the two variables between the first and  
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        
        # generate a random velocity
        vx = random.uniform(2, -2)
        vy = random.uniform(10, -5)
        a = 5
        b = 10
        # add the confetti to the list
        confetti.append({
            'id': canvas.create_rectangle(x, y, a,b, fill=color, outline=''),
            'x': x,
            'y': y,
            'vx': vx,
            'vy': vy,
        })
    close_button = tk.Button(root, text="Close", font=('Comic Sans MS', 18), fg='black', bg='white', command=root.destroy)
    close_button.pack(side=tk.BOTTOM, pady=20)
    # animate the confetti
    while True:
        for c in confetti:
            # update the position of the confetti
            c['x'] += c['vx']
            c['y'] += c['vy']
            canvas.coords(c['id'], c['x'], c['y'], c['x']+10, c['y']+10)
            
            # apply gravity to the confetti
            c['vy'] += 0.1
            
            # wrap the confetti around the screen edges
            if c['x'] > screen_width:
                c['x'] = 0
            elif c['x'] < 0:
                c['x'] = screen_width
            if c['y'] > screen_height:
                c['y'] = 0
                c['vy'] = random.uniform(10, 5)
            elif c['y'] < 0:
                c['y'] = screen_height
        
        # update the Tkinter window
        root.update()
        
        # wait for a short time
        time.sleep(0.01)
        
    # start the Tkinter event loop
    root.mainloop()
    


# In[ ]:


import tkinter as tk
import random
import time

def print_parallelogram():
    # create the Tkinter window
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    canvas = tk.Canvas(root, bg='midnightblue')
    canvas.pack(fill=tk.BOTH, expand=True)

    # get the screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # create the parallelogram
    width = 300
    height = 200
    offset = 50
    parallelogram = canvas.create_polygon(
        screen_width/2-width/2, screen_height/2+height/2,
        screen_width/2+width/2, screen_height/2+height/2,
        screen_width/2+width/2-offset, screen_height/2-height/2,
        screen_width/2-width/2-offset, screen_height/2-height/2,
        outline = 'black', width = 3,
        fill='white')

    # add text
    text_label = tk.Label(root, text='Yay!!!The given points form a parallelogram', font=('Comic Sans MS', 24), fg='white',  bg='midnightblue')
    text_label.place(relx=0.5, rely=0.2, anchor='center')


    # create confetti
    confetti = []
    for i in range(200):
        # generate a random color
        color = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))

        # generate a random position
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
       
        # generate a random velocity
        vx = random.uniform(2, -2)
        vy = random.uniform(10, -5)
        # add the confetti to the list
        confetti.append({
            'id': canvas.create_rectangle(x, y, x+5, y+10, fill=color, outline=color),
            'x': x,
            'y': y,
            'vx': vx,
            'vy': vy,
        })
    close_button = tk.Button(root, text="Close", font=('Comic Sans MS', 18), fg='black', bg='white', command=root.destroy)
    close_button.pack(side=tk.BOTTOM, pady=20)
    # animate the confetti
    while True:
        for c in confetti:
            # update the position of the confetti
            c['x'] += c['vx']
            c['y'] += c['vy']
            canvas.coords(c['id'], c['x'], c['y'], c['x']+10, c['y']+10)
           
            # apply gravity to the confetti
            c['vy'] += 0.1
           
            # wrap the confetti around the screen edges
            if c['x'] > screen_width:
                c['x'] = 0
            elif c['x'] < 0:
                c['x'] = screen_width
            if c['y'] > screen_height:
                c['y'] = 0
                c['vy'] = random.uniform(10, 5)
            elif c['y'] < 0:
                c['y'] = screen_height
       
        # update the Tkinter window
        root.update()
       
        # wait for a short time
        time.sleep(0.01)
   
    root.mainloop()
    # start the Tkinter event loop


# In[ ]:


def print_hexagon():
    # create the Tkinter window
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    canvas = tk.Canvas(root, bg='midnightblue')
    canvas.pack(fill=tk.BOTH, expand=True)

    # get the screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # create the hexagon
    hexagon_size = 300
    hexagon = canvas.create_polygon(
        screen_width/2-hexagon_size/2, screen_height/2,
        screen_width/2-hexagon_size/4, screen_height/2+hexagon_size/2,
        screen_width/2+hexagon_size/4, screen_height/2+hexagon_size/2,
        screen_width/2+hexagon_size/2, screen_height/2,
        screen_width/2+hexagon_size/4, screen_height/2-hexagon_size/2,
        screen_width/2-hexagon_size/4, screen_height/2-hexagon_size/2,
        outline = 'black', width = 3,
        fill='white')

    # add text
    text_label = tk.Label(root, text='Yay!!!The given points form a hexagon', font=('Comic Sans MS', 24), fg='white',  bg='midnightblue')
    text_label.place(relx=0.5, rely=0.2, anchor='center')


    # create confetti
    confetti = []
    for i in range(200):
        # generate a random color
        color = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))

        # generate a random position
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
       
        # generate a random velocity
        vx = random.uniform(2, -2)
        vy = random.uniform(10, -5)
        a = 5
        b = 10
        # add the confetti to the list
        confetti.append({
            'id': canvas.create_rectangle(x, y, x+5, y+10, fill=color, outline=color),
            'x': x,
            'y': y,
            'vx': vx,
            'vy': vy,
        })
    close_button = tk.Button(root, text="Close", font=('Comic Sans MS', 18), fg='black', bg='white', command=root.destroy)
    close_button.pack(side=tk.BOTTOM, pady=20)
    # animate the confetti
    while True:
        for c in confetti:
            # update the position of the confetti
            c['x'] += c['vx']
            c['y'] += c['vy']
            canvas.coords(c['id'], c['x'], c['y'], c['x']+10, c['y']+10)
           
            # apply gravity to the confetti
            c['vy'] += 0.1
           
            # wrap the confetti around the screen edges
            if c['x'] > screen_width:
                c['x'] = 0
            elif c['x'] < 0:
                c['x'] = screen_width
            if c['y'] > screen_height:
                c['y'] = 0
                c['vy'] = random.uniform(10, 5)
            elif c['y'] < 0:
                c['y'] = screen_height
       
        # update the Tkinter window
        root.update()
       
        # wait for a short time
        time.sleep(0.01)
   
    root.mainloop()
    # start the Tkinter event loop


# In[ ]:


def shape(points):
    if len(points) == 3 and triangle(points):
        print_triangle()
    if len(points) == 4 and parallelogram(points):
        print_parallelogram()
    if len(points) == 6 and hexagon(points):
        print_hexagon()


# In[ ]:


import tkinter as tk

def create_sad_emoji_gui():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    canvas = tk.Canvas(root)
    canvas.pack(fill=tk.BOTH, expand=True)
    
    canvas.config(bg='red')
    screen_width = canvas.winfo_screenwidth()
    screen_height = canvas.winfo_screenheight()
    
    emoji_width = 400
    emoji_height = 400
    emoji_x = (screen_width - emoji_width) / 2
    emoji_y = (screen_height - emoji_height) / 2
    canvas.create_oval(emoji_x, emoji_y, emoji_x + emoji_width, emoji_y + emoji_height,fill="yellow", outline="black", width=5)
    canvas.create_oval(emoji_x + 100, emoji_y + 160, emoji_x + 140, emoji_y + 200, fill="black")
    canvas.create_oval(emoji_x + 260, emoji_y + 160, emoji_x + 300, emoji_y + 200, fill="black")
    canvas.create_arc(emoji_x + 70, emoji_y + 260, emoji_x + 330, emoji_y + 340,start=20, extent=140, style="arc", outline="black", width=5)
    canvas.create_text(screen_width/2, screen_height/2 + 300,text="Sorry, no acceptable figure can be formed",font=("Comic Sans MS", "50", "bold italic"), fill="midnightblue")
    
    close_button = tk.Button(root, text="Close", font=('Comic Sans MS', 18), fg='black', bg='white', command=root.destroy)
    close_button.pack(side=tk.BOTTOM, pady=20)

    root.mainloop()


# In[ ]:


class TriangularGridGUI:
    def __init__(self, master):
       
        self.master = master
        self.master.title("Triangular Vertices")
        self.master.geometry("2000x1000")
        self.master.configure(bg='MediumPurple3')
        # Define font settings
        font = ("Comic Sans MS", 16)

        # Create a frame to hold the canvas for drawing the triangular grid
        self.grid_frame = tk.Frame(self.master, bg='MediumPurple3')
        self.grid_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # Initialize the canvas for drawing the triangular grid
        self.canvas = tk.Canvas(self.grid_frame, width=1000, height=650, bg="MediumPurple3")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)          
        self.canvas.create_rectangle(1500, 100, 700, 215, fill="white", outline="black",width = 3)
        self.canvas.create_text(1100,150, text="Triangular Vertices", font=("Comic Sans MS", "50", "bold"), fill="black")
        # Call draw_grid() method to display the grid by default
       
        self.draw_grid()

        # Create a frame to hold the text entry widget and proceed and connect buttons
        self.input_frame = tk.Frame(self.master, bg='MediumPurple3')
        self.input_frame.place(relx=0.7, rely=0.5, anchor='center')

        # Create label to describe the text entry point
        label = tk.Label(self.input_frame, text="Enter points ", font=font, bg='MediumPurple3', fg='black')
        label.pack(side=tk.TOP)

        # Create the text entry widget
        self.entry = tk.Entry(self.input_frame, font=font)
        self.entry.pack(side=tk.TOP)
       
        # Create connect button with custom font and color
        button_connect = tk.Button(self.input_frame, text="Connect", font=font, bg='MediumPurple2', fg="black", command=self.connect_points)
        button_connect.pack(side=tk.TOP, padx=15, pady=15)

        # Create proceed button with custom font and color
        proceed_button = tk.Button(self.input_frame, text="Process", font=font, bg='MediumPurple2', fg="black", command=self.proceed)
        proceed_button.pack(side=tk.TOP, padx=15, pady=15)

        # Create connect button with custom font and color
        #button_connect = tk.Button(self.input_frame, text="Connect", font=font, bg='MediumPurple2', fg="black", command=self.connect_points)
        #button_connect.pack(side=tk.TOP, padx=15, pady=15)
        #Create refresh button with custom font and color
        refresh_button = tk.Button(self.input_frame, text="Refresh", font=font, bg='MediumPurple2', fg="black", command=self.clear_canvas)
        refresh_button.pack(side=tk.TOP, padx=15, pady=15)
   
    def get_coords(self, p):
        # Calculate the row and column of the point in the triangular grid
        row, col = row_col(p)

    # Calculate the x and y coordinates of the center of the circle representing the point
        x = col * 60 - 30 + (16.95 - row) * 30
        y = row * 52.2 - 30

    # Return the x and y coordinates as a tuple
        return (x, y)
    def connect_points(self):
    # Get the user-specified points from the text entry widget
        text = self.entry.get()
        points = list(map(int, text.split()))
        points.sort()
    # Calculate the coordinates of each point in the triangular grid
        coords = [self.get_coords(p) for p in points]
        coords1 = []
        if(len(points)==3):
            coords1.append(self.get_coords(points[0]))
            coords1.append(self.get_coords(points[1]))
            coords1.append(self.get_coords(points[2]))
            coords1.append(self.get_coords(points[0]))
           
        elif(len(points)==4):
            coords1.append(self.get_coords(points[0]))
            coords1.append(self.get_coords(points[1]))
            coords1.append(self.get_coords(points[3]))
            coords1.append(self.get_coords(points[2]))
            coords1.append(self.get_coords(points[0]))
           
        elif(len(points)==6):
            coords1.append(self.get_coords(points[0]))
            coords1.append(self.get_coords(points[1]))
            coords1.append(self.get_coords(points[3]))
            coords1.append(self.get_coords(points[5]))
            coords1.append(self.get_coords(points[4]))
            coords1.append(self.get_coords(points[2]))
            coords1.append(self.get_coords(points[0]))
           
        else:
            coords1 = coords
            coords1.append(self.get_coords(points[0]))

        if(len(points)==3) and triangle(points):
            self.text_item = self.canvas.create_text(1100,625, text="The points form a TRIANGLE :)", font=("Comic Sans MS", "25"), fill="black")
        elif len(points) == 4 and parallelogram(points):
            self.text_item = self.canvas.create_text(1150,625, text="The points form a PARALELLOGRAM :)", font=("Comic Sans MS", "25"), fill="black")
        elif len(points) == 6 and hexagon(points):
            self.text_item = self.canvas.create_text(1100,625, text="The points form a HEXAGON :)", font=("Comic Sans MS", "25"), fill="black")
        else:            
            self.text_item = self.canvas.create_text(1175,625, text="Sorry, no acceptable figure can be formed :(", font=("Comic Sans MS", "25"), fill="black")
           
        self.canvas.create_line(coords1, fill="black", width=3, tags="input_line")
    def clear_canvas(self):
        # Delete input lines
        self.canvas.delete("input_line")
        # Clear text entry widget
        self.entry.delete(0, tk.END)
        self.canvas.delete(self.text_item)
       

    def proceed(self):
    # Reading points
        text = self.entry.get()
        points = list(map(int, text.split()))
        new_points = points.copy()
        points.sort()
        is_valid = (len(points) == 3) and triangle(points) or (len(points) == 4) and parallelogram(points) or (len(points) == 6) and hexagon(points)
        if is_valid:
            shape(points)
            self.connect_points(points)
        else:
            create_sad_emoji_gui()
            self.connect_points(points)
           
           
    def draw_grid(self):
        size = 15

    # Calculate the coordinates of the top point of the equilateral triangle
        x = 200
        y = 100
        side = 60
        height = side * sqrt(3) / 2
    # Calculate the width and height of the canvas
        canvas_width = (size + 1) * side
        canvas_height = size * height + side

    # Set the canvas size
        self.canvas.config(width=canvas_width, height=canvas_height)

    # Center the canvas
        self.canvas.xview_moveto(1.0)
        self.canvas.yview_moveto(1.0)

    # Draw the circles on
        number = 1
        for i in range(size):
            for j in range(i+1):
                x_coord = j*side+ (size-i)*side/2
                y_coord = i*height + side/2
                self.canvas.create_oval(x_coord-15, y_coord-15, x_coord+15, y_coord+15, fill="white")
                self.canvas.create_text(x_coord, y_coord, text=str(number))
                number += 1
               
root = tk.Tk()
gui = TriangularGridGUI(root)
root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




