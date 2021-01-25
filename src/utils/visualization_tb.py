# visualization_tb.py 
# Created by: Antonio J. Leal
# Last review: 25/01/2021, by Antonio Leal

# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime as dt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

class Visualization:
    def path_saver(self,cat,file_name):
        """
        @Alex
        Path creator to save the files in the appropiate format.
            Input:
                cat         : Cathegory of folder to be save 
                file_name   : Name of the file
            
            Output:
                path        : Path merged 
        """
        import os

        path = os.path.abspath(os.path.join(".." + os.sep + "resources" + os.sep + "plots" + os.sep + cat + os.sep + file_name))
        
        return path
        
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

    def all_matrix_visualization(self, dataset1, dataset2, dataset3, dataset4, dataset5, dataset6, dataset7, dataset8, dataset9, dataset10):
        """ Visualizes all the matrix in one command line
            Args:
            Creator: @JavierOlcoz
        """
        poland_matrix = self.correlation_matrix(matrix=dataset1, title_1='POLAND CORRELATION')
        south_africa_matrix = self.correlation_matrix(matrix=dataset2, title_1='SOUTH AFRICA CORRELATION')
        indonesia_matrix = self.correlation_matrix(matrix=dataset3, title_1='INDONESIA CORRELATION')
        ukraine_matrix = self.correlation_matrix(matrix=dataset4, title_1='UKRAINE CORRELATION')
        spain_matrix = self.correlation_matrix(matrix=dataset5, title_1='SPAIN CORRELATION')

        top_poland_matrix = self.correlation_matrix(matrix=dataset6, title_1='POLAND TOP 10 CORRELATION')
        top_south_africa_matrix = self.correlation_matrix(matrix=dataset7, title_1='SOUTH AFRICA TOP 10 CORRELATION')
        top_indonesia_matrix = self.correlation_matrix(matrix=dataset8, title_1='INDONESIA TOP 10 CORRELATION')
        top_ukraine_matrix = self.correlation_matrix(matrix=dataset9, title_1='UKRAINE TOP 10 CORRELATION')
        top_spain_matrix = self.correlation_matrix(matrix=dataset10, title_1='SPAIN TOP 10 CORRELATION')

        return poland_matrix, south_africa_matrix, indonesia_matrix, ukraine_matrix, spain_matrix, top_poland_matrix, top_south_africa_matrix, top_indonesia_matrix, top_ukraine_matrix, top_spain_matrix

    def plot_tendency_1(self, x, y_series, x_label, y_label, set_labels, label_rotation, title, date, path, vlines, vline_colors = ["r"], vline = False, legend = True):
        """ Make a lineplot of one or several series. Vertical lines can be added. Saves it to html and jpg
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

    def make_barplot(self, data, x, y, x_label, y_label, title):
        """ Makes plotly barplot and saves it. Saves it to html and jpg

            Creator: @AntonioLealDev
            Reviewer: @Alex

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

        path_static = self.path_saver("static","barplot_")
        path_html = self.path_saver("html","barplot_")       

        fig.write_image(path_static + y + "_" + title + ".png")
        fig.write_html(path_html + y + "_" + title + ".html")
        #fig.show()

    def make_lineplot(self, data, x, y, x_label, y_label, title):
        """ Makes plotly lineplot and saves it. Saves it to html and jpg

            Creator: @AntonioLealDev
            Reviewer: @Alex

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
                title='<span style="font-size: 26px;"><b>'+title+'</b></span>')

        fig.update_layout(title={"y":0.92})

        path_static = self.path_saver("static","lineplot_")
        path_html = self.path_saver("html","lineplot_")

        fig.write_image(path_static + y + "_" + title + ".png")
        fig.write_html(path_html + y + "_" + title + ".html")
        #fig.show()

    def make_scatter(self, data, x, y, x_label, y_label, title):
        """ Makes plotly scatter plot and saves it to html and jpg

            Creator: @AntonioLealDev
            Reviewer: @Alex

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
                title='<span style="font-size: 26px;"><b>'+title+'</b></span>')

        fig.update_layout(title={"y":0.92})
        fig.update_traces(marker=dict(size=4))

        path_static = self.path_saver("static","scatterplot_")
        path_html = self.path_saver("html","scatterplot_")

        fig.write_image(path_static + y + "_" + title + ".png")
        fig.write_html(path_html + y + "_" + title + ".html")
        #fig.show()

    def make_pies(self, data, p1_label, p2_label, p1_values, p2_values, colors, p1_title, p2_title):
        """ Make double pie plot. Saves it to html and jpg

            Creator: @AntonioLealDev
            Reviewer: @Alex

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
        
        path_static = self.path_saver("static","pieplot.png")
        path_html = self.path_saver("html","pieplot.png")

        fig.write_image(path_html)
        fig.write_html(path_static)            
        #fig.show()

    def variety_plot_wrapper(self, data):
        """ Prepares several plots to be done. Saves to html and jpg.

            Creator: @AntonioLealDev

            Args: data[(DataFrame)]: Dataframe to be plotted

            Returns: none
        """
        #Get country list
        country_list = list(data.index.unique())
        for i in range(len(country_list)):
            c_df = data.loc[data.index == country_list[i]]
            # Values for plotting
            columns = ["new_cases_smoothed", "new_deaths_smoothed"]
            labels = ["New cases", "New deaths"]
            # Make plots
            for j in range(2):
                self.make_barplot(c_df, "date", columns[j], "Date", labels[j], country_list[i])
                self.make_lineplot(c_df, "date", columns[j], "Date", labels[j], country_list[i])
                self.make_scatter(c_df, "date", columns[j], "Date", labels[j], country_list[i])

    def tendency_plots_wrapper(self, data, y, ylabel, yaxis):
        """ Prepares tendency&lockdown plots to be done. Saves to html and jpg.

            Creator: @AntonioLealDev

            Args: data[(DataFrame)]: Dataframe to be plotted
                  y[(list)]: List of the names of the columns (string) used as y-axes
                  ylabel[(list)]: List of labels for y-axes data
                  yaxis[(list)]: List of bools for each column ploted. True: Right y-axis, False: Otherwise

            Returns: None
        """
        country_list = list(data.index.unique())
        linecolors = ["red", "green"]
        
        lines = []
        lines.append([[dt.datetime(2020, 3, 13), 0, 2500000], [dt.datetime(2020, 5, 4), 0, 2500000]])
        lines.append([[dt.datetime(2020, 3, 26), 0, 1400000], [dt.datetime(2020, 5, 1), 0, 1400000]])
        lines.append([[dt.datetime(2020, 3, 17), 0, 1250000], [dt.datetime(2020, 5, 11), 0, 1250000]])
        lines.append([[dt.datetime(2020, 3, 26), 0, 1000000], [dt.datetime(2020, 7, 31), 0, 1000000]])
        lines.append([[dt.datetime(2020, 3, 14), 0, 2500000], [dt.datetime(2020, 5, 11), 0, 2500000]])

        for i in range(len(country_list)):
            c_data = data.loc[data.index == country_list[i]]
            self.tendency_and_lockdown(c_data, "date", "Date", y, ylabel, yaxis, lines[i], linecolors, country_list[i])


    def tendency_and_lockdown(self, data, x, xlabel, y, ylabel, yaxis, lines, linecolors, title):
        """ Generates line plots with 2 axes and several data. Adds vertical lines too. Saves to html and jpg

            Creator: @AntonioLealDev
            Reviewer: @Alex

            Args: data[(DataFrame)]: Dataframe to be plotted
                  x[(str)]: Name of the column used as x-axis
                  xlabel[(str)]: Label for x-axis data
                  y[(list)]: List of the names of the columns (string) used as y-axes
                  ylabel[(list)]: List of labels for y-axes data
                  yaxis[(list)]: List of bools for each column ploted. True: Right y-axis, False: Otherwise
                  lines[(list)]: List of data for vertical line plotting [x, y0, y1]
                  linecolors[(list)]: List of CSS colors for vertical lines
                  title[(str)]: Plot title

            Returns: None
        """ 
        fig = make_subplots(specs=[[{"secondary_y":True}]])

        # Add data plots
        for i in range(len(y)):
            fig.add_trace(go.Scatter(x=data[x], y=data[y[i]], mode="lines", name=ylabel[i]), secondary_y=yaxis[i])

        # Set legend and title
        fig.update_layout(legend=dict(orientation="h", yanchor="bottom", xanchor="center", y=-0.2, x=0.475), font=dict(color="Black"),\
                          title={"text":'<span style="font-size: 26px;"><b>'+title+'</b></span>', "x":0.5})

        # Add vertical lines
        for i in range(len(lines)):
            fig.add_shape(type="line", x0=lines[i][0], y0=lines[i][1], x1=lines[i][0], y1=lines[i][2], line=dict(color=linecolors[i], width=2, dash="dashdot"))

        path_static = self.path_saver("static","lockdowns")
        path_html = self.path_saver("html","lockdowns")

        fig.write_html(path_html + title + ".html")
        fig.write_image(path_static + title + ".png")
        
        #fig.show()

    
    def new_deaths_plot(self, data, lines):
        """ Generates line plot with several vertical lines. Saves to html and jpg

            Creator: @AntonioLealDev
            Reviewer: @Alex

            Args: data[(DataFrame)]: Dataframe to be plotted
                  lines[(list)]: list with x values (dates) for vertical line plot
                  y[(list)]: List of the names of the columns (string) used as y-axes

            Returns: None
        """
        # Get country list
        country_list = list(data.index.unique())

        # Make plot for every country
        for i in range(len(country_list)):  
            c_data = data.loc[data.index == country_list[i]]
            fig = px.line(c_data, x="date", y="new_deaths_smoothed", template="seaborn",\
                    labels={
                        "date":"<b>New daily deaths</b>",
                        "new_deaths_smoothed":"<b>Date</b>",
                    },
                    title='<span style="font-size: 26px;"><b>'+country_list[i]+'</b></span>')

            for j in range(len(lines[i])):
                colors = ["red" if i%2==0 else "green" for i in range(len(lines[i]))]
                fig.add_shape(type="line", x0=lines[i][j], y0=0, x1=lines[i][j], y1=c_data["new_deaths_smoothed"].max(), \
                              line=dict(color=colors[j], width=2, dash="dashdot"))

            path_static = self.path_saver("static","death_tendency")
            path_html = self.path_saver("html","death_tendency")

            fig.write_image(path_static + country_list[i] + ".png")
            fig.write_html(path_html + country_list[i] + ".html")

    def plot_resampled_evolution(self, data, data10, dataM, country):
        """ Creates a plot with the evolution of new cases with data grouped by day, 10 days and months

            Creator: @AntonioLealDev

            Args: data[(DataFrame)]: Dataframe to be plotted (grouped daily)
                  data10[(DataFrame)]: Dataframe to be plotted (grouped by 10 days)
                  dataM[(DataFrame)]: Dataframe to be plotted (grouped by month)
                  country[(str)]: Name of the country

            Returns: None
        """
        #Create Figure
        fig = go.Figure()

        #Add traces
        fig.add_trace(go.Scatter(x=data["date"], y=data["new_cases_smoothed"], mode="lines", name="Daily"))
        fig.add_trace(go.Scatter(x=data10.index, y=data10["new_cases_smoothed"], mode="markers+lines", name="10 Days"))
        fig.add_trace(go.Scatter(x=dataM.index, y=dataM["new_cases_smoothed"], mode="markers+lines", name="Monthly"))

        #Set Layout
        fig.update_layout(title={"text":'<span style="font-size: 26px;"><b>Evolution of new cases ('+country+')</b></span>', "x":0.5}, \
                                 xaxis_title="Date", yaxis_title="New cases")
        
        path_static = self.path_saver("static","death_tendency")
        path_html = self.path_saver("html","death_tendency")

        fig.write_image(path_static + country + ".png")
        fig.write_html(path_html + country + ".html")

        #fig.show()
