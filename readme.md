SEAM CARVING IMAGE RESIZING

This repository implements a Seam Carving algorithm for content-aware image resizing. The goal of this algorithm is to reduce while preserving important content (such as objects and structures) by removing less important regions based on energy values. 

The process involves removing vertical or horizontal seams (paths of minimal energy) iteratively until the target size is reached (i.e It takes an image, target width, and target height as inputs and generates a resized image with the same content but reduced size.)



FEATURES ---------->

    Content-Aware Resizing: Downscaling the image dimensions while preserving important content.

    Dynamic Masking: Protecting specified regions of the image from being resized.

    Shaking Wavy Line: Visual effect added to the seam removal process to simulate a shaking effect.

    GIF Creation: The transformation process is visualized by generating a GIF of the seam carving steps.


    
REQUIREMENTS ---------->

Ensure you have Python 3.x installed, along with the necessary dependencies:

    - numpy
    - opencv-python
    - Pillow

You can install the required libraries by running:
pip install numpy opencv-python pillow



PROJECT STRUCTURE ---------->

The project consists of several Python scripts:

    main.py: 
    The entry point for our algorithm. 
        Loads an image
        Sets the target dimensions
        Runs the seam carving process

    energy.py: 
    Contains the energy calculation function, which evaluates pixel gradients in the image to determine the importance of each region.
    
    seam_carving.py: Implements the seam carving algorithm itself, including functions 
        For removing vertical SEAMS
        For removing horizontal seams
        Applying the shaking wavy line effect
        Saving the result as a GIF.

    seam_utils.py: Includes utility functions for finding and removing seams from the image.



USAGE ---------->

    ৹ Place an image file (e.g., image.jpg) in the project folder.
    ৹ Open main.py and modify the image_path, target_width, and target_height parameters according to your requirements.
    ৹ Run the program:
        python main.py

This will generate the resized image and a GIF showing the seam carving process.




EXAMPLES ---------->

The program has been tested on various images and has produced satisfactory results. The resized images preserve the content and aspect ratio of the original images.

For example; if you want to resize an image to a target width of 500px and a height of 320px, simply set these values in main.py.

    target_width = 500
    target_height = 320

The program will output the resized image and a GIF of the seam removal steps.

NOTE:

    ৹ The program includes a protected region in the center of the image   
      (defined by the rectangle in main.py). 
    ৹ This area will be preserved during the seam carving process.
    ৹ A visual shaking wavy line effect is added during seam removal to enhance the transformation animation.




CODE REFERENCE

1. Avidan, S., & Shamir, A. (2007). Seam carving for content-aware image resizing. ACM Transactions on Graphics (TOG), 26(3), 10.
2. OpenCV Library. (n.d.). Retrieved from (https://sourceforge.net/projects/opencvlibrary/)
