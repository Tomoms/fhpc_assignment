#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from sys import argv

# Read the three CSV files
df1 = pd.read_csv(f"{argv[1]}/results_blis.csv") # blis
df2 = pd.read_csv(f"{argv[1]}/results_oblas.csv") # oblas
df3 = pd.read_csv(f"{argv[1]}/results_mkl.csv") # mkl

if "intel" in argv[1]:
	tpp = 3994
	mach = "intel"
else:
	mach = "amd"
	tpp = 5324

if "double" in argv[1]:
	tpp = tpp // 2

# Group the rows by 'size' and calculate the average of 'gflops' for each file
grouped_df1 = df1.groupby('size')['gflops'].mean().reset_index()
grouped_df2 = df2.groupby('size')['gflops'].mean().reset_index()
grouped_df3 = df3.groupby('size')['gflops'].mean().reset_index()

# Merge the three dataframes together based on the 'size' column
merged_df = pd.merge(grouped_df1, grouped_df2, on='size', suffixes=("_blis", "_oblas"))
merged_df = pd.merge(merged_df, grouped_df3, on='size', suffixes=("", "_mkl"))
merged_df['tpp'] = tpp

# Generate the plot
plt.plot(merged_df['size'], merged_df['gflops'], label='mkl')
plt.plot(merged_df['size'], merged_df['gflops_blis'], label='blis')
plt.plot(merged_df['size'], merged_df['gflops_oblas'], label='oblas')
plt.plot(merged_df['size'], merged_df['tpp'], label="tpp", linestyle="dashed")

plt.xlabel('Size')
plt.ylabel('GFLOPS')
plt.title('Average GFLOPS by Size')

plt.legend()
plt.savefig(fname=f"plot_fcem_{mach}.png")
