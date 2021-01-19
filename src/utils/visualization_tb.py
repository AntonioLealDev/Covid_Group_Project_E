# visualization_tb.py 
# Created by: Antonio J. Leal
# Last review: 19/01/2021, by Javier Olcoz


# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime as dt

class Visualization:
    
    
    def plot_tendency(self, x, y_series, x_label, y_label, set_labels, label_rotation, title, date, path, vlines, vline_colors, vline = False, legend = True):
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


    def correlation_matrix(self, matrix, title_1):
        """ Plot the correlation matrix
            Args: correlation matrix, title
            Creator: @JavierOlcoz
        """
        plt.title(title_1)
        sns.heatmap(matrix, cmap="BrBG", annot=True)
        return plt.show()