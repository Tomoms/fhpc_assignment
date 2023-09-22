#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from sys import argv

# Read the three CSV files
df1 = pd.read_csv(argv[1]) # blis

# Group the rows by 'size' and calculate the average of 'gflops' for each file
grouped_df1 = df1.groupby('swthreads')['time'].mean().reset_index()
serial = 205.889
grouped_df1['speedup'] = serial/grouped_df1['time']
# Generate the plot
plt.plot(grouped_df1['swthreads'] * 2, grouped_df1['speedup'], label='real speedup')
plt.plot(grouped_df1['swthreads'] * 2, grouped_df1['swthreads'] * 2, label='ideal speedup', linestyle="dashed")

plt.xlabel('total swthreads')
plt.ylabel('speedup')
plt.title('Speedup by OMP swthreads (1 MPI rank per socket)')

plt.legend()
plt.savefig(fname="omp_plot_speedup.png")
