print("==================")
print("IMPORTS AND SET UP")
print("==================")

# Import libraries
import utils.folders_tb as ft
import utils.mining_data_tb as mdt
import utils.visualization_tb as vis
import utils.apis_tb as ap
print(" > Libraries loaded...")

# Create objects
variable_creator = ft.Folders()
variable_miner = mdt.Miner()
variable_visual = vis.Visualization()
variable_apis = ap.Apis()
print(" > Class objects created...")

# Constants for the API call
passwords = {"group_id":"E80"}
# url_b = "http://81.40.88.247:5001/" # Javi Olcoz
url_b = "http://192.168.0.21:5000/" # Alex B
# url_b = "http://37.14.156.84:5001/" # Antonio
url_add = {"group_id": "group_id?password=" , "token": "token_id?password="}
print(" > Connectivity constants defined...\n")

print("============")
print("DATA READING")
print("============")

# Assign the df to a first variable called first_visualitation
first_visualitation_raw = variable_creator.open_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')

# Data of recovered
recovered = variable_creator.open_csv("https://covid19tracking.narrativa.com/csv/recovered.csv") 

# Trying to obtain the data from the server, in case it fails, returns the last version of the doc stored
d_json = variable_apis.requester(url_b,url_add,passwords)
print(" > Raw data readed...\n")

print("=============")
print("DATA CLEANING")
print("=============")

# Merge the dataframes of 'first_visualitation' and 'recovered'in 'first_visualitation'
first_visualitation = variable_miner.sort_and_merge_recovered(first_visualitation_raw,recovered) 

# Clean the dataframe in order to have just the asked countries
df_required_countries = variable_miner.chosen_countries(first_visualitation,'location', 'Poland', 'South Africa', 'Ukraine', 'Indonesia', 'Spain')

# Creation of the json file for the server 
variable_miner.json_creator(df_required_countries) 

# Turn the date column (string) into datetime.
df_required_countries = variable_miner.column_to_datetime(df_required_countries, 'date')

# Pivot table with date and countries as index (evolution per date)
# date_location_pivot_table = variable_miner.pivot_table_date_location(df_required_countries,'date', 'location')

# Better visualitation of the dataframe having the countries as index
df_required_countries = variable_miner.set_index_1(df_required_countries, 'location')
print(" > Dataframes reformatted por beter analysis...")

# df droping the constant values columns 
df_no_constant_1 = variable_miner.no_constant_df(df_required_countries,'Poland','South Africa','Indonesia','Ukraine','Spain')
df_no_constant = variable_miner.set_index_1(df_no_constant_1, 'location')

# df droping "... per..." columns
df_no_per = variable_miner.drop_per_columns(df_required_countries)

# df droping the constant values columns and "... per..." columns
df_no_constant_no_per_1 = variable_miner.no_constant_df(df_no_per,'Poland','South Africa','Indonesia','Ukraine','Spain')
df_no_constant_no_per = variable_miner.set_index_1(df_no_constant_no_per_1, 'location')
print(" > Undesired data dropped...")

# masking dfs
# all columns masked
df_required_countries_masked = variable_miner.neg_to_nan_complete(df_required_countries)

# no constants masked
df_no_constant_masked = variable_miner.neg_to_nan_complete(df_no_constant)

# no "per" masked
df_no_per_masked = variable_miner.neg_to_nan_complete(df_no_per)

# no constants, no "per", masked
df_no_constant_no_per_masked = variable_miner.neg_to_nan_complete(df_no_constant_no_per)
print(" > Outliers and incorrect values fixed...")

### poland dfs:
# df poland, masked
df_poland_masked = variable_miner.by_country(df_required_countries_masked, 'Poland')

#df poland, masked, no "per"
df_poland_masked_no_per = variable_miner.drop_per_columns(df_poland_masked)

### South Africa dfs:
# df south africa, masked
df_south_africa_masked = variable_miner.by_country(df_required_countries_masked, 'South Africa')

#df South Africa, masked, no "per"
df_south_africa_masked_no_per = variable_miner.drop_per_columns(df_south_africa_masked)

### indonesia dfs:
# df indonesia, masked
df_indonesia_masked = variable_miner.by_country(df_required_countries_masked, 'Indonesia')

#df indonesia, masked, no "per"
df_indonesia_masked_no_per = variable_miner.drop_per_columns(df_indonesia_masked)

### ukraine dfs:
# df ukraine, masked
df_ukraine_masked = variable_miner.by_country(df_required_countries_masked, 'Ukraine')

#df ukraine, masked, no "per"
df_ukraine_masked_no_per = variable_miner.drop_per_columns(df_ukraine_masked)

### spain dfs:
# df spain, masked
df_spain_masked = variable_miner.by_country(df_required_countries_masked, 'Spain')

#df spain, masked, no "per"
df_spain_masked_no_per = variable_miner.drop_per_columns(df_spain_masked)

#dataframe for pies
df_pie = variable_miner.get_dataframe_pies(df_required_countries)

#Progression by 10 days and monthly
# Poland
df_month_mean_poland, df_month_median_poland, df_10_days_mean_poland, df_10_days_median_poland = variable_miner.groupedby_month_and_10_days(df_poland_masked) 

# South Africa
df_month_mean_south_africa, df_month_median_south_africa, df_10_days_mean_south_africa, df_10_days_median_south_africa = variable_miner.groupedby_month_and_10_days(df_south_africa_masked)

# Indonesia
df_month_mean_indonesia, df_month_median_indonesia, df_10_days_mean_indonesia, df_10_days_median_indonesia = variable_miner.groupedby_month_and_10_days(df_indonesia_masked)

# Ukraine
df_month_mean_ukraine, df_month_median_ukraine, df_10_days_mean_ukraine, df_10_days_median_ukraine = variable_miner.groupedby_month_and_10_days(df_ukraine_masked)

# Spain
df_month_mean_spain, df_month_median_spain, df_10_days_mean_spain, df_10_days_median_spain = variable_miner.groupedby_month_and_10_days(df_spain_masked)
print(" > Required dataframes generated...\n")

print("=============")
print("DATA ANALYSIS")
print("=============")
# Function that calculates the correlation matrix for all of the assigned variables
highest_poland_correlation, highest_south_africa_correlation, highest_indonesia_correlation, highest_ukraine_correlation, \
    highest_spain_correlation, top_10_highest_poland_correlation, top_10_highest_south_africa_correlation, top_10_highest_indonesia_correlation,\
    top_10_highest_ukraine_correlation, top_10_highest_spain_correlation = variable_miner.matrix_high_correlation(dataset1=df_poland_masked_no_per,\
    dataset2= df_south_africa_masked_no_per, dataset3= df_indonesia_masked_no_per, dataset4=df_ukraine_masked_no_per, dataset5=df_spain_masked_no_per)
print(" > Correlation matrices calculated...\n")

print("===========")
print("PLOT MAKING")
print("===========")
# Tendency plots
y = ["total_cases", "total_deaths", "new_cases_smoothed", "new_deaths_smoothed"]
ylabel = ["Total cases(L)", "Total deaths(R)", "New cases(R)", "New deaths(R)"]
yaxis = [False, True, True, True]
variable_visual.tendency_plots_wrapper(df_required_countries_masked, y, ylabel, yaxis)
print(" > Tendency plots generated...")

# Visualization of all matrix
poland_matrix, south_africa_matrix, indonesia_matrix, ukraine_matrix, spain_matrix, \
    top_poland_matrix, top_south_africa_matrix, top_indonesia_matrix, top_ukraine_matrix, \
    top_spain_matrix = variable_visual.all_matrix_visualization(highest_poland_correlation, \
    highest_south_africa_correlation, highest_indonesia_correlation, highest_ukraine_correlation, \
    highest_spain_correlation, top_10_highest_poland_correlation, top_10_highest_south_africa_correlation,\
    top_10_highest_indonesia_correlation, top_10_highest_ukraine_correlation, top_10_highest_spain_correlation)
print(" > Correlation matrices plotted...")

# Pie charts for new_cases and new deaths
colors = ["#ff9633", "#8df877", "#52c8e8", "#6a5ef1", "#fa3939"]
variable_visual.make_pies(df_pie, "Country", "Country", "AV_NewDeaths", "AV_NewCases", colors, "Average daily deaths", "Average daily cases")
print(" > Pie charts plotted...")

# Scatter, Line and bar plots for new_cases and new deaths (by country)
variable_visual.variety_plot_wrapper(df_required_countries_masked)
print(" > Cases and deaths plots (bar, line, scatter) generated...")

# New deaths plot
import datetime as dt
lines = [[dt.datetime(2020, 3, 27), dt.datetime(2020, 4, 30), dt.datetime(2020, 9, 27), dt.datetime(2020, 11, 25), dt.datetime(2020, 12, 28)], \
         [dt.datetime(2020, 5, 18), dt.datetime(2020, 8, 10), dt.datetime(2020, 12, 2)], \
         [dt.datetime(2020, 4, 1), dt.datetime(2020, 12, 12), dt.datetime(2021, 1, 14)], \
         [dt.datetime(2020, 3, 17), dt.datetime(2020, 9, 25), dt.datetime(2020, 11, 11)], \
         [dt.datetime(2020, 3, 11), dt.datetime(2020, 4, 3), dt.datetime(2020, 8, 11), dt.datetime(2020, 11, 9), dt.datetime(2021, 1, 6)]]
variable_visual.new_deaths_plot(df_required_countries_masked, lines)
print(" > New deaths tendencies plotted...")

# representing the json file
df_json = variable_miner.json_prep_plot(d_json)

variable_visual.make_lineplot(data=df_json, x='Date', y='Total Deaths Mean', x_label='DATE',\
     y_label='Total Deaths Mean', title='ANNEXED GROUP JSON LINE PLOT')
variable_visual.make_barplot(data=df_json, x='Date', y='Total Deaths Mean', x_label='DATE',\
     y_label='Total Deaths Mean', title='ANNEXED GROUP JSON BAR PLOT')
print(" > JSON file plotted...")

#Make plot for new cases, grouped by day, 10 days and month
variable_visual.plot_resampled_evolution(df_poland_masked, df_10_days_mean_poland, df_month_mean_poland, "Poland")
variable_visual.plot_resampled_evolution(df_south_africa_masked, df_10_days_mean_south_africa, df_month_mean_south_africa, "South Africa")
variable_visual.plot_resampled_evolution(df_indonesia_masked, df_10_days_mean_indonesia, df_month_mean_indonesia, "Indonesia")
variable_visual.plot_resampled_evolution(df_ukraine_masked, df_10_days_mean_ukraine, df_month_mean_ukraine, "Ukraine")
variable_visual.plot_resampled_evolution(df_spain_masked, df_10_days_mean_spain, df_month_mean_spain, "Spain")
print(" > Resampled plots generated...")









