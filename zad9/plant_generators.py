import pandas as pd
import matplotlib.pyplot as plt


class PlantGenerators:
    def __init__(self, *args):
        dfs = [pd.read_csv(filename) for filename in args]
        self.df = pd.concat(dfs, ignore_index=True)

    def _drop_NaN_rows(self):
        rows_with_NaN = self.df.index[self.df.isnull().any(axis=1)]
        self.df.drop(rows_with_NaN, 0, inplace=True)
        return self.df

    def _convert_data_time(self):
        self.df['DATE_TIME'] = pd.to_datetime(self.df['DATE_TIME'])
        self.df['DATE_HOUR'] = self.df['DATE_TIME'].dt.strftime('%H:%M')
        return self.df

    def avg_for_generators(self):
        self._convert_data_time()
        df = self._drop_NaN_rows()
        generators_mean = pd.DataFrame(df.loc[df['DATE_HOUR'] == '23:45'].groupby(['DATE_TIME']).mean()['DAILY_YIELD'])
        return generators_mean

    def choose_daily_yield_gen(self, SOURCE_KEY):
        self._convert_data_time()
        df = self._drop_NaN_rows().set_index(['SOURCE_KEY', 'DATE_TIME'])
        daily_yield = pd.DataFrame(df.loc[df['DATE_HOUR'] == '23:45']
                                   .loc[SOURCE_KEY]['DAILY_YIELD'])
        return daily_yield

    def ratio(self, SOURCE_KEY):
        mean = self.avg_for_generators()
        daily_yield_gen = self.choose_daily_yield_gen(SOURCE_KEY)
        ratio_frame = pd.merge(daily_yield_gen, mean, on='DATE_TIME', suffixes=('_GEN', '_MEAN'))
        ratio_frame['RATIO'] = ratio_frame.DAILY_YIELD_GEN.div(ratio_frame.DAILY_YIELD_MEAN)    # czemu nie zwykłe dzielenie?

        return ratio_frame

    def ac_power_plot(self, SOURCE_KEY1, SOURCE_KEY2, startWeek, endWeek):
        self._convert_data_time()
        df = self._drop_NaN_rows().set_index(['SOURCE_KEY', 'DATE_TIME'])

        # ac_power dla dwoch wybranych generatorow
        df.loc[SOURCE_KEY1]['AC_POWER'][startWeek:endWeek] \
            .plot(xlabel="DATE_TIME", color='g', linewidth=2, ylabel="AC_POWER", label=f'{SOURCE_KEY1}')
        df.loc[SOURCE_KEY2]['AC_POWER'][startWeek:endWeek] \
            .plot(xlabel="DATE_TIME", color='lightcoral', linewidth=2, ylabel="AC_POWER", label=f'{SOURCE_KEY2}')

        # ac_power dla czterech innych
        df.loc['ih0vzX44oOqAx2f']['AC_POWER'][startWeek:endWeek] \
            .plot(xlabel="DATE_TIME", color='r', linestyle='dashed', linewidth=1, ylabel="AC_POWER",
                  label='ih0vzX44oOqAx2f')
        df.loc['zBIq5rxdHJRwDNY']['AC_POWER'][startWeek:endWeek] \
            .plot(xlabel="DATE_TIME", color='blue', linestyle='dashed', linewidth=1, ylabel="AC_POWER", # DRY
                  label='zBIq5rxdHJRwDNY')
        df.loc['rrq4fwE8jgrTyWY']['AC_POWER'][startWeek:endWeek] \
            .plot(xlabel="DATE_TIME", color='y', linestyle='dashed', linewidth=1, ylabel="AC_POWER",
                  label='rrq4fwE8jgrTyWY')
        df.loc['4UPUqMRk7TRMgml']['AC_POWER'][startWeek:endWeek] \
            .plot(xlabel="DATE_TIME", color='#4b0082', linestyle='dashed', linewidth=1, ylabel="AC_POWER",
                  label='4UPUqMRk7TRMgml')

        plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))


    def dc_power_plot(self, SOURCE_KEY1, SOURCE_KEY2, startWeek, endWeek):
        self._convert_data_time()
        df = self._drop_NaN_rows().set_index(['SOURCE_KEY', 'DATE_TIME'])

        # dc_power dla dwoch wybranych generatorow
        df.loc[SOURCE_KEY1]['DC_POWER'][startWeek:endWeek] \
            .plot(xlabel="DATE_TIME", color='g', linewidth=2, ylabel="AC_POWER", label=f'{SOURCE_KEY1}')
        df.loc[SOURCE_KEY2]['DC_POWER'][startWeek:endWeek] \
            .plot(xlabel="DATE_TIME", color='lightcoral', linewidth=2, ylabel="AC_POWER", label=f'{SOURCE_KEY2}')

        # dc_power dla czterech innych
        df.loc['ih0vzX44oOqAx2f']['DC_POWER'][startWeek:endWeek] \
            .plot(xlabel="DATE_TIME", color='r', linestyle='dashed', linewidth=1, ylabel="AC_POWER",
                  label='ih0vzX44oOqAx2f')
        df.loc['zBIq5rxdHJRwDNY']['DC_POWER'][startWeek:endWeek] \
            .plot(xlabel="DATE_TIME", color='blue', linestyle='dashed', linewidth=1, ylabel="AC_POWER",
                  label='zBIq5rxdHJRwDNY')
        df.loc['rrq4fwE8jgrTyWY']['DC_POWER'][startWeek:endWeek] \
            .plot(xlabel="DATE_TIME", color='y', linestyle='dashed', linewidth=1, ylabel="AC_POWER",
                  label='rrq4fwE8jgrTyWY')
        df.loc['4UPUqMRk7TRMgml']['DC_POWER'][startWeek:endWeek] \
            .plot(xlabel="DATE_TIME", color='#4b0082', linestyle='dashed', linewidth=1, ylabel="AC_POWER",
                  label='4UPUqMRk7TRMgml')

        plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

    def map_element(self, element):
        if element < 0.75:
            return "<75%"
        elif 0.85 > element >= 0.75:    # DRY
            return "75-85%"
        elif 0.95 > element >= 0.85:
            return "85-95%"
        elif 1.05 > element >= 0.95:
            return "95-105%"
        elif 1.15 > element >= 1.05:
            return "105-115%"
        elif 1.25 > element >= 1.15:
            return "115-125%"
        elif element >= 1.25:
            return ">125%"

    def count_days(self, SOURCE_KEY):
        df = self.ratio(SOURCE_KEY)
        df['RATIO'] = df['RATIO'].map(lambda x: self.map_element(x))
        df = df.set_index(['RATIO'])
        return df['DAILY_YIELD_GEN'].groupby(['RATIO']).count()

    def bar_graph(self, SOURCE_KEY):
        df = self.count_days(SOURCE_KEY)
        ratio_values = pd.DataFrame(df.groupby(['RATIO'])).values[:, 0]
        x = pd.Series(range(len(df)))

        plt.rc('xtick', labelsize=11)
        df.plot(kind='bar', alpha=1, rot=50, xlabel="RATIO", ylabel="AMOUNT")
        plt.xticks(x, ratio_values)

    def sub_plots(self):
        plt.figure()

        plt.subplot(221)
        self.ac_power_plot('1BY6WEcLGh8j5v7', '1IF53ai7Xc0U56Y', '2020-05-15 00:00:00', '2020-05-23 00:00:00')
        plt.title('AC_POWER')
        plt.grid(True)

        plt.subplot(222)
        self.dc_power_plot('1BY6WEcLGh8j5v7', '1IF53ai7Xc0U56Y', '2020-05-15 00:00:00', '2020-05-23 00:00:00')
        plt.title('DC_POWER')
        plt.grid(True)

        plt.subplot(223)
        self.bar_graph('1BY6WEcLGh8j5v7')
        plt.title('Bar graph for 1BY6WEcLGh8j5v7')
        plt.grid(True)

        plt.subplot(224)
        self.bar_graph('1IF53ai7Xc0U56Y')
        plt.title('Bar graph for 1IF53ai7Xc0U56Y')
        plt.grid(True)

        plt.subplots_adjust(top=1.9, bottom=0.03, left=0.05, right=2, hspace=2,
                            wspace=2)

        plt.show()


p = PlantGenerators("Plant_1_Generation_Data.csv", "Plant_2_Generation_Data.csv")
# p.avg_for_generators()
# p.choose_daily_yield_gen('1BY6WEcLGh8j5v7')
# p.ratio('1BY6WEcLGh8j5v7')
# p.ac_power_plot( '1BY6WEcLGh8j5v7', '1IF53ai7Xc0U56Y', '2020-05-15 00:00:00', '2020-05-23 00:00:00')
# p.dc_power_plot( '1BY6WEcLGh8j5v7', '1IF53ai7Xc0U56Y', '2020-05-15 00:00:00', '2020-05-23 00:00:00')
# p.bar_graph('1BY6WEcLGh8j5v7')
# p.count_days('1BY6WEcLGh8j5v7')
p.sub_plots()
