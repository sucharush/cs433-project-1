import numpy as np
from concurrent.futures import ThreadPoolExecutor
from rich import progress as prog


class KNNDataImputer:

    def __init__(self, k=3, missing_value=np.nan, feature_categories=None):
        self.k = k
        self.missing_value = missing_value
        self.feature_categories = feature_categories

    def calculate_mixed_distance(self, target_data, data):
        """
        Calculate the mixed distance between the target data and
          the given data.

        Parameters:
            target_data (numpy.ndarray): The target data for
              distance calculation.
            data (numpy.ndarray): The data to compare with the target data.

        Returns:
            numpy.ndarray: The mixed distance between the target data and
              the given data.
        """
        seq_mask = np.array([ft in ["Continues", "Discrete_Seq"]
                             for ft in self.feature_categories])
        discrete_noseq_mask = np.array([ft == "Discrete_NoSeq"
                                        for ft in self.feature_categories])

        dist_seq = np.sum((target_data[seq_mask] - data[:, seq_mask]) ** 2,
                          axis=1)

        dist_noseq = np.sum(target_data[None, discrete_noseq_mask] != 
                            data[:, discrete_noseq_mask], axis=1)

        return dist_seq + dist_noseq

    def run(self, data_mat):
        """
        Runs the imputation algorithm on the given dataset.

        Parameters:
            data_mat (ndarray): The input dataset with missing values.

        Returns:
            ndarray: The dataset with missing values imputed.
        """
        data = np.copy(data_mat)
        self.data_base = data[[not np.isnan(data[i]).any()
                               for i in range(len(data))]]
        N, D = data.shape
        missing_mask = np.isnan(data)
        with prog.Progress("[progress.description]{task.description}",
                           prog.BarColumn(),
                           "[progress.percentage]{task.percentage:>3.0f}%",
                           prog.TimeRemainingColumn(),
                           prog.TimeElapsedColumn(),
                           refresh_per_second=1
                           ) as progress:
            with ThreadPoolExecutor(max_workers=16) as executor:
                processes = []
                for i in range(N):
                    if missing_mask[i].any():
                        processes.append(executor.submit(self._impute,
                                                         data[i],
                                                         missing_mask[i]))
                n_tasks = len(processes)
                main_progress_task = progress.add_task('Main task',
                                                       total=n_tasks)
                while True:
                    n_completed = len([h for h in processes if h.done()])

                    progress.update(
                        main_progress_task,
                        visible=True,
                        completed=n_completed)
                    if n_completed == n_tasks:
                        break

        return data

    def _impute(self, target_data, missing_mask):

        distances = self.calculate_mixed_distance(target_data, self.data_base)
        sorted_neighbors = np.argsort(distances, axis=0)

        for idx, is_missing in enumerate(missing_mask):
            if not is_missing:
                continue
            non_missing_values = self._get_non_missing_values(sorted_neighbors,
                                                              idx)
            feature_type = self.feature_categories[idx]
            target_data[idx] = self._assign_value(feature_type,
                                                  non_missing_values)

        return target_data

    def _get_non_missing_values(self, sorted_neighbors, idx):
        available_neighbors = ~np.isnan(self.data_base[sorted_neighbors, idx])
        neighbors = sorted_neighbors[available_neighbors][:self.k]
        non_missing_values = self.data_base[neighbors, idx]

        return non_missing_values

    def _choose_mode(self, non_missing_values):
        """
        Choose the mode from a list of non-missing values.

        Parameters:
            non_missing_values (np.ndarray): An array of non-missing values.

        Returns:
            chosen_mode: The mode of the non-missing values.
        """
        label_candidates, counts = np.unique(non_missing_values,
                                             return_counts=True)
        chosen_mode = label_candidates[np.argmax(counts)]

        return chosen_mode

    def _assign_value(self, feature_type, non_missing_values):

        if feature_type in ["Continues", "Discrete_Seq"]:
            return np.mean(non_missing_values)
        else:  # Discrete_NoSeq
            if not non_missing_values.size:  # empty array
                return 0
            else:
                return self._choose_mode(non_missing_values)
