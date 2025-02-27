import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import random
import time

def row_col(p):
    row = 1
    col = 1
    while p >= row + col:
        col += row
        row += 1
    return row, p - col

def triangle(points):
    row = [row_col(p)[0] for p in points]
    col = [row_col(p)[1] for p in points]
    if row[0] == row[1]:
        length = col[1] - col[0]
        return col[2] == col[1] and row[2] == row[1] + length
    else:
        length = row[1] - row[0]
        return col[0] == col[1] and row[2] == row[1] and col[2] == col[1] + length

def parallelogram(points):
    row = [row_col(p)[0] for p in points]
    col = [row_col(p)[1] for p in points]
    length = col[1] - col[0]
    return (
        row[2] == row[3]
        and col[3] - col[2] == length
        and row[2] - row[0] == length
        and (col[2] == col[0] or col[2] == col[1])
    )

def hexagon(points):
    row = [row_col(p)[0] for p in points]
    col = [row_col(p)[1] for p in points]
    length = col[1] - col[0]
    return (
        row[0] == row[1]
        and col[2] == col[0]
        and row[2] == row[0] + length
        and col[3] == col[1] + length
        and row[3] == row[2]
        and col[4] == col[1]
        and row[4] == row[2] + length
        and col[5] == col[3]
        and row[5] == row[4]
    )

def draw_grid():
    size = 15
    side = 60
    height = side * sqrt(3) / 2
    fig, ax = plt.subplots()
    ax.set_xlim(0, size * side)
    ax.set_ylim(size * height, 0)  # Invert the Y-axis to match expected layout
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    
    number = 1
    for i in range(size):
        for j in range(i + 1):
            x_coord = j * side + (size - i) * side / 2
            y_coord = i * height + side / 2
            ax.add_patch(plt.Circle((x_coord, y_coord), 20, color='white', ec='black'))  # Increased circle size
            ax.text(x_coord, y_coord, str(number), ha='center', va='center', fontsize=12)
            number += 1
    
    st.pyplot(fig)

def create_sad_emoji():
    st.error("Sorry, no acceptable figure can be formed.")
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.add_patch(plt.Circle((5, 5), 4, color='yellow', ec='black'))
    ax.add_patch(plt.Circle((4, 6), 0.5, color='black'))
    ax.add_patch(plt.Circle((6, 6), 0.5, color='black'))
    ax.plot([3.5, 6.5], [3, 3], color='black', linewidth=3)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    st.pyplot(fig)

def draw_shape(ax, vertices, color='blue'):
    polygon = plt.Polygon(vertices, closed=True, edgecolor='black', facecolor=color, linewidth=2)
    ax.add_patch(polygon)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.axis('off')

def shape(points):
    fig, ax = plt.subplots()
    if len(points) == 3 and triangle(points):
        st.success("The given points form a Triangle!")
        tri = np.array([[0, 1], [-1, -1], [1, -1]])
        draw_shape(ax, tri, color='lightblue')
        st.pyplot(fig)
    elif len(points) == 4 and parallelogram(points):
        st.success("The given points form a Parallelogram!")
        parallel = np.array([[-1, -1], [1, -1], [1.5, 1], [-0.5, 1]])
        draw_shape(ax, parallel, color='lightblue')
        st.pyplot(fig)
    elif len(points) == 6 and hexagon(points):
        st.success("The given points form a Hexagon!")
        hexa = np.array([[np.cos(theta), np.sin(theta)] for theta in np.linspace(0, 2*np.pi, 7)])
        draw_shape(ax, hexa, color='lightblue')
        st.pyplot(fig)
    else:
        create_sad_emoji()

def main():
    st.title("Triangular Grid Shape Detection")
    draw_grid()
    points_input = st.text_input("Enter space-separated points:")
    
    if st.button("Process"):
        points = list(map(int, points_input.split()))
        shape(points)

if __name__ == "__main__":
    main()
