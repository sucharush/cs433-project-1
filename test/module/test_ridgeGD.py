import pytest
import numpy as np
from impl.method.ridge_regression import RidgeRegressionGD
from impl.method.base_method import *


def test_ridge_regression_second_iteration():
    # Define a specific dataset.
    x = np.array([
        [1, 2],
        [2, 3],
        [3, 4],
        [4, 5]
    ])
    y = np.array([5, 7, 9, 11])
    gamma = 0.1
    lambda_ = 0.1
    initial_w = np.array([0.5, 0.5])
    max_iters = 2

    # Create the RidgeRegressionGD object.
    ridge = RidgeRegressionGD(max_iters=max_iters, gamma=gamma, lambda_=lambda_, initial_w=initial_w)

    # Fit the model.
    ridge.fit(x, y)

    # Check the weights after the first iteration.
    expected_w = np.array([0.3288, 0.3268])
    np.testing.assert_array_almost_equal(ridge.get_weights(), expected_w, decimal=5)

