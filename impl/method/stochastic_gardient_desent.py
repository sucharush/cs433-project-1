import numpy as np

from impl.method.gardient_desent import MeanSquaredErrorGD


class MeanSquaredErrorSGD(MeanSquaredErrorGD):

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

    def __init__(self, max_iters: int, gamma: float, lambda_: float = 0.0, initial_w: np.ndarray = None,
                 bias: bool = False, verbose: bool = False, batch_size: int = 100):
        self.batch_size = batch_size
        super().__init__(max_iters, gamma, lambda_, initial_w, bias, verbose)

    def fit(self, x, y):
        for _ in range(self.max_iters):
            i = np.random.randint(0, len(y), size=self.batch_size)
            grad = self.get_gradient(self.w, np.array(x[i]), np.array(y[i]))
            self.w -= self.gamma * grad
            if self.verbose:
                print(f'Epoch {i}: loss: {self.get_loss(self.w)}')
