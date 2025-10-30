"""läs in funktioner från metrics"""
import matplotlib.pyplot as plt
import pandas as pd


"""
Skapa olika diagram med värden från metrics
"""
def bar(ax, x, y, title, xlabel, ylabel, grid=True):
    ax.bar(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis='y')
    return ax

def box(ax, df, x, y, title, xlabel, ylabel, grid=True):
    df.boxplot(column=x, by=y, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis='y')
    ax.grid(False, axis='x')
    plt.suptitle('')
    return ax