#!/bin/bash
#SBATCH --job-name=mpi_scalability_epyc_balanced
#SBATCH --output=mpi_scalability_epyc_balanced
#SBATCH --nodes=2
#SBATCH --exclusive
#SBATCH --time=2:00:00
#SBATCH --partition=EPYC
module load openMPI/4.1.5/gnu/12.2.1
cd /u/dssc/tfonda/fast/gol
export OMP_NUM_THREADS=1
export LD_LIBRARY_PATH=/u/dssc/tfonda/boost/lib:/u/dssc/tfonda/mimalloc/out/release:$LD_LIBRARY_PATH
for j in {2..254..8} 256; do
for i in {0..2} ; do
	mpirun -np $j --map-by ppr:$(($j / 2)):node ./gol -r -f image_4.pgm -n 100 -s 0 -e 1
done
done
