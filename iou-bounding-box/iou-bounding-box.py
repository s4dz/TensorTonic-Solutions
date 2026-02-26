def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    max_x = max(box_a[0], box_b[0])
    min_x = min(box_a[2], box_b[2])
    min_y = min(box_a[3], box_b[3])
    max_y = max(box_a[1], box_b[1])
    aoi = max(0, min_x - max_x) * max(0, min_y - max_y)
    union = ((box_a[2] - box_a[0]) * (box_a[3] - box_a[1])) + (box_b[2] - box_b[0]) * (box_b[3] - box_b[1]) - aoi
    if aoi == 0: return 0
    return aoi / union
    pass