import numpy as np

from impl.method.base_method import BaseMethod


class MeanSquaredErrorGD(BaseMethod):
    """Mean squared error loss with gardient desent algorithm.

    Attributes:
        y (numpy.ndarray): the target variable, a numpy array with the shape
        of (N_samples)
        tx (numpy.ndarray): the input variable, a numpy array with the shape
        of (N_samples, N_features)
        array with the shape of (N_features)
        max_iters (int): maximum number of iterations
        gamma (float): the learning rate
        lambda_ (float): L2 regularization term
        inital_w (numpy.ndarray): the initial value of weight matrix, a numpy
        bias (bool): if True, add a bias term weights
        verbose (bool): if True, print the weight and the loss when running"""

    def get_gradient(self, w, x, y) -> np.ndarray:
        """Get the gradient for the input weight matrix

        Args:
            w (numpy.ndarray): the value of weight matrix, a numpy array with
            the shape of (N_features, 1)

        Returns:
            grad (numpy.ndarry): the gradient, a numpy array with the shape of
            (N_features, 1)
        """
        if x.ndim == 1:
            x = x.reshape(1, x.shape[0])

        n = y.shape[0] if y.shape else 1
        grad = -x.T @ (y - self.predict(x)) / n

        return grad

    def predict(self, x: np.ndarray) -> np.ndarray:
        return x @ self.w
