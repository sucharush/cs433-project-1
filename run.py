import random

import numpy as np

from helpers import create_csv_submission
from impl.data.dataloader import DataLoader
from impl.data.define import DELETE_FEATURE, TREAT_NAN, ONEHOT
from impl.method.logistic_regression import LogisticRegression

X_CSV = 'data/x_train.csv'
Y_CSV = 'data/y_train.csv'
TEST_X_CSV = 'data/x_test.csv'
TRAIN_SIZE = 0.9

NAN_NUM = 0


def data_preprocessing(data, type='val', use_knn=False):
    for feature in DELETE_FEATURE:
        data.delete_column(feature)

    #for feature in set(TREAT_NAN.keys()).intersection(data.column):
    #    data_col = data[feature]
    #    for key, value in TREAT_NAN[feature].items():
    #        if not np.isnan(key):
    #            data_col[data_col == key] = np.nan


    # remove nan
    #if type == 'train':
    #    idx = np.where(np.sum(np.isnan(data), axis=1) <= NAN_NUM)
    #    data.data = data.data[idx]

    # process
    if use_knn:
        category = [FEATURE_CATEGORIES[feature] 
                    for feature in data.column if feature != 'label']
        imputer = KNNDataImputer(3, feature_categories=category)
        if 'label' in data.column:
            data.data[:, :-1] = imputer.run(data.data[:, :-1])
        else:
            data.data = imputer.run(data.data)
        return data
    
    #for feature in data.column:
    #    data[feature][np.isnan(data[feature])] = np.nanmean(data[feature])
    for feature in set(TREAT_NAN.keys()).intersection(data.column):
        data_col = data[feature]
        for key, value in TREAT_NAN[feature].items():
            if isinstance(key, int):
                to_replace = data_col == key
            elif isinstance(key, float) and np.isnan(key):
                to_replace = np.isnan(data_col)
            elif key[0] == '>':
                threshold = eval(key[1:])
                to_replace = data_col > threshold
            elif key[0] == '<':
                threshold = eval(key[1:])
                to_replace = data_col < threshold
            else:
                raise NotImplementedError(
                    f'not implemented {feature} {TREAT_NAN[feature][key]}')
            
            if isinstance(value, int):
                data_col[to_replace] = value
            elif value == 'avg':
                data_col[to_replace] = np.nanmean(data_col)
            elif value == 'ALCDAY5<':
                data_col[to_replace] -= 100
                data_col[to_replace][data_col[to_replace] > 7] = 7
                data_col[to_replace] *= 4
            elif value == 'ALCDAY5>':
                data_col[to_replace] -= 200
                data_col[to_replace][data_col[to_replace] > 30] = 30
            else:
                raise NotImplementedError(
                    f'not implemented {feature} {value} {TREAT_NAN[feature][key]}')

    # onehot
    for feature in set(ONEHOT.keys()).intersection(data.column):
        data_col = data[feature]
        col_idx = data._name2column[feature]
        hots = set(data[feature])
        # hot size
        size = len(hots)
        # new zero array
        map = np.zeros((data_col.shape[0], size))
        for i, hot in enumerate(hots):
            ids = np.where(data_col == hot)
            if len(ids) == 0: continue
            map[:, i][ids] = 1
        data.data[:, col_idx] = map[:, 0]
        data.data = np.concatenate((data.data[:, :col_idx], map[:, 1:], data.data[:, col_idx:]), axis=1)

        map_col = []
        data.column[col_idx] = feature + "0"
        for i in range(1, size):
            map_col.append(feature + str(i))
        data.column = np.concatenate((data.column[:col_idx], map_col, data.column[col_idx:]), axis=0)
        data._name2column = {name: i for i, name in enumerate(data.column)}

    return data

def get_preprocess_option(data):

    to_normalize = []
    to_standardize = []
    for column in data.column:
        if column == "label": continue  # not include label
        if np.average(data[column]) > 10: 
            to_standardize.append(column)
        else: 
            to_normalize.append(column)

    return to_normalize, to_standardize


def cosine_annealing(T_cur, lr_max, lr_min, T_max):
    if T_cur / T_max - 1 // 2 != 0:
        return lr_min / 2 + 1 / 2 * (lr_max - lr_min) * (1 + np.cos(np.pi * T_cur / T_max))
    else:
        return lr_min / 2 + 1 / 2 * (lr_max - lr_min) * (1 - np.cos(np.pi * 1 / T_max))


if __name__ == '__main__':
    # Fix seeds
    np.random.seed(0)
    random.seed(0)

    # load data
    data = DataLoader(X_CSV, Y_CSV, ratio_missing=0.6)
    # train, test = data.split(0.8)
    train = data

    # process
    train = data_preprocessing(train, type='train', use_knn=False)
    #to_normalize, to_standardize = get_preprocess_option(train)

    # train
    train.normalize(train.column[:-1])  # not include label

    n_positive = int(np.sum(train.data[:, -1] == 1) * 0.05)
    n_negative = int(1.8 * n_positive)
    i_positive = np.concatenate(np.argwhere(train.data[:, -1] == 1))
    i_negative = np.concatenate(np.argwhere(train.data[:, -1] == 0))

    lr = 1e-2
    lambda_ = 1e-15
    max_iter = 150500
    lr_max = 1e-2
    lr_min = 1e-6

    sample = np.concatenate([np.random.choice(i_positive, n_positive),
                             np.random.choice(i_negative, n_negative)])
    model = LogisticRegression(1, lr, lambda_=lambda_, bias=False)
    model.fit(train.data[sample, :-1], train.data[sample, -1])
    w = model.get_weights()

    for i in range(max_iter):
        lr = cosine_annealing(i, lr_max, lr_min, 1000)
        sample = np.concatenate([np.random.choice(i_positive, n_positive),
                                 np.random.choice(i_negative, n_negative)])
        model = LogisticRegression(1, lr, lambda_=lambda_,
                                   bias=False, initial_w=w)
        model.fit(train.data[sample, :-1], train.data[sample, -1])
        w = model.get_weights()

    # inference
    testset = DataLoader(TEST_X_CSV, ratio_missing=0.6)
    testset = data_preprocessing(testset)
    testset.normalize(testset.column[:-1])
    result = model.predict(testset.data)
    result[result >= 0.5] = 1
    result[result < 0.5] = -1
    ids = list(range(328135, 437514))
    create_csv_submission(ids, result, 'result.csv')
