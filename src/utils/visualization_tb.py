# visualization_tb.py 
# Created by: Antonio J. Leal
# Last review: 19/01/2021, by Javier Olcoz

# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime as dt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

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

    def plot_tendency(x, y_series, x_label, y_label, set_labels, label_rotation, title, date, path, vlines, vline_colors = ["r"], vline = False, legend = True):
        """ Make a lineplot of one or several series. Vertical lines can be added.
            Saves the plot to file. Made by @AntonioLealDev

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

    def make_barplot(data, x, y, x_label, y_label, title):
        """ Makes plotly barplot and saves it.

            Creator: @AntonioLealDev

            Args: data[(DataFrame)]: Dataframe to be plotted
                  x[(string)]: Name of the column to be used as x axis
                  y[(string)]: Name of the column to be used as y axis
                  x_label[(string)]: X-axis label
                  y_label[(string)]: Y-axis label
                  title[(string)]: Plot title

            Returns: none
        """
        fig = px.bar(data, x=x, y=y, template="seaborn",\
                labels={
                    y:"<b>"+ y_label +"</b>",
                    x:"<b>"+ x_label +"</b>",
                },
                title='<span style="font-size: 26px;"><b>'+title+'</b></span>')

        fig.update_layout(title={"y":0.92})
        fig.show()

    def make_lineplot(data, x, y, x_label, y_label, title):
        """ Makes plotly lineplot and saves it.

            Creator: @AntonioLealDev

            Args: data[(DataFrame)]: Dataframe to be plotted
                  x[(string)]: Name of the column to be used as x axis
                  y[(string)]: Name of the column to be used as y axis
                  x_label[(string)]: X-axis label
                  y_label[(string)]: Y-axis label
                  title[(string)]: Plot title

            Returns: none
        """
        fig = px.line(data, x=x, y=y, template="seaborn",\
                labels={
                    y:"<b>"+ y_label +"</b>",
                    x:"<b>"+ x_label +"</b>",
                },
                title='<span style="font-size: 26px;"><b>'+country+'</b></span>')

        fig.update_layout(title={"y":0.92})
        fig.show()

    def make_scatter(data, x, y, x_label, y_label, title):
        """ Makes plotly scatter plot and saves it to html

            Creator: @AntonioLealDev

            Args: data[(DataFrame)]: Dataframe to be plotted
                  x[(string)]: Name of the column to be used as x axis
                  y[(string)]: Name of the column to be used as y axis
                  x_label[(string)]: X-axis label
                  y_label[(string)]: Y-axis label
                  title[(string)]: Plot title

            Returns: none
        """
        fig = px.scatter(data, x=x, y=y, template="seaborn",\
                labels={
                    y:"<b>"+ y_label +"</b>",
                    x:"<b>"+ x_label +"</b>",
                },
                title='<span style="font-size: 26px;"><b>'+country+'</b></span>')

        fig.update_layout(title={"y":0.92})
        fig.update_traces(marker=dict(size=4))
        fig.show()

    def make_pies(data, p1_label, p2_label, p1_values, p2_values, colors, p1_title, p2_title):
        """ Make double pie plot. Saves it to html

            Creator: @AntonioLealDev

            Args: data[(DataFrame)]: Dataframe to be plotted
                  p1_label[(str)]: Name of the column containing pie 1 labels
                  p2_label[(str)]: Name of the column containing pie 2 labels
                  p1_values[(str)]: Name of the column containing pie 1 values
                  p2_values[(str)]: Name of the column containing pie 2 values
                  colors[(list)]: List of colors for pie sectors
                  p1_title[(str)]: Title for pie 1
                  p2_title[(str)]: Title for pie 2

            Returns: None
        """
        fig = make_subplots(rows=1, cols=2, specs=[[{"type":"pie"}, {"type":"pie"}]],
                            subplot_titles=['<b>'+p1_title+'</b>', '<b>'+p2_title+'</b>'])

        fig.add_trace(go.Pie(labels=data[p1_label], values=data[p1_values], pull=[0,0,0,0,0.1], hole=0.1), row=1, col=1)
        fig.add_trace(go.Pie(labels=data[p2_label], values=data[p2_values], pull=[0,0,0,0,0.1], hole=0.1), row=1, col=2)

        fig.update_traces(hoverinfo='label+value', textinfo='percent', \
                        marker=dict(colors=colors, line=dict(color='#000000', width=0.5)))
        fig.update_layout(legend=dict(orientation="h", yanchor="bottom", xanchor="center", y=-0.1, x=0.5),
                        font=dict(color="Black"))
                        
        fig.show()