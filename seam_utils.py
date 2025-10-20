import numpy as np

def find_vertical_seam(energy):
    rows, cols = energy.shape
    seam = np.zeros(rows, dtype=int)
    cumulative_energy = np.copy(energy)

    for i in range(1, rows):
        for j in range(cols):
            left = cumulative_energy[i-1, j-1] if j > 0 else float('inf')
            up = cumulative_energy[i-1, j]
            right = cumulative_energy[i-1, j+1] if j < cols-1 else float('inf')
            cumulative_energy[i, j] += min(left, up, right)

    seam[-1] = np.argmin(cumulative_energy[-1])
    for i in range(rows-2, -1, -1):
        j = seam[i+1]
        left = cumulative_energy[i, j-1] if j > 0 else float('inf')
        up = cumulative_energy[i, j]
        right = cumulative_energy[i, j+1] if j < cols-1 else float('inf')
        if min(left, up, right) == left:
            seam[i] = j-1
        elif min(left, up, right) == right:
            seam[i] = j+1
        else:
            seam[i] = j
    return seam

def remove_vertical_seam(image, seam):
    if len(image.shape) == 3:
        rows, cols, channels = image.shape
        new_image = np.zeros((rows, cols - 1, channels), dtype=image.dtype)

        for i in range(rows):
            j = seam[i]
            new_image[i, :, :] = np.delete(image[i, :, :], j, axis=0)

    elif len(image.shape) == 2:
        rows, cols = image.shape
        new_image = np.zeros((rows, cols - 1), dtype=image.dtype)

        for i in range(rows):
            j = seam[i]
            new_image[i, :] = np.delete(image[i, :], j, axis=0)

    return new_image