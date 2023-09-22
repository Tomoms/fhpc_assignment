# Compiling the program

Folder `gol` contains the actual code, plus the Makefile to build it.
In order to compile it, run:

```
module load openMPI/4.1.5/gnu/12.2.1
salloc -n 1 -N1 -p EPYC --time=0:10:0 make
```

Patterns are not provided as they are several hundreds of megabytes, or gigabytes, big.

To run the program, execute, for example:

```
module load openMPI/4.1.5/gnu/12.2.1
export LD_LIBRARY_PATH=/u/dssc/tfonda/boost/lib:/u/dssc/tfonda/mimalloc/out/release:$LD_LIBRARY_PATH
export OMP_NUM_THREADS=32
salloc --sockets-per-node=2 --ntasks=64 --ntasks-per-socket=32 --cpus-per-task=1 -N1 -p EPYC --time=0:10:0  mpirun --map-by socket ./gol -r -f image_2.pgm -n 100 -s 0 -e 1
```

Folder `scripts` contains example slurm scripts to execute the simulations.

Folder `results` contains csv files with results and Python scripts to generate plots from them.
