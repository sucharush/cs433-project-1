import numpy as np
from impl.util.utils import sigmoid

def f1_score(y_true, y_pred):
    """Compute the F1-score."""
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    precision = tp / (tp + fp) if tp + fp > 0 else 0
    recall = tp / (tp + fn) if tp + fn > 0 else 0
    return 2 * (precision * recall) / (precision + recall) if precision + recall > 0 else 0


def cross_validate(y, x, w, k_fold: int = 5):
    """
        Performs k-fold cross-validation on the given model using pre-trained weights.

        Args:
        - model: An instance of the logistic regression model.
        - w: Pre-trained weights.
        - k_fold: Number of folds to split the data into.

        Returns:
        - avg_f1: Average F1-score across all folds.
        - avg_accuracy_rate: Average accuracy rate across all folds.
        """
    # Split the dataset into k_fold parts
    fold_size = len(y) // k_fold
    indices = np.random.permutation(len(y))

    f1_scores = []
    accuracy_rates = []

    for fold_start in range(0, len(y), fold_size):
        fold_indices = indices[fold_start:fold_start + fold_size]

        # Splitting data into train and validation sets
        x_validation, y_validation = x[fold_indices], y[fold_indices]  # i.e. tx

        # Predicting on the validation set using weights from trained model
        y_pred_proba = sigmoid(x_validation @ w)
        y_pred = (y_pred_proba > 0.5).astype(int)

        # Calculating f1-score and accuracy rate for this fold
        f1_scores.append(f1_score(y_validation, y_pred))
        accuracy_rates.append(np.mean(y_pred == y_validation))  # Accuracy rate

    # Averaging the scores over all folds
    avg_f1 = np.mean(f1_scores)
    avg_accuracy_rate = np.mean(accuracy_rates)

    return avg_f1, avg_accuracy_rate
