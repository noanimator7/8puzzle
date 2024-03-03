import numpy as np
import matplotlib.pyplot as plt
import imageio
import cv2

def plot_matrix(matrices, goal, output_file='E:/ai1/puzzle_animation.gif', delay=2000):
    images = [] 
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    height = len(matrices[0]) * 50
    width = len(matrices[0][0]) * 50
    for matrix in matrices:
        img = np.zeros((height, width, 3), np.uint8)
        img.fill(255)  
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    text = str(matrix[i][j])
                    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
                    text_width = text_size[0]
                    text_height = text_size[1]
                    text_x = j * 50 + (50 - text_width) // 2
                    text_y = i * 50 + (50 + text_height) // 2
                    cv2.putText(img, text, (text_x, text_y), font, font_scale, (0, 0, 0), font_thickness)

        images.append(img)

    if matrix == goal:
        green_bg = np.ones((height, width, 3), np.uint8) * 255  # Fill with white background
        green_bg[:, :] = (0, 255, 0)  # Set color to green
        images.append(green_bg)
    else:
        red_bg = np.ones((height, width, 3), np.uint8) * 255  # Fill with white background
        red_bg[:, :] = (255, 0, 0)  # Set color to red
        images.append(red_bg)

    # Save images as a GIF
    imageio.mimsave(output_file, images, duration=delay)# # Example usage:


