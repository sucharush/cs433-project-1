[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/U9FTc9i_)

# EPFL Machine Learning (CS433) Project 1

In this project, we are given a dataset containing features from the Behavioral Risk Factor Surveillance System (BRFSS)
to build a model to predict a personal situation will lead to MICHD or not.
To achieve this, we initially preprocess the data and build Machine Learning model to train.
We implement six
functions `mean_squared_error_gd` `mean_squared_error_sgd` `least_squares` `ridge_regression` `logistic_regression` `reg_logistic_regression`
in the `implementations.py` to test the performance of different binary classification approaches.

## Team members

- Pian Wan, pian.wan@epfl.ch
- Qianjun Xu, qianjun.xu@epfl.ch
- Siyuan Cheng, siyuan.cheng@epfl.ch

## Quickstart

### Requirements

```shell
git clone git@github.com:epfml/ml-project-1-cross-entropy.git
cd ml-project-1-cross-entropy
pip install -r requirements.txt
```

### Datasets

You can download the dataset [here](https://github.com/epfml/ML_course/blob/master/projects/project1/data/dataset.zip).
Extract all files and move into a new folder `./data` in the base dir. We do not include full dataset in the repository because of the large size of dataset.

### Result

|                | Accuracy (%) | F1-score (%) |
| -------------- | ------------ | ------------ |
| Training       | 0.425        | 0.868        |
| Validation     | 0.423        | 0.866        |
| Test (AIcrowd) | 0.883        | 0.432        |

## Project Organization

```shell
.
├── README.md
├── data (Put your dataset here)
├── grading_tests (Skeleton)
├── helpers.py (Skeleton)
├── impl (implementation details of our project)
│   ├── __init__.py
│   ├── data
│   │   ├── __init__.py
│   │   ├── _lib.py
│   │   ├── dataloader.py
│   │   ├── define.py
│   │   └── define.xlsx
│   ├── method
│   │   ├── base_method.py
│   │   ├── gardient_desent.py
│   │   ├── logistic_regression.py
│   │   └── stochastic_gardient_desent.py
│   └── util
│       ├── __init__.py
│       ├── evaluation.py
│       └── utils.py
├── implementations.py (interface left for grading_tests)
├── paper_figs.ipynb (notebook for draw image)
├── project1_description.pdf (Skeleton)
├── requirements.txt (Requirements)
├── result.csv (Our result)
├── run.py (Train and predict result on CVDs dataset)
├── test (test written by ourselves)
│   ├── __init__.py
│   ├── conftest.py
│   ├── data
│   │   └── test_dataloader.py
│   └── module
└─      └── test_bias.py


```