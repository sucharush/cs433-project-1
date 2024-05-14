from typing import Union, Optional, List

import numpy as np

from impl.data._lib import get_csv_column_name, get_name2idx_map

_START_COLUMN = 230  # corresponds to _RFHLTH column


class DataLoader:
    """
    A simple data loader.

    Attributes:
        xfilename: The filename of the x_train.csv file
        yfilename: The filename of the y_train.csv file
    """

    def __init__(self,
                 xfilename: Optional[str] = None,
                 yfilename: Optional[str] = None,
                 x: Optional[np.ndarray] = None,
                 y: Optional[np.ndarray] = None,
                 column: Optional[list] = None,
                 ratio_missing: Optional[float] = 1):
        self.xfilename = xfilename
        self.yfilename = yfilename
        if xfilename is not None:
            # skip the first ID column
            self.column = get_csv_column_name(xfilename)[1:]
            # skip the first ID column
            self.data = np.genfromtxt(xfilename,
                                      delimiter=',',
                                      skip_header=1)[:, 1:]
            # delete every line before the _START_ COLUMN
            # self._delete([i for i in range(_START_COLUMN)
            #              if self.column[i] not in USEFUL_QUESTIONARE])
        elif x is not None:
            self.data = x
            if column is not None:
                assert x.shape[1] == len(column), \
                    "Column length mismatch between x and column"
                self.column = column
            else:
                self.column = [f'feature {i}' for i in range(x.shape[1])]
        else:
            raise ValueError("If filename is not provided, "
                             "x cannot be None")

        if yfilename is not None and y is None:
            y = np.genfromtxt(yfilename,
                              delimiter=',',
                              skip_header=1)[:, 1:]

        if y is not None:
            self.data = np.column_stack([self.data, y])
            self.column = np.append(self.column, 'label')
            self.data[self.data[:, -1] == -1, -1] = 0
        self._name2column = {name: i for i, name in enumerate(self.column)}

        to_delete = []
        for column in self.column:
            n_nan = np.sum(np.isnan(self[column]))
            if n_nan / len(self.data) > ratio_missing:
                to_delete.append(column)
        self.delete_column(to_delete)

    def __len__(self) -> int:

        return len(self.data)

    def __getitem__(self, key: Union[int, np.ndarray, str]) -> (np.ndarray, np.ndarray):

        if isinstance(key, int) or isinstance(key, list) \
                or isinstance(key, np.ndarray):
            return self.data[key]
        elif isinstance(key, str):
            return self.data[:, self._name2column[key]]

    def __repr__(self) -> str:

        return f"DataLoader with {self.__len__()} datapoints\n" \
               f"xfilename = {self.xfilename}\n" \
               f"yfilename = {self.yfilename}\n"

    def _get_data_missing_ratio(self) -> float:
        """
        Calculate the ratio of missing data in the dataset.

        Returns:
            float: The missing data ratio.
        """

        return np.sum(np.isnan(self.data), axis=0) / len(self)

    @classmethod
    def from_array(cls,
                   x: np.ndarray,
                   y: np.ndarray,
                   column: Optional[list] = None) -> 'DataLoader':

        if column is None:
            column = [f'feature {i}' for i in range(x.shape[1])]

        return cls(x=x, y=y, column=column)

    def delete_column(self, name: Union[str, list]):
        """
        Deletes the specified column(s) from the dataset.

        Parameters:
            name (Union[str, list]): The name of the column(s) to be deleted.
            Can be a single string or a list of strings.

        Returns:
            None
        """
        if isinstance(name, str):
            name = [name]
        del_idx = []
        for colname in name:
            if colname not in self._name2column.keys():
                print(f'The column {colname} you want to '
                      'delete is not in the dataset.')
                continue
            del_idx.append(self._name2column[colname])
        self._delete(del_idx)

    def _delete(self, idxs: list):
        """
        Delete specified indices from the x arrays.

        Parameters:
            idxs (list): A list of indices to delete.

        Returns:
            None
        """

        self.column = np.delete(self.column, idxs)
        self.data = np.delete(self.data, idxs, axis=1)
        self._name2column = get_name2idx_map(self.column)
        assert len(self._name2column) == self.data.shape[1] and \
               len(self._name2column) == len(self.column)

    def standardize(self, select_feature: list):
        """
        Standardizes the selected features in the dataset.

        Parameters:
            select_feature (list): A list of strings representing the names of
            the features to be standardized.

        Returns:
            None
        """

        select_idx = [self._name2column[feature] for feature in select_feature
                      if np.std(self[feature]) != 0]
        x_mean = np.nanmean(self.data[:, select_idx], axis=0)
        x_std = np.nanstd(self.data[:, select_idx], axis=0)
        self.data[:, select_idx] = (self.data[:, select_idx] - x_mean) / x_std

    def normalize(self, select_feature: list):
        """
        Normalize the selected features in the dataset.

        Args:
            select_feature (list): A list of strings representing the names of
            the features to be normalized.

        Returns:
            None
        """

        select_idx = [self._name2column[feature] for feature in select_feature
                      if np.nanmax(self[feature]) != np.nanmin(self[feature])]
        x_max = np.nanmax(self.data[:, select_idx], axis=0)
        x_min = np.nanmin(self.data[:, select_idx], axis=0)

        self.data[:, select_idx] = \
            (self.data[:, select_idx] - x_min) / (x_max - x_min)

    def split(self,
              portion: Optional[float]) -> List['DataLoader']:
        """
        Splits the data into batches of a specified size
        or a specified number of batches.

        Args:
            portion (float | None): The size of batch that you want, the rest
            will also be returned. Default is None.

        Returns:
            list['DataLoader']: A list of DataLoader.
        """

        shuffle = np.random.shuffle(list(range(len(self))))
        portion = int(len(self) * portion)
        data_batch = [batch
                      for batch in np.split(np.squeeze(self.data[shuffle]),
                                            np.arange(portion,
                                                      self.__len__(),
                                                      portion))]

        if 'label' in self.column:
            return [DataLoader.from_array(batch[:, :-1],
                                          batch[:, -1],
                                          self.column[:-1].tolist())
                    for batch in data_batch]
        else:
            return [DataLoader.from_array(batch,
                                          self.column)
                    for batch in data_batch]

    def split_k_fold(self,
                     k: Optional[int]) -> List['DataLoader']:
        """
        Splits the data into batches of a k_fold or a specified number of batches.

        Args:
            portion (float | None): The size of batch that you want, the rest
            will also be returned. Default is None.

        Returns:
            list['DataLoader']: A list of DataLoader.
        """

        shuffle = np.random.shuffle(list(range(len(self))))
        shuffle = np.squeeze(self.data[shuffle])
        bounds = np.arange(0, k + 1) * (k / len(self))
        bounds.astype(int)

        data_batch = []

        for i in range(len(bounds)):
            loader = DataLoader.from_array(shuffle[int(bounds[i]):int(bounds[i + 1]), :-1],
                                           shuffle[int(bounds[i]):int(bounds[i + 1]), -1],
                                           shuffle[:-1].tolist())
            data_batch.append(loader)

        if 'label' in self.column:
            return [DataLoader.from_array(batch[:, :-1],
                                          batch[:, -1],
                                          self.column[:-1].tolist())
                    for batch in data_batch]
        else:
            return [DataLoader.from_array(batch,
                                          self.column)
                    for batch in data_batch]
