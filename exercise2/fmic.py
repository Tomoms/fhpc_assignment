#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from sys import argv

# Read the three CSV files
df1 = pd.read_csv(f"{argv[1]}/results_blis.csv") # blis
df2 = pd.read_csv(f"{argv[1]}/results_oblas.csv") # oblas
df3 = pd.read_csv(f"{argv[1]}/results_mkl.csv") # mkl

mach = "amd"
if "intel" in argv[1]:
	mach = "intel"

policy = "coresclose"
if "spread" in argv[1]:
	policy = "coresspread"

tpp = 3994 // 24
if "amd" in argv[1]:
	tpp = 10648 // 128

datatype = "float"
if "double" in argv[1]:
	datatype = "double"
	tpp = tpp // 2

# Group the rows by 'cores' and calculate the average of 'gflops' for each file
grouped_df1 = df1.groupby('cores')['gflops'].mean().reset_index()
grouped_df2 = df2.groupby('cores')['gflops'].mean().reset_index()
grouped_df3 = df3.groupby('cores')['gflops'].mean().reset_index()

# Merge the three dataframes together based on the 'size' column
merged_df = pd.merge(grouped_df1, grouped_df2, on='cores', suffixes=("_blis", "_oblas"))
merged_df = pd.merge(merged_df, grouped_df3, on='cores', suffixes=("", "_mkl"))
merged_df['tpp'] = 0
i = 0
for el in merged_df['cores']:
	merged_df.loc[i, 'tpp'] = el * tpp
	i += 1

# Generate the plot
plt.plot(merged_df['cores'], merged_df['gflops'], label='mkl')
plt.plot(merged_df['cores'], merged_df['gflops_blis'], label='blis')
plt.plot(merged_df['cores'], merged_df['gflops_oblas'], label='oblas')
plt.plot(merged_df['cores'], merged_df['tpp'], label='tpp', linestyle="dashed")

plt.xlabel('Cores')
plt.ylabel('GFLOPS')
plt.title('Average GFLOPS by Cores')

plt.legend()
plt.savefig(fname=f"plot_fmic_{mach}_{datatype}_{policy}.png")
