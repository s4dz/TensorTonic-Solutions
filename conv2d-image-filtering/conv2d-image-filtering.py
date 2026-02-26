import numpy as np
def conv2d(image, kernel, stride=1, padding=0):
    """
    Apply 2D convolution to a single-channel image.
    """
    image = np.array(image)
    kernel = np.array(kernel)
    H, W = image.shape
    kH, kW = kernel.shape
    Hout = int(((H + 2 * padding - kH) // stride) + 1)
    Wout = int(((W + 2 * padding - kW) // stride) + 1)
    image = np.array(image)
    output = np.zeros((Hout, Wout))
    pad_image = np.pad(image, pad_width = padding, mode = 'constant', constant_values = 0)
    for i in range(Hout):
        for j in range(Wout):
            for m in range(kH):
                for n in range(kW):
                    output[i, j] += pad_image[i * stride + m, j * stride + n] * kernel[n, m]
    return output.tolist()
    pass