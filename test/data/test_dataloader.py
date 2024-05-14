from numpy import allclose, array, copy, nan
from impl.data.dataloader import DataLoader

EXPECTED_DATA00 = \
    array([2.000e+00, 2.000e+00, 3.000e+00,
           1.000e+00, 1.000e+00, 1.000e+00, 1.000e+00, 1.000e+00, 1.000e+00,
           1.000e+00, 3.000e+00, 2.000e+00, 1.000e+00, 1.000e+00, 2.000e+00,
           1.000e+00, 1.000e+00, 1.000e+00, 1.000e+00, 8.000e+00, 1.000e+00,
           5.700e+01, 5.000e+00, 6.100e+01, 1.550e+00, 4.990e+01, 2.078e+01,
           2.000e+00, 1.000e+00, 1.000e+00, 3.000e+00, 5.000e+00, 1.000e+00,
           2.000e+00, 2.000e+00, 0.000e+00, 1.000e+00, 0.000e+00, 1.000e+00,
           0.000e+00, 7.100e-01, 1.300e-01, 1.000e-01, 2.700e-01, 7.100e-01,
           0.000e+00, 0.000e+00, 1.000e+00, 1.000e+00, 7.100e-01, 1.210e+00,
           2.000e+00, 1.000e+00, 1.000e+00, 1.000e+00, 0.000e+00, 0.000e+00,
           1.000e+00, 3.500e+00, 4.500e+00, 2.691e+01, 4.610e+00, 1.000e+00,
           1.000e+00, 3.000e+01, 3.000e+01, 2.000e+00, 4.667e+00, 6.000e+01,
           1.400e+02, 5.000e+00, 0.000e+00, 6.000e+01, 1.400e+02, 2.000e+02,
           0.000e+00, 0.000e+00, 0.000e+00, 2.000e+00, 1.000e+00, 1.000e+00,
           2.000e+00, 2.000e+00, 1.000e+00, 1.000e+00, 1.000e+00, 3.000e+00,
           3.000e+00, 4.000e+00, 1.000e+00, 1.000e+00,       nan,       nan,
           2.000e+00, 0])
EXPECTED_AGEG5YR = \
    array([-0.94702745, -0.94702745, -0.09470274, -0.09470274,  1.60994666,
           -0.94702745,  1.18378431,  1.18378431, -0.94702745])
EXPECTED_LMTSCL1 = \
    array([1., 1., 0.5, 0.5, 1., 1., 0., 0., 1.])


def test_load_data(set_global_data):

    data = DataLoader('data/x_train_small.csv', 'data/y_train_small.csv')
    assert len(data) == 9
    assert len(data.column) == 95
    print(data[0])
    assert allclose(data[0], EXPECTED_DATA00, equal_nan=True)
    set_global_data('data', data)


def test_preprocessing(get_global_data):

    data = get_global_data('data')
    original_x = copy(data.data)
    data.standardize(['_AGEG5YR'])
    data.normalize(['_LMTSCL1'])
    processed_idx = [data._name2column[name]
                     for name in ['_AGEG5YR', '_LMTSCL1']]
    for i in range(len(data.column)):
        if i not in processed_idx:
            assert allclose(original_x[:, i], data.data[:, i], equal_nan=True)
    assert allclose(data['_AGEG5YR'], EXPECTED_AGEG5YR)
    assert allclose(data['_LMTSCL1'], EXPECTED_LMTSCL1)


def test_split(get_global_data):

    data = get_global_data('data')
    result = data.split(batch_size=5)
    assert len(result) == 2
    assert result[0].data.shape == (5, data.data.shape[1])
    assert len(result[1]) == 4

    result = data.split(n_batch=3)
    assert len(result) == 3
    assert result[0].data.shape == (3, data.data.shape[1])
    assert len(result[1]) == 3
    assert len(result[2]) == 3
