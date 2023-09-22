#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from sys import argv

# Read the three CSV files
df1 = pd.read_csv(argv[1]) # blis

# Group the rows by 'size' and calculate the average of 'gflops' for each file
grouped_df1 = df1.groupby('ranks')['time'].mean().reset_index()

# Generate the plot
plt.plot(grouped_df1['ranks'], grouped_df1['time'], label='time')

plt.xlabel('processes')
plt.ylabel('elapsed time')
plt.title('Average elapsed time by MPI processes')

plt.legend()
plt.savefig(fname="mpi_strong_plot_runtime.png")
