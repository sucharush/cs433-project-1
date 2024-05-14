from abc import abstractmethod

import numpy as np


class BaseMethod:
    def __init__(self,
                 max_iters: int,
                 gamma: float,
                 lambda_: float = 0.0,
                 initial_w: np.ndarray = None,
                 bias: bool = False,
                 verbose: bool = False):

        self.max_iters = max_iters
        self.gamma = gamma
        self.lambda_ = lambda_
        self.bias = bias
        self.bias_flag = False
        self.w = initial_w
        self.verbose = verbose

    def _initial_weight(self):

        self.w = np.random.normal(0, 1, size=self.x.shape[1])

        if self.bias:
            self.w = np.append(self.w, 0)

    @abstractmethod
    def predict(self, x: np.ndarray) -> np.ndarray:
        """Compute the prediction for the input data matrix"""

    @abstractmethod
    def get_gradient(self,
                     w: np.ndarray, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        """Get the gradient value for the input weight matrix"""

    @abstractmethod
    def fit(self, x, y) -> None:
        if self.w is None:
            self.w = np.random.normal(0, 1, size=x.shape[1])
        if self.bias:
            x = np.column_stack((x, np.ones(x.shape[0])))
            if not self.bias_flag:
                self.w = np.append(self.w, 0.)
                self.bias_flag = True
        for i in range(self.max_iters):
            grad = self.get_gradient(self.w, x, y)
            self.w -= self.gamma * grad
            if self.verbose:
                print(f'Epoch {i}: loss: {self.get_loss(self.w)}')

    def get_weights(self):
        return self.w
