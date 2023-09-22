#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from sys import argv

# Read the three CSV files
df1 = pd.read_csv(argv[1]) # blis

# Group the rows by 'size' and calculate the average of 'gflops' for each file
grouped_df1 = df1.groupby('ranks')['time'].mean().reset_index()
serial = grouped_df1['time'][0]
grouped_df1['speedup'] = serial/grouped_df1['time']
# Generate the plot
plt.plot(grouped_df1['ranks'], grouped_df1['speedup'], label='real speedup')
plt.plot(grouped_df1['ranks'], grouped_df1['ranks'], label='ideal speedup', linestyle="dashed")

plt.xlabel('processes')
plt.ylabel('speedup')
plt.title('Speedup by MPI processes')

plt.legend()
plt.savefig(fname="mpi_strong_plot_speedup.png")
