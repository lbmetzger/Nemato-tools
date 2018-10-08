import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from argparse import ArgumentParser,FileType


def make_option_parser():
    parser = argparse.ArgumentParser(description = "load the file")
    parser.add_argument("-f", dest = "thefile", help = "enter file name along with location")
    parser.add_argument("-x", dest = "x_value", help = "enter the name of your x-value column")
    parser.add_argument("-y1", dest = "y1_value", help = "enter the name of your y1-value column")
    parser.add_argument("-y2", dest = "y2_value", help = "enter the name of your y2-value column")
    parser.add_argument("-o", dest = "output", type = FileType('w', encoding='UTF-8'), default='results.txt', help ='enter the \
    name that you would like for output file')
    return parser

def print_file_name(filename):
    file_msg = "The file being used is %s" %filename
    print(file_msg)

def pandas_data_x(filename, x_value):
    df = pd.read_csv(filename)
    x_val = df[[x_value]]
    return x_val

def pandas_data_y1(filename, y1_value):
    df = pd.read_csv(filename)
    y1_val = df[[y1_value]]
    return y1_val

def pandas_data_y2(filename, y2_value):
    df = pd.read_csv(filename)
    y2_val = df[[y2_value]]
    return y2_val

def sample_plot(x_val, y1_val):
    plt.plot(x_val, y1_val)
    plt.xlabel('x-column')
    plt.ylabel('y-column')
    plt.title('Simple Plot')
    plt.grid(True)
    plt.savefig("fig.png")
    plt.show()
#add more plots as a option, ie plot 1, 2, 3 etc all correspond to different figures


def sample_OLSregression(x_val, y1_val):
    model = sm.OLS(x_val, y1_val)
    results = model.fit()
    print(results.summary())
#need to add way to have multiple values, should be accessable by a command from user.  ie -r 2 is two sample, -r3 is 3 sample, etc.


def main():
      parser = make_option_parser()
      args = parser.parse_args()
      print_file_name(filename = args.thefile)
      x_val = pandas_data_x(filename = args.thefile, x_value = args.x_value)
      y1_val = pandas_data_y1(filename = args.thefile, y1_value = args.y1_value)
      #y2_val = pandas_data_y2(filename = args.thefile, y2_value = args.y2_value)
      sample_plot(x_val, y1_val)
      sample_OLSregression(x_val, y1_val)





if __name__ == "__main__":
  main()
