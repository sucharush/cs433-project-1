import pytest
import numpy as np
from impl.method.gardient_desent import MeanSquaredErrorGD
from impl.method.logistic_regression import LogisticRegression
from impl.util.utils import mse_loss, logistic_loss

X = np.array([[2.3, 3.2], [1.0, 0.1], [1.4, 2.3]])
Y = np.array([0., 1., 1.])
INITIAL_W = np.array([0.5, 1.])


@pytest.mark.parametrize('module_cls, expected_loss, loss_fn',
                         [(MeanSquaredErrorGD, 0.3545193842178323, mse_loss),
                          (LogisticRegression, 1.3425153104769987, logistic_loss)])
def test_bias(module_cls, expected_loss, loss_fn):

    runner = module_cls(max_iters=2, gamma=0.1,
                        initial_w=INITIAL_W, bias=True)
    # runner.set_bias(0.)
    runner.fit(X, Y)
    loss = loss_fn(runner.predict(np.column_stack([X, np.ones(X.shape[0])])),
                   Y)
    assert np.allclose(loss, expected_loss)
