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
    sns.scatterplot(x=df['Height(Inches)'], y=df['Weight(Pounds)'], ax=ax)
    plt.title('Height vs Weight Relationship')
    plt.xlabel('Height (Inches)')
    plt.ylabel('Weight (Pounds)')
    plt.savefig('relational_plot.png')
    plt.close()
    return


def plot_categorical_plot(df):
    df['Height Range'] = pd.cut(df['Height(Inches)'], bins=[55, 60, 65, 70, 75, 80],
                                labels=['55-60', '60-65', '65-70', '70-75', '75-80'])
    fig, ax = plt.subplots()
    sns.barplot(x='Height Range', y='Weight(Pounds)', data=df, ax=ax, errorbar=None)
    plt.title('Average Weight by Height Range')
    plt.xlabel('Height Range (Inches)')
    plt.ylabel('Average Weight (Pounds)')
    plt.savefig('categorical_plot.png')
    plt.close()
    return


def plot_statistical_plot(df):
    fig, ax = plt.subplots()
    sns.histplot(df['Height(Inches)'], kde=True, ax=ax, bins=20, color='blue')
    plt.title('Height Distribution')
    plt.xlabel('Height (Inches)')
    plt.ylabel('Frequency')
    plt.savefig('statistical_plot.png')
    plt.close()
    return


def statistical_analysis(df, col: str):
    mean = df[col].mean()
    stddev = df[col].std()
    skew = ss.skew(df[col])
    excess_kurtosis = ss.kurtosis(df[col])
    return mean, stddev, skew, excess_kurtosis


def preprocessing(df):
    df=df.dropna()
    print("summary: ")
    print(df.describe())
    print("\nFirst 5 rows: ")
    print(df.head())
    print("\ncorrelation matrix")
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
