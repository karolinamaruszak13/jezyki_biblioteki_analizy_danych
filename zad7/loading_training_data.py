import numpy as np


class LoadCSV:

    def __init__(self, path):
        with open(path, encoding='utf-8') as csv_file:
            self.csv_data = np.genfromtxt(csv_file, delimiter=';')

    def get_label(self):
        return self.csv_data[:, ~0]

    def column_normalization(self, col):
        ''' Nie do konca jestem pewna czy chodzilo o zwrocenie jednej kolumny czy o podmiane kolumny w calej tablicy'''
        col -= 1
        if 0 <= col < self.csv_data.shape[1] - 1 and isinstance(col, int):
            self.csv_data[:, col] = self.csv_data[:, col] / np.linalg.norm(self.csv_data[:, col])  # podmieniam kolumne
        else:
            raise ValueError(f"Column must be integer in range (1, {self.csv_data.shape[1] - 1})")

    def column_centering(self, col):
        ''' Nie do konca jestem pewna czy chodzilo o zwrocenie jednej kolumny czy o podmiane kolumny w calej tablicy'''
        col -= 1
        if 0 <= col < self.csv_data.shape[1] - 1 and isinstance(col, int):
            mean_value = self.csv_data[:, col] - self.csv_data[:, col].mean()
            std_value = self.csv_data[:, col].std()
            self.csv_data[:, col] = np.divide(mean_value, std_value, where=std_value != 0)  # podmieniam kolumne
        else:
            raise ValueError(f"Column must be integer in range (1, {self.csv_data.shape[1] - 1})")

    def rows_normalization(self):
        ''' Nie do konca jestem pewna czy chodzilo o zwrocenie znormalizowanej tablicy czy o jej podmiane '''
        self.csv_data = self.csv_data / np.linalg.norm(self.csv_data, axis=0)

    def getX(self):
        return self.csv_data[:, :self.csv_data.shape[1] - 1]


l = LoadCSV('sample1.csv')
# print(l.column_normalization(2))
# print(l.column_centering(2))
# print(l.get_label())

# l.rows_normalization()
# print(l.csv_data)
# print(l.getX())
