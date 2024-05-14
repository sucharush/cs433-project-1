import numpy as np

from impl.method.base_method import BaseMethod
from impl.util.utils import sigmoid


class LogisticRegression(BaseMethod):
    """Regularized logistic regression using gradient descent.

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

    def __init__(self, sgd=False, batch_size=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sgd = sgd
        self.batch_size = batch_size

    def get_gradient(self, w, x, y) -> np.ndarray:
        """Get the gradient for the input weight matrix."""
        if self.sgd:
            # for sgd:
            batch_indices = np.random.choice(x.shape[0], self.batch_size, replace=False)
            x = x[batch_indices]
            y = y[batch_indices]

        grad = x.T @ (-(y - self.predict(x))) / len(y)
        l2_grad = 2 * self.lambda_ * w
        if self.bias:
            l2_grad[0] = 0
        return grad + l2_grad

    def predict(self, x: np.ndarray) -> np.ndarray:
        return sigmoid(x @ self.w)
