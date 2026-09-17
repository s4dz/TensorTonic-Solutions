import numpy as np

def impute_missing(X: list, strategy: str = "mean") -> np.ndarray:
    answer = np.asarray(X, dtype=float)
    if answer.ndim == 1:
        if strategy == "mean":
            rp = np.nanmean(answer)
        else:
            rp = np.nanmedian(answer)

        if np.isnan(rp):
            rp = 0.0
        answer[np.isnan(answer)] = rp
        return answer
    if strategy == "mean":
        rp = np.nanmean(answer, axis=0)
    else:
        rp = np.nanmedian(answer, axis=0)
    rp = np.where(np.isnan(rp), 0.0, rp)
    inds = np.isnan(answer)
    answer[inds] = rp[np.where(inds)[1]]
    return answer