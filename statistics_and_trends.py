"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns


def plot_relational_plot(df):
    fig, ax = plt.subplots()
    sns.scatterplot(x=df.iloc[:, 0], y=df.iloc[:, 1], ax=ax)
    plt.savefig('relational_plot.png')
    return


def plot_categorical_plot(df):
    fig, ax = plt.subplots()
    sns.boxplot(x=df.iloc[:, 0], y=df.iloc[:, 1], ax=ax)
    plt.savefig('categorical_plot.png')
    return


def plot_statistical_plot(df):
    fig, ax = plt.subplots()
    sns.histplot(df.iloc[:, 0], kde=True, ax=ax)
    plt.savefig('statistical_plot.png')
    return


def statistical_analysis(df, col: str):
    mean = df[col].mean()
    stddev = df[col].std()
    skew = ss.skew(df[col])
    excess_kurtosis = ss.kurtosis(df[col])
    return mean, stddev, skew, excess_kurtosis


def preprocessing(df):
    df=df.dropna()
    print(df.describe())
    print(df.head())
    print(df.corr())
    return df


def writing(moments, col):
    print(f'For the attribute {col}:')
    print(f'Mean = {moments[0]:.2f}, '
          f'Standard Deviation = {moments[1]:.2f}, '
          f'Skewness = {moments[2]:.2f}, and '
          f'Excess Kurtosis = {moments[3]:.2f}.')
    skewness = "right-skewed" if moments[2] > 0 else "left-skewed" if moments[2] < 0 else "not skewed"
    kurtosis = "leptokurtic" if moments[3] > 0 else "platykurtic" if moments[3] < 0 else "mesokurtic"
    print(f'The data was {skewness} and {kurtosis}.')
    return


def main():
    df = pd.read_csv('data.csv')
    df = preprocessing(df)
    col ='Height(Inches)'
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    return


if __name__ == '__main__':
    main()
