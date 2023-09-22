#!/bin/bash
#SBATCH --job-name=omp_scalability_epyc
#SBATCH --output=omp_scalability_epyc
#SBATCH --nodes=1
#SBATCH --exclusive
#SBATCH --ntasks=2
#SBATCH --ntasks-per-socket=1
#SBATCH --exclude=epyc002
#SBATCH --time=2:00:00
#SBATCH --partition=EPYC
module load openMPI/4.1.5/gnu/12.2.1
cd /u/dssc/tfonda/fast/gol
export OMP_PLACES=sockets
export OMP_PROC_BIND=master
export LD_LIBRARY_PATH=/u/dssc/tfonda/boost/lib:/u/dssc/tfonda/mimalloc/out/release:$LD_LIBRARY_PATH
NODE_TYPE=epyc
OUTFILE=omp_scalability_"${NODE_TYPE}".csv
echo "size,ranks,swthreads,time" > "${OUTFILE}"
for j in 1 8 16 24 32 40 48 56 64; do
export OMP_NUM_THREADS=$j
for i in {0..2} ; do
	mpirun --map-by socket ./gol -r -f huge.pgm -n 150 -s 0 -e 1
	echo "run finished"
done 
done
