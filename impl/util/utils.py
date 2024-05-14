import numpy as np


def mse_loss(y_pred, y_true):
    return np.mean((y_true - y_pred) ** 2) / 2


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


def logistic_loss(y_pred, y_true):
    return np.sum(- y_true.T @ (np.log(y_pred)) - (1 - y_true).T @ (np.log(1 - y_pred))) / len(y_pred)
