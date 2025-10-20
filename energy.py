import numpy as np
import cv2


def calculate_energy(image):
    print("Calculating energy...")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    energy = np.abs(grad_x) + np.abs(grad_y)
    return energy


def update_energy_map(energy, image, seam, direction='vertical'):
    rows, cols = image.shape[:2]
    if direction == 'vertical':
        for i, j in enumerate(seam):
            for col in range(max(0, j - 1), min(j + 2, cols - 1)):
                if col < cols:
                    energy[i, col] = calculate_energy(
                        image[i:i+1, col:col+1])[0, 0]
    return energy
