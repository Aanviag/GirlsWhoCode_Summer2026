# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

#information
print("How has the percentage of low-quality water access changed in India from the years 1990 - 2020?")
input("\nPlease press enter to continue")
print("\nIn the 1990's many rural villages and areas in India didn't have access to clean running water within their household causing poverty and major problems for small villages and towns.During the monsoon, heavy rainfall would cause the water to be unclean, spreading high numbers of diseases, with only about 72% families having running clean water.")

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell135.csv")


oneCountryBooleanList = lwd["country_name"]=="India"
oneCountryData = lwd.loc[oneCountryBooleanList]


# Print out the number of rows and columns
print(lwd.shape)

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'

# create a scatter plot
plt.scatter(lwd["year"],lwd["HH_water_low_p"],color="red")

# add a title to the plot
plt.title("% of Household wiht low-quality Water access in different years")

#Label the x-axis
plt.xlabel("Year")

# label the y-axis
plt.ylabel("Households with low quality water access (%)")

# set the range for the y-axis
plt.xlim(1990, 2020)
plt.ylim(0, 100)

# show the plot
plt.show()

input("Please press enter to continue")
#after information
print("In early 2000's the Indian national government launched programs like 'Swajaldhara Programme' to help small communities establish running water systems and allowed them funds to keep those foundations running themselves. Since then the many efforts have been made to help improve water access.")

input("\nPlease press enter to continue.")

print("By 2020, the scatterplot shows a decrease in % of households with water quality access to over 90% of housholdsin India.")
