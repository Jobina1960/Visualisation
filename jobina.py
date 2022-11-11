#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 18:49:12 2022

@author: asus
"""

#imported modules
import pandas as pd
import matplotlib.pyplot as plt

# read file into dataframe and print
df = pd.read_csv("jobna.csv")
print(df)

def multiline() :
    """
     function for multiline plot for showing birth rates in 1985, 1963, 2002

    """
    
    plt.figure(figsize = (10,12))
    plt.plot(df["CountryCode"], df["1985"], 
         label = "1985")
    plt.plot(df["CountryCode"], df["1963"], 
         label = "1963")
    plt.plot(df["CountryCode"], df["2002"], 
         label = "2002")
    plt.xlabel("CountryCode")
    plt.ylabel("Birth Rate")
    plt.legend()
    plt.title("multiline plot showing birth rate")
# saving figure
    plt.savefig("linegraph.png")
    plt.show()

def line() :
    """
    function for lineplot for showing the birth rate in 1960.

    """
    
    plt.figure(figsize = (10,12))
    plt.plot(df["CountryCode"], df["1960"], 
         label = "1960")
    plt.xlabel("CountryCode")
    plt.ylabel("Birth Rate")
    plt.legend()
    plt.title("Line plot showing birth rate")
# saving figure
    plt.savefig("linegraph.png")
    plt.show()
    
def barChart() :
    """
    Function for the bar chart for plotting the birth rate in 1986 and 2015
    """
# Plot the figure
    plt.figure(figsize = (10,10))
# plot the temperatures of different cities.
    plt.bar(df["CountryCode"], df["1986"], 
            label = "1986", alpha = 1.0, color = 'orange')
    plt.bar(df["CountryCode"], df["2015"], 
            label = "2015", alpha=0.6, color = 'yellow')
   
# set labels and show the legend    
    plt.xlabel("Station.City")
    plt.ylabel("Birth Rate")
    plt.title("Bar graph showing birth rates for the year 1986 and 2015")
# saving figure
    plt.savefig("barchart_png")
    plt.legend()
    plt.show()
    
# function for the box plot
def boxPlot() :
    """
    Function for the box plot. It plots the 2015, 1986, 1960.
    """
# plot the figure
    plt.figure(figsize = (8,9))
# plot the temperatures of different cities.
    plt.boxplot([df["2015"],
                 df["1986"],
                 df["1960"]], 
                labels = ["2015",
                          "1986",
                          "1960"])
 
# set labels and show the legend
   
    plt.ylabel("Birth rates")
    plt.title("Box plot showing birth rates")
# saving figure
    plt.savefig("boxfig_png")
    plt.legend()
    plt.show()

# calling the functions for boxplot, multiline, line and barchart.    
boxPlot()
multiline()
line()
barChart()