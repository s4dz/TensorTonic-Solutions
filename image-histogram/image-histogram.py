import numpy as np
def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    output = np.zeros(256)
    image = np.array(image)
    H, W = image.shape
    for i in range(H):
        for j in range(W):
            output[image[i, j]]+=1
    
    return output.tolist()