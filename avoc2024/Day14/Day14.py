import os
import subprocess
import time
from collections import Counter

import pandas
import pyautogui
from PIL import Image, ImageDraw, ImageFont


def part_one(input, seconds, width,height):
    if input is None:
        input = 'resources/input.txt'
    total=1
    with open(input, 'r') as file:
        lines = file.readlines()
        quadrants = Counter()
        # q1 = [(0,0),(4,2)]
        # q2 = [(6,0),(10,2)]
        # q3 = [(0,4),(4,6)]
        # q4 = [(6,6),(10,6)]
        q1 = [(0, 0), (width//2-1, height//2-1)]
        q2 = [(width//2+1, 0), (width, height//2-1)]
        q3 = [(0, height//2+1), (width//2-1, height)]
        q4 = [(width//2+1, height//2+1), (width, height)]
        for second in range(8157,seconds):
            coordinates = [[0 for _ in range(width + 1)] for _ in range(height + 1)]
            for line in lines:
                pos = line.split(" ")[0]
                move = line.split(" ")[1]
                x = int(pos.strip("p=").split(",")[0])
                y = int(pos.strip("p=").split(",")[1])
                dx = int(move.strip("v=").split(",")[0])
                dy = int(move.strip("v=").split(",")[1])
                for _ in range(second):
                    x = x + dx
                    y = y + dy
                    if x>width:
                        x = x-width-1
                    if x<0:
                        x = width + x +1
                    if y>height:
                        y = y-height-1
                    if y<0:
                        y = height + y+1
                coordinates[y][x] += 1
            save_grid_as_image(coordinates, "resources/pic" + str(second) + ".png")

                # checkQuadrant(q1, quadrants, x, y)
                # checkQuadrant(q2, quadrants, x, y)
                # checkQuadrant(q3, quadrants, x, y)
                # checkQuadrant(q4, quadrants, x, y)

            # for i in quadrants.values():
            #     total*=i
    return total

def save_grid_as_image(grid, output_file):
    """Render the grid to an image and save it."""
    cell_width = 20
    cell_height = 20
    font_size = 12
    padding = 10

    # Compute image dimensions
    img_width = cell_width * len(grid[0]) + 2 * padding
    img_height = cell_height * len(grid) + 2 * padding


    # Create a blank image
    image = Image.new("RGB", (img_width, img_height), "black")
    draw = ImageDraw.Draw(image)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()  # Use default if font file is not available

    # Draw the grid text on the image
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == 0:
                x = col_idx * cell_width + padding
                y = row_idx * cell_height + padding
                draw.text((x, y), ".", fill="black", font=font)
            else:
                x = col_idx * cell_width + padding
                y = row_idx * cell_height + padding
                x1 = x + cell_width
                y1 = y + cell_height

                # Draw cell background
                cell_color = "green"
                draw.rectangle([x, y, x1, y1], fill=cell_color, outline="black")
                draw.text((x, y), "X", fill="green",background="green", font=font)
    # Save the image
    image.save(output_file)


def checkQuadrant(q, quadrants, x, y):
    if x >= q[0][0] and x <= (q[1][0]):
        if y >= q[0][1] and y <= (q[1][1]):
            quadrants[q[0]] = quadrants.get(q[0], 0) + 1

def open_terminal_and_show_file(temp_file_path):
    """Open the temporary file in a new terminal and wait for rendering."""
    if os.name == 'posix':  # Linux/Unix/Mac
        # Use xterm or another terminal emulator
        subprocess.Popen(["xterm", "-hold", "-e", f"cat {temp_file_path}"])
    elif os.name == 'nt':  # Windows
        # Use `start` to run a command in a new cmd window
        subprocess.Popen(f'start cmd /k "cd resources && type {temp_file_path}"', shell=True)
    time.sleep(3)

def take_screenshot(output_file):
    """Take a screenshot of the terminal."""
    time.sleep(2)  # Ensure the terminal has focus
    screenshot = pyautogui.screenshot()
    screenshot.save(output_file)

part_one(None,8160,100,102)

