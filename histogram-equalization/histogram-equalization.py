import numpy as np
def histogram_equalize(image):
    """
    Apply histogram equalization to enhance image contrast.
    """
    image = np.array(image)
    H, W = image.shape
    histogram = np.zeros(256)
    for i in range(H):
        for j in range(W):
            histogram[image[i, j]] += 1
    cdf = np.zeros(256)
    cdf_min = 1e9
    cdf[0] = histogram[0]
    if cdf[0] > 0:
        cdf_min = cdf[0]
    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + histogram[i]
        if cdf[i] > 0 and cdf[i] < cdf_min:
            cdf_min = cdf[i]
    denominator = (H * W) - cdf_min
    if denominator > 0:
        for i in range(H):
            for j in range(W):
                image[i, j] = round((cdf[image[i, j]] - cdf_min) / denominator * 255)
    else:
        for i in range(H):
            for j in range(W):
                image[i, j] = 0
                
    return image.tolist()