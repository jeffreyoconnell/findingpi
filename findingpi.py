# This python program will estimate the value of Pi by randomly selecting
# points inside a 2 x 2 square, which has an area of 4) and then determines
# if the points are inside the inscribed circle (area of Pi). The program
# keeps track of the percentage of the points inside the circle and then
# multiplies that by 4 (the area of the square).  As the number of points
# increases, the result should get closer to Pi 🤓 

import matplotlib.pyplot as plt
import numpy as np
import random
import time


def generate_random_point():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    return x, y

def plot_point(x, y, inside_circle):
    color = 'green' if inside_circle else 'red'
    plt.scatter(x, y, color=color, marker='o')

def plot_unit_circle():
    theta = np.linspace(0, 2*np.pi, 100)
    x_circle = np.cos(theta)
    y_circle = np.sin(theta)
    plt.plot(x_circle, y_circle, linestyle='--', color='blue')

def update_plot(points, percentage_inside, num_points_selected):
    plt.title('Randomly Generated Points',fontsize=36)
    plt.xlabel('X-axis',fontsize=18)
    plt.ylabel('Y-axis',fontsize=18)
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.gca().set_aspect('equal', adjustable='box')  # Set aspect ratio to be equal
    plt.grid(True)

    plot_unit_circle()  # Plot the unit circle

    for point, inside_circle in points:
        plot_point(*point, inside_circle)

    # Add labels below the graph
    plt.text(-1, -1.2, f'Total Number of Points: {num_points_selected}', color='blue', fontsize=18)
    plt.text(-1, -1.3, f'Percentage Inside: {percentage_inside:.2f}%', color='blue', fontsize=18)
    plt.text(-1, -1.4, f'Estimate of Pi: {percentage_inside * 4/100:.10f}', color='purple', fontsize=18)

    plt.draw()
    plt.pause(0.1)  # Add a small pause to update the plot

# ...

if __name__ == "__main__":
    plt.ion()  # Turn on interactive mode for live plotting

    points_inside_circle = 0
    total_points = 0
    all_points = []
    num_points_selected = 0

    # Set the figure size
    plt.figure(figsize=(8, 10))

    #Get user input for the number of iterations
    num_interations = int(input("Enter the number of iterations: "))

    for i in range(num_interations):
        random_point = generate_random_point()
        total_points += 1

        inside_circle = random_point[0]**2 + random_point[1]**2 <= 1
        if inside_circle:
            points_inside_circle += 1

        percentage_inside = (points_inside_circle / total_points) * 100

        all_points.append((random_point, inside_circle))
        num_points_selected += 1  # Increment for every point selected
        
        plt.clf()  # Clear the figure
        update_plot(all_points, percentage_inside, num_points_selected)

        #if i % 1000 == 0:
         #  plt.clf()  # Clear the figure
          # update_plot(all_points, percentage_inside, num_points_selected)



    plt.ioff()  # Turn off interactive mode
    plt.show()
