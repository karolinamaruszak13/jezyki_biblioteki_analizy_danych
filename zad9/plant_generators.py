import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class PlantGenerators:
    def __init__(self, *args):
        dfs = [pd.read_csv(filename) for filename in args]
        self.df = pd.concat(dfs, ignore_index=True)

    def _drop_NaN_rows(self):
        rows_with_NaN = self.df.index[self.df.isnull().any(axis=1)]
        # print(rows_with_NaN.shape)
        self.df.drop(rows_with_NaN, 0, inplace=True)
        return self.df

    def _convert_data_time(self):
        self.df['DATE_TIME'] = pd.to_datetime(self.df['DATE_TIME'])
        self.df['DATE_HOUR'] = self.df['DATE_TIME'].dt.strftime('%H:%M')
        return self.df

    def avg_for_generators(self):
        self._convert_data_time()
        df = self._drop_NaN_rows()
        generators_mean = pd.DataFrame(df.groupby(['SOURCE_KEY']).mean()['DAILY_YIELD'])
        mean_column = df.merge(generators_mean, on='SOURCE_KEY', suffixes=('', '_MEAN'))
        result = mean_column[['DAILY_YIELD_MEAN']]
        df['MEAN'] = result.values
        return df['MEAN']


    def daily_yield_to_avg_ratio(self, SOURCE_KEY1, SOURCE_KEY2):
        self._convert_data_time()
        df = self._drop_NaN_rows()
        daily_yield1 = pd.DataFrame(df.loc[df['SOURCE_KEY'] == SOURCE_KEY1]['DAILY_YIELD'])
        daily_yield2 = pd.DataFrame(df.loc[df['SOURCE_KEY'] == SOURCE_KEY2]['DAILY_YIELD'])
        daily_yield = pd.concat([daily_yield1, daily_yield2])
        df['RATIO'] = daily_yield.div(self.avg_for_generators())
        print(df)



p = PlantGenerators("Plant_1_Generation_Data.csv", "Plant_2_Generation_Data.csv")
# p.avg_for_generators()
p.daily_yield_to_avg_ratio('1BY6WEcLGh8j5v7', '1IF53ai7Xc0U56Y')
