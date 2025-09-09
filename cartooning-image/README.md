- Python Library: OpenCV
- Cartooning an image turns a normal photo into a fun, animated-style picture. With OpenCV, I do this by smoothing the image to simplify colors and detecting edges to create outlines. Combining these steps makes the photo look like a cartoon.
- Steps:
    + Read the input image.
    + Convert the image to grayscale for edge detection.
    + Apply median blur to remove noise.
    + Use adaptive thresholding to detect edges.
    + Apply a bilateral filter to smooth the image while preserving edges.
    + Combine the smoothed image with edges to produce the cartoon effect.