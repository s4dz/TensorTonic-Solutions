import numpy as np

def roc_curve(y_true, y_score):
    """
    Compute ROC curve from binary labels and scores.
    """
    y_true = np.array(y_true)
    y_score = np.array(y_score)
    desc_indices = np.argsort(y_score)[::-1]
    y_score = y_score[desc_indices]
    y_true = y_true[desc_indices]
    distinct_value_indices = np.where(np.diff(y_score))[0]
    threshold_indices = np.r_[distinct_value_indices, y_true.size - 1]
    tps = np.cumsum(y_true)[threshold_indices]
    fps = (1 + threshold_indices) - tps
    total_pos = tps[-1]
    total_neg = fps[-1]
    tpr = tps / total_pos if total_pos > 0 else np.zeros_like(tps)
    fpr = fps / total_neg if total_neg > 0 else np.zeros_like(fps)
    tpr = np.r_[0, tpr]
    fpr = np.r_[0, fpr]
    thresholds = np.r_[np.inf, y_score[threshold_indices]]
    return fpr, tpr, thresholds