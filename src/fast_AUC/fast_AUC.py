import numpy as np

def auroc(y_true: np.ndarray, y_score: np.ndarray) -> float:
    """Computes the AUC under the ROC curve in O(n log n) time.

    This approach uses the probabilistic definition of AUC and efficiently computes the fraction of pairs of
    one positive and one negative sample that satisfy the property that the positive score is higher than the
    negative score. It does this by pre-sorting the smaller of the two classes and then using binary search to
    efficiently determine how many pairs satisfy the target property.

    Args:
        y_true: The true labels.
        y_score: The predicted scores.

    Returns:
        The AUC under the ROC curve.

    Examples:
        >>> auroc(np.array([0, 1, 1, 0]), np.array([0.1, 0.4, 0.35, 0.8]))
        np.float64(0.5)
        >>> auroc(np.array([0, 1, 0, 1]), np.array([0.1, 0.4, 0.35, 0.8]))
        np.float64(1.0)
    """

    P_pos = y_score[y_true == 1]
    P_neg = y_score[y_true == 0]

    if len(P_neg) < len(P_pos):
      reverse = True
      P_pos, P_neg = P_neg, P_pos
    else:
      reverse = False

    P_neg = np.sort(P_neg)

    pairs_correct = np.searchsorted(P_neg, P_pos, side="right").sum()
    pairs_total = len(P_pos) * len(P_neg)

    auc = pairs_correct / pairs_total
    if reverse:
      auc = 1 - auc
    return auc
