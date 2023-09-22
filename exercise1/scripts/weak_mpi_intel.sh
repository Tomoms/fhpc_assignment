#!/bin/bash
#SBATCH --job-name=weak_mpi_scalability_thin
#SBATCH --output=weak_mpi_scalability_thin
#SBATCH --nodes=3
#SBATCH --exclusive
#SBATCH --time=2:00:00
#SBATCH --nodelist=thin007,thin008,thin010
#SBATCH --partition=THIN
module load openMPI/4.1.5/gnu/12.2.1
cd /u/dssc/tfonda/fast/gol
export LD_LIBRARY_PATH=/u/dssc/tfonda/boost_intel/lib:/u/dssc/tfonda/mimalloc_intel/out/release:$LD_LIBRARY_PATH
NODE_TYPE=intel
export OMP_NUM_THREADS=12
export OMP_PLACES=sockets
export OMP_PROC_BIND=master
OUTFILE=weak_mpi_scalability_"${NODE_TYPE}".csv
echo "size,ranks,swthreads,time" > "${OUTFILE}"
for j in 1 2 4 6; do
for i in {0..2} ; do
	mpirun -np $j --map-by socket ./gol_intel -r -f image_${j}.pgm -n 100 -s 0 -e 1
done
done
