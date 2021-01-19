import pandas as pd



class Miner:

    

    def chosen_countries(self, old_df, location_column, country_1, country_2, country_3, country_4, country_5):
        """ It divides the original df in others where the 'location' column is specific for the country given,
        then, it concatenates them into a single df
            Args: new dataframe name, dataframe to work with, location_column, 5 countries to work with
            Return a df with the asked countries
            Creator: @JavierOlcoz
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
            Creator: @JavierOlcoz
        """
        dataset[column_to_change] = pd.to_datetime(dataset[column_to_change], format= '%Y/%m/%d')

        return dataset

    def pivot_table_date_location(self, dataset, index_1, index_2):
        """ Creates a pivot table with the chosen index
            Args: dataset and 2 index
            Creator: @JavierOlcoz
        """
        new_df = pd.pivot_table(dataset,index=[index_1, index_2])

        return new_df

    def set_index_1(self, dataset, index_3):
        """ Sets index_3 as index
            Args: datset, index
            Creator: @JavierOlcoz
        """
        new_df = dataset.set_index(index_3)

        return new_df