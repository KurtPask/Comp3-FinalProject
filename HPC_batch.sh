#!/bin/bash
#SBATCH --array=1-100
#SBATCH --output=batch_print_outputs/out_%a.txt
#SBATCH --mem-per-cpu=2000M
#SBATCH --cpus-per-task=1
#SBATCH --time=02:00:00

. /etc/profile
module load lang/python/3.8.11
pip install protobuf==3.20.3
pip install tensorflow==2.8.0
pip install h5py==3.9.0
pip install numpy==1.24.3
pip install keras==2.8.0

python $HOME/Comp3-FinalProject/HPC_script.py $SLURM_ARRAY_TASK_ID 