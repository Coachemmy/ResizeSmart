from seam_carving import seam_carving, save_gif
import cv2


def main():
    image_path = 'image2.jpg'
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not loaded.")
        return

    print(f"Original Dimensions: {image.shape[1]}x{image.shape[0]}")

    # target_width = 500
    # target_height = 320

    # middle_x_start = 120
    # middle_x_end = 420
    # middle_y_start = 0
    # middle_y_end = 336

    target_width = 450
    target_height = 420

    middle_x_start = 150
    middle_x_end = 450 
    middle_y_start = 150 
    middle_y_end = 360


    # cv2.line(image, (0, image.shape[0] // 2),
    #          (image.shape[1], image.shape[0] // 2), (255, 0, 0), 2)

    # cv2.line(image, (image.shape[1] // 2, 0),
    #          (image.shape[1] // 2, image.shape[0]), (0, 255, 0), 2)

    # cv2.rectangle(
    #     image,
    #     (middle_x_start, middle_y_start),
    #     (middle_x_end, middle_y_end),
    #     (0, 0, 255),  
    #     2  
    # )

    # cv2.imshow("Original with X, Y Axis and Protected Region", image)
    # cv2.waitKey(0) 

    mask = cv2.imread(image_path, 0)
    mask[:, :] = 0
    mask[middle_y_start:middle_y_end, middle_x_start:middle_x_end] = 255
    print("Starting seam carving...")

    resized_image, removed_seams = seam_carving(image, target_width, target_height, mask)
    
    cv2.imwrite("resized_image2.jpg", resized_image)
    print("Resized image saved.")

    # cv2.imshow("Resized Image", resized_image)
    # cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()