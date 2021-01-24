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

    def matrix_high_correlation(self,dataset1, dataset2, dataset3, dataset4, dataset5):
        """ Return the correlation matrix of the 5 given countries
            Args: dataset of each country
            Creator: @JavierOlcoz
        """
        highest_poland_correlation = self.highest_correlation_columns_per_country(dataset=dataset1, h=0.90)
        highest_south_africa_correlation = self.highest_correlation_columns_per_country(dataset=dataset2, h=0.90)
        highest_indonesia_correlation = self.highest_correlation_columns_per_country(dataset=dataset3, h=0.90)
        highest_ukraine_correlation = self.highest_correlation_columns_per_country(dataset=dataset4, h=0.90)
        highest_spain_correlation = self.highest_correlation_columns_per_country(dataset=dataset5, h=0.90)

        top_10_highest_poland_correlation = self.highest_correlation_columns_per_country(dataset=dataset1, h=0.877)
        top_10_highest_south_africa_correlation = self.highest_correlation_columns_per_country(dataset=dataset2, h=0.90)
        top_10_highest_indonesia_correlation = self.highest_correlation_columns_per_country(dataset=dataset3, h=0.54)
        top_10_highest_ukraine_correlation = self.highest_correlation_columns_per_country(dataset=dataset4, h=0.82)
        top_10_highest_spain_correlation = self.highest_correlation_columns_per_country(dataset=dataset5, h=0.68)

        return highest_poland_correlation, highest_south_africa_correlation, highest_indonesia_correlation, highest_ukraine_correlation, highest_spain_correlation, top_10_highest_poland_correlation, top_10_highest_south_africa_correlation, top_10_highest_indonesia_correlation, top_10_highest_ukraine_correlation, top_10_highest_spain_correlation


    def country_position(self, dataset, country, variable, h):
        """ Function that return the position of the country in the world in terms of the variable
            Args: dataset you are working with, country you want to know, variable to check and h
            (number of countries in your dataset)
            Creator: @JavierOlcoz
        """
        x1 = dataset.groupby('location')[variable].aggregate([max])
        x1 = x1.sort_values(['max'], ascending=False)
        x1['location'] = x1.index
        x1.index = np.arange(h)
        total = x1[x1['location'] == country]
        total['Position'] = total.index
        total = total.set_index(['location'])

        return total


    def total_infected(self, dataset1):
        """ Concatenates all the dataframes
            Args: dataset used
            Creator: @JavierOlcoz
        """
        poland_total_cases = self.country_position(dataset=dataset1, country='Poland',variable='total_cases',h=193)
        south_africa_total_cases = self.country_position(dataset=dataset1,country='South Africa',variable='total_cases',h=193)
        indonesia_total_cases = self.country_position(dataset=dataset1,country='Indonesia',variable='total_cases',h=193)
        ukraine_total_cases = self.country_position(dataset=dataset1,country='Ukraine',variable='total_cases',h=193)
        spain_total_cases = self.country_position(dataset=dataset1,country='Spain',variable='total_cases',h=193)
        our_countries_total_cases = pd.concat([poland_total_cases, south_africa_total_cases, indonesia_total_cases, ukraine_total_cases, spain_total_cases])

        return our_countries_total_cases  


    def total_deaths(self, dataset1):
        """ Concatenates all the dataframes
            Args: dataset used
            Creator: @JavierOlcoz
        """
        poland_total_deaths = self.country_position(dataset=dataset1,country='Poland',variable='total_deaths',h=193)
        south_africa_total_deaths = self.country_position(dataset=dataset1,country='South Africa',variable='total_deaths',h=193)
        indonesia_total_deaths = self.country_position(dataset=dataset1,country='Indonesia',variable='total_deaths',h=193)
        ukraine_total_deaths = self.country_position(dataset=dataset1,country='Ukraine',variable='total_deaths',h=193)
        spain_total_deaths = self.country_position(dataset=dataset1,country='Spain',variable='total_deaths',h=193)
        our_countries_total_deaths = pd.concat([poland_total_deaths, south_africa_total_deaths, indonesia_total_deaths, ukraine_total_deaths, spain_total_deaths])

        return our_countries_total_deaths


    def life_expectancy(self, dataset1): 
        """ Concatenates all the dataframes
            Args: dataset used
            Creator: @JavierOlcoz
        """   
        poland_life_expectancy = self.country_position(dataset=dataset1,country='Poland',variable='life_expectancy',h=193)
        south_africa_life_expectancy = self.country_position(dataset=dataset1,country='South Africa',variable='life_expectancy',h=193)
        indonesia_life_expectancy = self.country_position(dataset=dataset1,country='Indonesia',variable='life_expectancy',h=193)
        ukraine_life_expectancy = self.country_position(dataset=dataset1,country='Ukraine',variable='life_expectancy',h=193)
        spain_life_expectancy = self.country_position(dataset=dataset1,country='Spain',variable='life_expectancy',h=193)
        our_countries_life_expectancy = pd.concat([poland_life_expectancy, south_africa_life_expectancy, indonesia_life_expectancy, ukraine_life_expectancy, spain_life_expectancy])

        return our_countries_life_expectancy


    def total_recoveries(self, dataset1):
        """ Concatenates all the dataframes
            Args: dataset used
            Creator: @JavierOlcoz
        """
        poland_total_recoveries = self.country_position(dataset=dataset1,country='Poland',variable='recovered',h=193)
        south_africa_total_recoveries = self.country_position(dataset=dataset1,country='South Africa',variable='recovered',h=193)
        indonesia_total_recoveries = self.country_position(dataset=dataset1,country='Indonesia',variable='recovered',h=193)
        ukraine_total_recoveries = self.country_position(dataset=dataset1,country='Ukraine',variable='recovered',h=193)
        spain_total_recoveries = self.country_position(dataset=dataset1,country='Spain',variable='recovered',h=193)
        our_countries_recovered = pd.concat([poland_total_recoveries, south_africa_total_recoveries, indonesia_total_recoveries, ukraine_total_recoveries, spain_total_recoveries])

        return our_countries_recovered

        
    def get_dataframe_pies(self, df):
        """ Creates a dataframe to make pie charts

            Args: df[(dataFrame)]: dataframe with required data

            Returns: Generated dataframe

            Creator: @AntonioLealDev
        """
        country_list = list(df.index.unique())
        dict_list = []
        for country in country_list:
            temp_df = df.loc[df.index==country]
            dict_list.append({"Country":country, "AV_NewDeaths":temp_df["new_deaths"].mean(), "AV_NewCases":temp_df["new_cases"].mean()})

        return pd.DataFrame(dict_list)


    def groupedby_month(self,dataset):
        """ Returns the mean and the median dataframe grouped by month
            Args: dataset 
            Creator: @JavierOlcoz
        """
        x = dataset
        x['location'] = x.index
        x = x.set_index(['date'])
        df_month_mean = x.resample('BM').mean()
        df_month_median = x.resample('BM').median()

        return df_month_mean, df_month_median


    def groupedby_10_days(self, dataset):
        """ Returns the mean and the median dataframe grouped by 10 days
            Args: dataset 
            Creator: @JavierOlcoz
        """
        x = dataset
        x['location'] = x.index
        x = x.set_index(['date'])
        df_10_days_mean = x.resample('10D').mean()
        df_10_days_median = x.resample('10D').median()

        return df_10_days_mean, df_10_days_median

    
    def groupedby_month_and_10_days(self, dataset):
        """ Returns the mean and the median dataframe grouped by month and 10 days
            Args: dataset 
            Creator: @JavierOlcoz
        """
        x = dataset
        x['location'] = x.index
        x = x.set_index(['date'])
        df_month_mean = x.resample('BM').mean()
        df_month_median = x.resample('BM').median()
        df_10_days_mean = x.resample('10D').mean()
        df_10_days_median = x.resample('10D').median()

        return df_month_mean, df_month_median, df_10_days_mean, df_10_days_median

    def list_extractor(self,df, col):
        """
        @Alex
        Function that will extract a list with the items in a column given in the argument, without repited values
            Input:
                df      : Dataframe with the data
                col     : Column of interest
            Output:
                l_col   : List with the unique references of the desired column
        """
        l_col = df[col].tolist()
        l_col = list(dict.fromkeys(l_col))

        return l_col

    def compare_list_and_keep_value(self,complete, dat_complete, filt):
        """
        @Alex
        Function that checkes two list and accumulates the values of the original one for the result of the filted one
        """
        
        if len(dat_complete) > len(filt):
            dat_filt=[0.]*len(filt)
            j = 0
            for i in range(len(complete)-1):
                try:
                    if complete[i] in filt:
                        dat_filt[j] = dat_complete[i]
                        j += 1
                    else:
                        pass
                        #dat_filt[j] = dat_complete[i]
                except:
                    print("ERROR:",i," ",dat_complete[i])
        else:
            dat_filt = [0.] + dat_complete

        return dat_filt

    def sort_and_merge_recovered(self,df_required_countries,recovered):
        """
        @Alex
        Function that gets new data of recovered data from a diferent source of covid generic data.
            Input:
                df_required_countries : Dataframe with the covid data 
                recovered             : Dataframe with recovered data
            Output:
                total                 : Dataframe with the infomation of recovered merged in the appropiate format to df_required_countries
        """

        import os
        import datetime
        
        #List with the original locations
        location = self.list_extractor(df_required_countries,"location")

        #dictionary with dates per conuntry of original frame
        dic_required_countries = {pais:df_required_countries[df_required_countries["location"]==pais]["date"].values.tolist() for pais in location} 

        # In here I got the countries that appears in the recovered df
        recovered_group = recovered.groupby("Country_EN").sum()

        # delete the index to work with Country_EN
        recovered_country = recovered_group.reset_index()

        # List of the Countries in Country_EN
        countries_rec = self.list_extractor(recovered_country,"Country_EN")

        # Countries from countries_rec that NOT appear in location
        dif_countries = [pais for pais in countries_rec if pais not in location]

        # Extract the DF with the countries of interest
        recovered_country = recovered_country[~recovered_country["Country_EN"].isin(dif_countries)]

        # list of final countries
        final_countries_rec = [pais for pais in countries_rec if pais not in dif_countries]

        # future dictionary with the values
        dic_values_date_filt={}

        # list of conflict countries
        conflict = []

        origin_date_rec = datetime.datetime.strptime("2020-01-23", '%Y-%m-%d').date()
        today = datetime.date.today()
        today = today.strftime('%Y-%m-%d')
        complete = [d.strftime('%Y-%m-%d') for d in pd.date_range("2020-01-23",today)]


        # for each country in location...
        for pais in location:
        #... we check if it's in the list of available data and...
            # ... if it's in there, we extract the data from the begining of data (23-Jan-2020)
            if pais in final_countries_rec: 
                aux = recovered_country.loc[recovered_country["Country_EN"] == pais].values.tolist() 
                clean = aux[0][1:]

            #... if it's not there, we fullfill with NaN values
            else:
                aux = [np.nan]*len(dic_required_countries[pais])
                clean = aux
                conflict.append(pais)

            # finally, we fill with the information for country
            dic_values_date_filt [pais] = clean
            
        #  for each country in location we...
        for pais in location:
            # ...first avoid the conflictive data
            if pais not in conflict:
                # ... get the date of origin from required countries and transform it to date format
                pais_date = datetime.datetime.strptime(dic_required_countries[pais][0], '%Y-%m-%d').date()
                        
                # ...if the 'pais_date' is older than 'origin_date_rec', we add the difference in value to  
                if pais_date < origin_date_rec:
                    dic_values_date_filt[pais] = [0.]*(abs((pais_date-origin_date_rec).days)) + dic_values_date_filt[pais]

                # ... if the 'origin_date_rec' is older than 'pais_date', we substract as many data as needed
                elif pais_date > origin_date_rec:           
                    dic_values_date_filt[pais] = self.compare_list_and_keep_value(complete, dic_values_date_filt[pais], dic_required_countries[pais])

        # We finally build the dict from where we'll create the DF
        loc = []
        rec = []
        dates = []
        for pais in location:
            rec = rec + dic_values_date_filt[pais]
            loc = loc + [pais]*len(dic_values_date_filt[pais])
            dates = dates + dic_required_countries[pais]

        final = {"location":loc,"date":dates,"recovered":rec}

        # Creation of the Dataframe
        result = pd.DataFrame(final)

        # Reindex for merging purposes
        df1 = df_required_countries.set_index(["location","date"])
        df2 = result.set_index(["location","date"])

        # Merge of both df
        total = pd.concat([df1,df2], axis=1, join="inner")

        # Final result
        return total
    
    def json_creator(self,df_to_convert):
        """
        @Alex
        Function that will create and save the json required by the server
            Input:
                df_to_convert   : Dataframe with the data to convert
        
        """
        import json
        import os
        
        # Group by required data
        n_v_averages = df_to_convert.groupby("date").agg({"new_vaccinations":"mean"})
        n_v_averages = n_v_averages.reset_index()
        n_v_averages = n_v_averages.values.tolist()

        # Creation of the json
        json_own = {"n_v_averages":n_v_averages}

        # Saving the file
        camino = ".." + os.sep + "reports" + os.sep + "json_own.json"
        with open(camino,'w') as json_file:
            json.dump(json_own,json_file)
