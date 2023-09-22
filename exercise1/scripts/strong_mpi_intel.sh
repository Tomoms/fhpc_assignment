#!/bin/bash
#SBATCH --job-name=mpi_scalability_thin_new
#SBATCH --output=mpi_scalability_thin_new
#SBATCH --nodes=2
#SBATCH --exclusive
#SBATCH --time=2:00:00
#SBATCH --partition=THIN
module load openMPI/4.1.5/gnu/12.2.1
cd /u/dssc/tfonda/fast/gol
export OMP_NUM_THREADS=1
export LD_LIBRARY_PATH=/u/dssc/tfonda/boost_intel/lib:/u/dssc/tfonda/mimalloc_intel/out/release:$LD_LIBRARY_PATH
NODE_TYPE=intel
OUTFILE=strong_mpi_scalability_"${NODE_TYPE}".csv
echo "size,ranks,swthreads,time" > "${OUTFILE}"
for j in {2..48..4} 48; do
for i in {0..2} ; do
	mpirun -np $j --map-by ppr:$(($j / 2)):node  ./gol_intel -r -f image_4.pgm -n 100 -s 0 -e 1
done
done
