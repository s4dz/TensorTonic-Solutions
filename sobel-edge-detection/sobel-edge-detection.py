import math
def sobel_edges(image):
    """
    Apply the Sobel operator to detect edges.
    """
    H = len(image)
    W = len(image[0])
    pad = [[0] * (W + 2) for _ in range(H + 2)]
    for i in range(H):
        for j in range(W):
            pad[i + 1][j + 1] = image[i][j]
    output = [[0] * W for _ in range(H)]
    Kx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    Ky = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    for i in range(H):
        for j in range(W):
            val_x = 0
            val_y = 0
            for m in range(3):
                for n in range(3):
                    pixel = pad[i + m][j + n]
                    val_x += pixel * Kx[m][n]
                    val_y += pixel * Ky[m][n]
                    
            output[i][j] = math.sqrt(val_x ** 2 + val_y ** 2)

    return output
            