#!/usr/bin/env python
# coding: utf-8

# In[42]:


import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk


# In[43]:


def row_col(p):
	row = 1
	col = 1
	while p >= row + col:
		col += row
		row += 1
	return row,p-col


# In[44]:


def triangle(points):
	row = [row_col(p)[0] for p in points]
	col = [row_col(p)[1] for p in points]
	if row[0] == row[1]:
		len = col[1] - col[0]
		return col[2] == col[1] and row[2] == row[1] + len
	else:
		len = row[1] - row[0]
		return col[0] == col [1] and row[2] == row[1] and col[2] == col[1] + len


# In[45]:


def parallelogram(points):
	row = [row_col(p)[0] for p in points]
	col = [row_col(p)[1] for p in points]
	len = col[1] - col[0]
	return row[2] == row[3] and col[3] - col[2] == len and row[2] - row[0] == len and (col[2]==col[0] or col[2] == col[1])


# In[46]:


def hexagon(points):
	row = [row_col(p)[0] for p in points]
	col = [row_col(p)[1] for p in points]
	len = col[1] - col[0]

	return row[0]==row[1] and col[2] == col[0] and row[2] == row[0] + len and col[3]==col[1]+len and row[3]==row[2] and col[4]==col[1]and row[4] == row[2]+len and col[5]==col[3] and row[5]==row[4]


# In[133]:


import tkinter as tk
import math

class EquilateralTriangleGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Equilateral Triangle")
        
        # Initialize the canvas for drawing
        self.canvas = tk.Canvas(self.master, width=2000, height=830, bg="white")
        self.canvas.pack()
        
        # Create a button to draw the triangle
        self.draw_button = tk.Button(self.master, text="Draw Triangle", command=self.draw_triangle)
        self.draw_button.pack(pady=10)
        
    def draw_triangle(self):
        # Define the size of the equilateral triangle
        size = 200
        
        # Calculate the coordinates of the three vertices of the triangle
        x1 = 200
        y1 = 200 - math.sqrt(3) * size / 3
        x2 = 200 - size / 2
        y2 = 200 + math.sqrt(3) * size / 6
        x3 = 200 + size / 2
        y3 = 200 + math.sqrt(3) * size / 6
        
        # Draw the triangle on the canvas
        self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="lightblue", outline="black", width=5)
        bbox = self.canvas.bbox("all")
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        dx = (canvas_width - bbox[2] - bbox[0]) / 2 - bbox[0]/4
        dy = (canvas_height - bbox[3] - bbox[1]) / 2 - bbox[1]/4
        self.canvas.move("all", dx, dy)
    
root = tk.Tk()
gui = EquilateralTriangleGUI(root)
root.mainloop()


# In[157]:


import tkinter as tk
import math

class TriangleGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Triangle Figure")
        
        # Initialize the canvas for drawing
        self.canvas = tk.Canvas(self.master, width=2000, height=830, bg="white")
        self.canvas.pack()
        
        # Draw the triangle
        self.draw_triangle()
        
    def draw_triangle(self):
        # Define the length of the sides of the equilateral triangle
        size = 200
        
        # Calculate the coordinates of the three vertices of the triangle
        x1 = 200
        y1 = 200 - math.sqrt(3) * size / 3
        x2 = 200 - size / 2
        y2 = 200 + math.sqrt(3) * size / 6
        x3 = 200 + size / 2
        y3 = 200 + math.sqrt(3) * size / 6
        
        # Convert the vertex coordinates to a list of integers
        #coords = [int(coord) for vertex in vertices for coord in vertex]
        
        # Draw the triangle on the canvas
        self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="lightblue", outline="black", width=5)
        bbox = self.canvas.bbox("all")
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        dx = (canvas_width - bbox[2] - bbox[0]) / 900 - bbox[0]/400
        dy = (canvas_height - bbox[3] - bbox[1]) / 900 - bbox[1]/400
        self.canvas.move("all", dx, dy)
    
root = tk.Tk()
gui = TriangleGUI(root)
root.mainloop()


# In[173]:


import math

class HexagonGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hexagon Figure")
        
        # Initialize the canvas for drawing
        self.canvas = tk.Canvas(self.master, width=2000, height=830, bg="white")
        self.canvas.pack()
        
        # Draw the hexagon
        self.draw_hexagon()
    
    def draw_hexagon(self):
        # Define the radius of the circle that circumscribes the hexagon
        radius = 200
        
        # Calculate the coordinates of the six vertices of the hexagon
        vertices = []
        for i in range(6):
            x = 600 + radius * math.cos(i * math.pi / 3)
            y = 600 + radius * math.sin(i * math.pi / 3)
            vertices.append((x, y))
        
        # Convert the vertex coordinates to a list of integers
        coords = [int(coord) for vertex in vertices for coord in vertex]
        
        # Draw the hexagon on the canvas
        self.canvas.create_polygon(coords, fill="lightblue", outline="black", width=5)
        bbox = self.canvas.bbox("all")
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        dx = (canvas_width - bbox[2] - bbox[0]) / 0 - bbox[0]/40
        dy = (canvas_height - bbox[3] - bbox[1]) / 80 - bbox[1]/40
        self.canvas.move("all", dx, dy)
    
root = tk.Tk()
gui = HexagonGUI(root)
root.mainloop()


# In[174]:


import math

class HexagonGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hexagon Figure")
        
        # Initialize the canvas for drawing
        self.canvas = tk.Canvas(self.master, width=2000, height=830, bg="white")
        self.canvas.pack()
        
        # Create a button to draw the hexagon
        self.draw_button = tk.Button(self.master, text="Draw Hexagon", command=self.draw_hexagon)
        self.draw_button.pack(pady=10)
        
    def draw_hexagon(self):
        # Define the radius of the circle that circumscribes the hexagon
        radius = 200
        
        # Calculate the coordinates of the six vertices of the hexagon
        vertices = []
        for i in range(6):
            x = 600 + radius * math.cos(i * math.pi / 3)
            y = 600 + radius * math.sin(i * math.pi / 3)
            vertices.append((x, y))
        
        # Convert the vertex coordinates to a list of integers
        coords = [int(coord) for vertex in vertices for coord in vertex]
        
        # Draw the hexagon on the canvas
        self.canvas.create_polygon(coords, fill="lightblue", outline="black", width=5)
        bbox = self.canvas.bbox("all")
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        dx = (canvas_width - bbox[2] - bbox[0]) / 2 - bbox[0]/6
        dy = (canvas_height - bbox[3] - bbox[1]) / 2 - bbox[1]/6
        self.canvas.move("all", dx, dy)
    
root = tk.Tk()
gui = HexagonGUI(root)
root.mainloop()


# In[175]:


import tkinter as tk

class HexagonGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hexagon Figure")
        
        # Initialize the canvas for drawing
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="white")
        self.canvas.pack()
        
        # Load the hexagon image
        self.hexagon_image = tk.PhotoImage(file="hexagon.png")
        
        # Display the hexagon image in the center of the canvas
        self.canvas.create_image(200, 200, image=self.hexagon_image)
    
root = tk.Tk()
gui = HexagonGUI(root)
root.mainloop()


# In[176]:


get_ipython().system('mkdir images')


# In[186]:


import tkinter as tk
from PIL import Image
class HexagonGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hexagon Figure")
        
        # Initialize the canvas for drawing
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="white")
        self.canvas.pack()
        
        # Load the hexagon image
        #self.hexagon_image = tk.PhotoImage(file="images/hexagon.png")
        self.hexagon_image = tk.PhotoImage(file="images/hexagon.png")
        #self.canvas.create_image(x, y, image=self.hexagon_image)
        
        image = Image.open("images/hexagon.png")
        image.show()

        # Display the hexagon image in the center of the canvas
        self.canvas.create_image(600, 600, image=self.hexagon_image)
    
root = tk.Tk()
gui = HexagonGUI(root)
root.mainloop()


# In[48]:


def shape(points):
    row = [row_col(p)[0] for p in points]
    col = [row_col(p)[1] for p in points]
    if len(points) == 3 and triangle(points):
        root = tk.Tk()
        gui = TriangleGUI(root)
        root.mainloop()
    if len(points) == 4 and parallelogram(points):
        root = tk.Tk()
        gui = ParallelogramGUI(root)
        root.mainloop()
    if len(points) == 6 and hexagon(points):
        root = tk.Tk()
        gui = HexagonGUI(root)
        root.mainloop()


# In[77]:


while True:
  line= input()
  if line == '@':
    break
  points = list(map(int, line.split()))
  new_points = points.copy()
  points.sort()
  is_valid=(len(points) == 3) and triangle(points) or (len(points) == 4) and parallelogram(points) or (len(points) == 6) and hexagon(points) 
  if is_valid:
    shape(points)
  print(f"{' '.join(map(str, new_points))} are {' not' if not is_valid else ' '} the vertices of {'an acceptable figure' if not is_valid else (len(points) == 3 and 'a triangle'or len(points) == 4 and 'a parallelogram' or ' a hexagon')}")


# In[75]:


import tkinter as tk
from math import sqrt

class TriangularGridGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Triangular Grid")

        # Initialize the canvas for drawing
        self.canvas = tk.Canvas(self.master, width=2000, height=835, bg="purple")
        self.canvas.pack()

        # Create an entry widget to take input for the grid size
        self.label = tk.Label(self.master, text="Enter grid size:")
        self.label.pack(pady=20)
        self.entry = tk.Entry(self.master, width=10)
        self.entry.pack(pady=5)
        self.button = tk.Button(self.master, text="Draw Grid", command=self.draw_grid)
        self.button.pack(pady=5)

    def draw_grid(self):
        # Get the size of the grid from the input entry
        try:
            size = int(self.entry.get())
        except ValueError:
            size = 5

        # Calculate the coordinates of the top point of the equilateral triangle
        x = 200
        y = 100
        side = 40
        height = side * sqrt(3) / 2

        # Draw the circles on the canvas
        count = 1
        for i in range(size):
            for j in range(i+1):
                x_coord = x + (j - i/2) * side
                y_coord = y + i * height
                self.canvas.create_oval(x_coord-10, y_coord-10, x_coord+10, y_coord+10, fill="pink")
                self.canvas.create_text(x_coord, y_coord, text=str(count))
                count += 1

# Create the main window and run the GUI
root = tk.Tk()
gui = TriangularGridGUI(root)
root.mainloop()


# In[73]:


import tkinter as tk
from math import sqrt

class TriangularGridGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Triangular Grid")

        # Initialize the canvas for drawing
        self.canvas = tk.Canvas(self.master, width=1000, height=800, bg="purple", scrollregion=(0, 0, 2000, 2000))
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Add scrollbars if necessary
        self.hscrollbar = tk.Scrollbar(self.master, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.vscrollbar = tk.Scrollbar(self.master, orient=tk.VERTICAL, command=self.canvas.yview)
        self.vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(xscrollcommand=self.hscrollbar.set, yscrollcommand=self.vscrollbar.set)

        # Create an entry widget to take input for the grid size
        self.label = tk.Label(self.master, text="Enter grid size:")
        self.label.pack(pady=20)
        self.entry = tk.Entry(self.master, width=10)
        self.entry.pack(pady=5)
        self.button = tk.Button(self.master, text="Draw Grid", command=self.draw_grid)
        self.button.pack(pady=5)

    def draw_grid(self):
        # Get the size of the grid from the input entry
        try:
            size = int(self.entry.get())
        except ValueError:
            size = 5

        # Calculate the coordinates of the top point of the equilateral triangle
        x = 200
        y = 100
        side = 40
        height = side * sqrt(3) / 2

        # Calculate the width and height of the canvas
        canvas_width = (size + 1) * side
        canvas_height = size * height + side / 2

        # Set the canvas size
        self.canvas.config(scrollregion=(0, 0, canvas_width, canvas_height), width=canvas_width, height=canvas_height)

        # Center the canvas
        self.canvas.xview_moveto(0.5)
        self.canvas.yview_moveto(0.5)

        # Draw the circles on the canvas
        count = 1
        for i in range(size):
            for j in range(i+1):
                x_coord = x + (j - i/2) * side
                y_coord = y + i * height
                self.canvas.create_oval(x_coord-10, y_coord-10, x_coord+10, y_coord+10, fill="pink")
                self.canvas.create_text(x_coord, y_coord, text=str(count))
                count += 1

# Create the main window and run the GUI
root = tk.Tk()
gui = TriangularGridGUI(root)
root.mainloop()


# In[ ]:




