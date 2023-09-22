#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from sys import argv

# Read the three CSV files
df1 = pd.read_csv(argv[1]) # blis

# Group the rows by 'size' and calculate the average of 'gflops' for each file
grouped_df1 = df1.groupby('swthreads')['time'].mean().reset_index()
# Generate the plot
plt.plot(grouped_df1['swthreads'], grouped_df1['time'], label='time')

plt.xlabel('swthreads per socket')
plt.ylabel('time')
plt.title('Runtime by OMP swthreads (1 MPI rank per socket)')

plt.legend()
plt.savefig(fname="omp_plot_runtime.png")
