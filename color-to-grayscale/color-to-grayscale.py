def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    H = len(image)
    W = len(image[0])
    grayscale = [[0.0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            r = image[i][j][0]
            g = image[i][j][1]
            b = image[i][j][2]
            grayscale[i][j] = 0.299 * r + 0.587 * g + 0.114 * b
        
    return grayscale