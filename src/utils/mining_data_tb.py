# mining_data_tb.py 
# Creator: Javier Olcoz
# Last review: 20/01/2021 by Javier Olcoz


import pandas as pd
import numpy as np



class Miner:

    

    def chosen_countries(self, old_df, location_column, country_1, country_2, country_3, country_4, country_5):
        """ It divides the original df in others where the 'location' column is specific for the country given,
        then, it concatenates them into a single df
            Args: new dataframe name, dataframe to work with, location_column, 5 countries to work with
            Return a df with the asked countries
            Creator: Javier Olcoz Macayo
        """
        x1 = old_df[old_df[location_column] == country_1]
        x2 = old_df[old_df[location_column] == country_2] 
        x3 = old_df[old_df[location_column] == country_3]
        x4 = old_df[old_df[location_column] == country_4] 
        x5 = old_df[old_df[location_column] == country_5] 
        new_df = pd.concat([x1, x2, x3, x4, x5], ignore_index=True)
        
        return new_df

    def column_to_datetime(self, dataset,column_to_change):
        """ It turns the column given into datetime type with the format '%Y/%m/%d'
            Args: dataset and the column to change
            Creator: Javier Olcoz Macayo
        """
        dataset[column_to_change] = pd.to_datetime(dataset[column_to_change], format= '%Y/%m/%d')

        return dataset

    def pivot_table_date_location(self, dataset, index_1, index_2):
        """ Creates a pivot table with the chosen index
            Args: dataset and 2 index
            Creator: Javier Olcoz Macayo
        """
        new_df = pd.pivot_table(dataset,index=[index_1, index_2])

        return new_df

    def set_index_1(self, dataset, index_3):
        """ Sets index_3 as index
            Args: datset, index
            Creator: Javier Olcoz Macayo
        """
        new_df = dataset.set_index(index_3)

        return new_df

    def no_constant_df(self, old_df, country_1, country_2, country_3, country_4, country_5):
        """ It divides the original df in the ones from each country, then drops the constant columns
        finally concatenates them.
            Args: dataframe and each country
            Creator: @JavierOlcoz
        """
        x1 = old_df[old_df.index == country_1]
        a = x1.loc[:, (x1 != x1.iloc[0]).any()]
        a['location'] = country_1

        x2 = old_df[old_df.index == country_2]
        b = x2.loc[:, (x2 != x2.iloc[0]).any()] 
        b['location'] = country_2

        x3 = old_df[old_df.index == country_3]
        c = x3.loc[:, (x3 != x3.iloc[0]).any()] 
        c['location'] = country_3

        x4 = old_df[old_df.index == country_4]
        d = x4.loc[:, (x4 != x4.iloc[0]).any()] 
        d['location'] = country_4

        x5 = old_df[old_df.index == country_5]
        e = x5.loc[:, (x5 != x5.iloc[0]).any()] 
        e['location'] = country_5

        df_no_constant = pd.concat([a, b, c, d, e], ignore_index=True)

        return df_no_constant

    
    def drop_per_columns(self, dataset):
        """ Drop the following columns from the dataset
            Args: dataset
            Creator @JavierOlcoz
        """
        df_no_per = dataset.drop(['total_cases_per_million', 'new_cases_per_million',
        'new_cases_smoothed_per_million', 'total_deaths_per_million', 'new_deaths_per_million',
        'new_deaths_smoothed_per_million', 'icu_patients_per_million', 'hosp_patients_per_million',
        'weekly_icu_admissions_per_million', 'weekly_hosp_admissions_per_million', 'total_tests_per_thousand',
        'new_tests_per_thousand', 'new_tests_smoothed_per_thousand', 'tests_per_case',
        'total_vaccinations_per_hundred', 'new_vaccinations_smoothed_per_million', 'hospital_beds_per_thousand'],
         axis=1)

        return df_no_per


    def neg_to_nan(self, dataset, i):
        """ Replaces the negatives values by Nan values.
            Args: dataset, column
            Creator: @JavierOlcoz
        """
        
        dataset[i]=dataset[i].mask(dataset[i].lt(0),np.nan)
        
        return dataset

    def neg_to_nan_complete(self, dataset):
        """ Replaces the negatives values by Nan values in all the dataframe
            Args: dataset
            Creator: @JavierOlcoz
        """

        for i in dataset.columns:
            if dataset[i].dtype == float:
                dataset = dataset[(dataset[i] >= 0) | (dataset[i].isnull())]

        return dataset

    def by_country(self, dataset, country):
        """ Makes a df of the data from the same country and delete the columns with all values = Nan
            Args: dataset, coutry
            Creator: @JavierOlcoz
        """
        x = dataset.loc[country]
        
        return x

    def highest_correlation_columns_per_country(self, dataset, h):
        """ Returns a matrix with the highest correlation columns of the dataset given
            Args: dataset, h (how high the correlation you ask to be)
            Creator @JavierOlcoz
        """
        # Empty lists used in the process
        most_correlation_x = []
        keys_list_x = []

        # Assign the dataset to a variable, drop the columns with all the values equal to Nan, 
        # drop the columns with too many Nan results and obtain the correlation matrix 

        x = dataset
        x = x.dropna(axis=1, how='all')
        thresh = len(x) * .15
        x.dropna(thresh = thresh, axis = 1, inplace = True)
        x_correlation = x.corr()

        # Get the highest correlation from the previous matrix

        x_middle = (x_correlation.where(np.triu(np.ones(x_correlation.shape), k=1).astype(np.bool)).stack().sort_values(ascending=False))

        # Make a list of the correlations and the columns involved 

        for index, value in x_middle.items():
            if h < value < 0.989 or -0.989 < value < -h:
                most_correlation_x.append(index)


        for i in most_correlation_x:
            for j in i:
                if j not in keys_list_x:
                    keys_list_x.append(j)

        # Obtain the matrix with the highest correlated columns.

        df_x_highest_correlation = x[keys_list_x]
        z = df_x_highest_correlation.corr()

        return z


    def country_position(self, dataset, country, variable, h):
        """ Function that return the position of the country in the world in terms of the variable
            Args: dataset you are working with, country you want to know, variable to check and h
            (number of countries in your dataset)
        """
        x1 = dataset.groupby('location')[variable].aggregate([max])
        x1 = x1.sort_values(['max'], ascending=False)
        x1['location'] = x1.index
        x1.index = np.arange(h)
        total = x1[x1['location'] == country]
        total['Position'] = total.index
        total = total.set_index(['location'])

        return total