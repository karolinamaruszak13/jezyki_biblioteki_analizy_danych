import pandas as pd
import matplotlib.pyplot as plt


class DataCSV:
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
        return self.df

    def ac_power_plot(self, SOURCE_KEY, startWeek, endWeek):
        self._convert_data_time()
        df = self._drop_NaN_rows()
        df.loc[(df['DATE_TIME'] >= startWeek) & (df['DATE_TIME'] <= endWeek)].loc[df['SOURCE_KEY'] == SOURCE_KEY] \
            .plot(x="DATE_TIME", y= "AC_POWER", xlabel="DATE_TIME", ylabel="AC_POWER", label=f'{SOURCE_KEY}')
        df.loc[(df['DATE_TIME'] >= startWeek) & (df['DATE_TIME'] <= endWeek)].groupby(['DATE_TIME']).mean()['AC_POWER']\
            .plot(xlabel="DATE_TIME", ylabel="AC_POWER", label='General_AC_POWER_MEAN')

        plt.legend()
        plt.suptitle("AC_POWER plot for selected week \n along with ac_power averages for all generators")
        plt.show()

    def find_ac_power_below_avg(self):
        self._convert_data_time()
        df = self._drop_NaN_rows()
        general_mean = pd.DataFrame(df.groupby(['DATE_TIME']).mean()['AC_POWER'])
        mean_column = df.merge(general_mean, on='DATE_TIME', suffixes=('', '_MEAN'))
        result = mean_column[mean_column['AC_POWER'] < 0.8 * mean_column['AC_POWER_MEAN']]
        result = result[['AC_POWER', 'SOURCE_KEY', 'AC_POWER_MEAN']]
        return result

    def count_generators(self):
        df = self.find_ac_power_below_avg().set_index(['SOURCE_KEY'])
        return df['AC_POWER'].groupby(['SOURCE_KEY']).count().sort_values()
#najczesciej dotyczy to generatora Quc1TzYxW2pYoWX

d = DataCSV("Plant_1_Generation_Data.csv", "Plant_2_Generation_Data.csv")
# print(d.drop_NaN_rows())
d.ac_power_plot('1BY6WEcLGh8j5v7', '2020-05-15 00:00:00', '2020-05-23 00:00:00')
print(d.find_ac_power_below_avg())
print(d.count_generators())
