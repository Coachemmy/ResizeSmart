import numpy as np
import cv2
from energy import calculate_energy
from seam_utils import find_vertical_seam, remove_vertical_seam
from PIL import Image
import random
import math


def seam_carving(image, target_width, target_height, mask=None):
    original_height, original_width = image.shape[:2]
    current_height, current_width = image.shape[:2]

    frames = []
    seams = []

    black_canvas = np.zeros(
        (original_height, original_width, 3), dtype=np.uint8)

    while current_width > target_width:
        print(f"Removing vertical seams, width: {current_width}")
        energy = calculate_energy(image)

        if mask is not None:
            energy[mask > 0] += 1e6

        vertical_seam = find_vertical_seam(energy)
        image = remove_vertical_seam(image, vertical_seam)

        canvas = black_canvas.copy()
        canvas[:, :current_width - 1] = image

        wave_amplitude = 10
        wave_frequency = 0.05
        shake_offset = random.randint(-3, 3)
        middle_x = original_width // 2

        for y in range(original_height):
            wave_y = int(math.sin(y * wave_frequency +
                         shake_offset) * wave_amplitude)
            canvas[y, middle_x + wave_y] = [0, 0, 255]
        frames.append(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))

        if mask is not None:
            mask = remove_vertical_seam(mask, vertical_seam)

        seams.append(vertical_seam)
        current_width -= 1

    while current_height > target_height:
        print(f"Removing horizontal seams, height: {current_height}")
        energy = calculate_energy(image)

        if mask is not None:
            energy[mask > 0] += 1e6

        horizontal_seam = find_vertical_seam(energy.T)
        image = remove_vertical_seam(image.transpose(
            1, 0, 2), horizontal_seam).transpose(1, 0, 2)

        canvas = black_canvas.copy()
        canvas[:current_height - 1, :current_width] = image

        wave_amplitude = 10
        wave_frequency = 0.05
        shake_offset = random.randint(-3, 3)
        middle_x = original_width // 2

        for y in range(original_height):
            wave_y = int(math.sin(y * wave_frequency +
                         shake_offset) * wave_amplitude)
            canvas[y, middle_x + wave_y] = [0, 0, 255]
        frames.append(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))

        if mask is not None:
            mask = remove_vertical_seam(mask.T, horizontal_seam).T
            print("Mask before seam removal:")
            print(mask)

        seams.append(horizontal_seam)
        current_height -= 1
    save_gif(frames, "resized_image2.gif")

    return image, seams


def protect_region(energy, box_coordinates):
    x1, y1, x2, y2 = box_coordinates
    protected_energy = 1e6
    energy[y1:y2, x1:x2] += protected_energy
    return energy


def save_gif(frames, gif_path):
    """Save a list of frames as a GIF."""
    pil_images = [Image.fromarray(frame) for frame in frames]
    pil_images[0].save(
        gif_path, save_all=True, append_images=pil_images[1:], duration=200, loop=0
    )
    print(f"GIF saved at {gif_path}")
