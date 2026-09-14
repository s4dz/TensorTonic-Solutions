from math import sqrt
def generate_anchors(feature_size: int, image_size: float, scales: list[float], aspect_ratios: list[float]) -> list[list[float]]:
    """
    Returns a list of [x1, y1, x2, y2] anchor boxes.
    """ 
    answer = []
    stride = image_size / feature_size
    for i in range(feature_size):
        for j in range(feature_size):
            cx = (j + 0.5) * stride 
            cy = (i + 0.5) * stride
            for z in range(len(scales)):
                for y in range(len(aspect_ratios)):
                    w = scales[z] * sqrt(aspect_ratios[y])
                    h = scales[z]/sqrt(aspect_ratios[y])
                    box = [cx - w / 2, cy - h/2, cx + w/2, cy + h/2]
                    answer.append(box)
    return answer
    pass