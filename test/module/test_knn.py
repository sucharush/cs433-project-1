import numpy as np
from impl.util.knn import KNNDataImputer

X = [[1, 2, np.nan],
     [3, 4, 3],
     [np.nan, 6, 5],
     [8, 8, 7]]
EXPECTED_X = [[1., 2., 5.],
              [3., 4., 3.],
              [5.5, 6., 5.],
              [8., 8., 7.]]


def test_knn():

    feature_categories = ['Continues' for i in range(3)]
    imp = KNNDataImputer(k=2,
                         feature_categories=feature_categories)
    assert np.allclose(imp.run(X), EXPECTED_X)
