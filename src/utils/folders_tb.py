class Folders:


    import pandas as pd


    def open_csv(self, url):
        """ Read a csv file and return a df assigned to a given variable
            Args: url
            Creator: @JavierOlcoz
        """
        variable = self.pd.read_csv(url)

        return variable