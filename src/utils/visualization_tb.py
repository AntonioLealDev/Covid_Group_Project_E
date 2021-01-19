# visualization_tb.py 
# Created by: Antonio J. Leal
# Last review: XX/XX/XXXX, by XXXXXXXXXX

class Visualization:
    # Import libraries
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    import datetime as dt

    def plot_tendency(x, y_series, x_label, y_label, set_labels, label_rotation, title, date, path, vlines, vline_colors, vline = False, legend = True):
        """ Make a lineplot of one or several series. Vertical lines can be added.
            Saves the plot to file. 
            
            Creator: @AntonioLealDev

            Args: x [(pd.Series)]: Series for x axis
                  y [(list)]: List of series to be plotted in the y axis
                  x_label [(str)]: Label for the x axis
                  y_label [(str)]: Label for the y axis
                  set_labels[(list)]: List of string for series labels
                  label_rotation[(float)]: Rotation for the x axis labels
                  title[(str)]: Plot title
                  date[list]: List of datetimes for vertical lines
                  path[(str)]: Path where the plot will be saved
                  vlines[(int)]: Number of vertical lines
                  vline_colors[(list)]: List of strings representing vertical line colors
                  vline[(bool)]: True: draw vertical line, False: otherwise (default False)
            
            Returns: None
        """
        # Setting lineplots
        plot = plt.figure()
        for i in range(len(y_series)):
            sns.lineplot(x=x, y=y_series[i], label=set_labels[i])

        # Setting axes
        plt.xticks(rotation=label_rotation)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        # Add legend
        if not legend:
            plt.legend("", frameon=False)

        # Add vertical line
        if vline:
            for i in range(vlines):
                plt.axvline(date[i], c=vline_colors[i])

        # Save plot to file
        plot.savefig(path, dpi=plot.dpi)