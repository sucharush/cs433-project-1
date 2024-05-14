import numpy as np

from impl.method.base_method import BaseMethod


class RidgeRegressionGD(BaseMethod):
    """Linear regression model with gradient descent optimization.

    Attributes:
        y (numpy.ndarray): the target variable, a numpy array with the shape of (N_samples)
        tx (numpy.ndarray): the input variable, a numpy array with the shape of (N_samples, N_features)
        max_iters (int): maximum number of iterations
        gamma (float): the learning rate
        inital_w (numpy.ndarray): the initial value of weight matrix, a numpy array with the shape of (N_features)
        bias (bool): if True, add a bias term weights
        verbose (bool): if True, print the weight and the loss when running
    """
    def __init__(self, sgd=False, batch_size=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sgd = sgd
        self.batch_size = batch_size

    def get_gradient(self, w, x, y) -> np.ndarray:
        """Get the gradient for the input weight matrix"""
        if self.sgd:
            batch_indices = np.random.choice(x.shape[0], self.batch_size, replace=False)
            x = x[batch_indices]
            y = y[batch_indices]

        if x.ndim == 1:
            x = x.reshape(1, x.shape[0])

        n = y.shape[0] if y.shape else 1
        grad = -x.T @ (y - self.predict(x)) / n
        # L2 regularization
        grad += self.lambda_ * w
        return grad

    def predict(self, x: np.ndarray) -> np.ndarray:
        """Compute the prediction for the input data matrix"""
        return x @ self.w

    def get_loss(self, w) -> float:
        """Compute the loss for the current weight matrix"""
        e = self.y - self.predict(self.tx)
        mse = 0.5 * np.mean(e**2) + self.lambda_ * np.sum(w**2)
        return mse
    

   