#!/bin/bash
#SBATCH --array=1-3
#SBATCH --output=batch_print_outputs/out_%a.txt

. /etc/profile
module load lang/python/3.8.11
pip install protobuf==3.20.0
pip install tensorflow==2.10.0
pip install h5py==3.9.0
pip install numpy==1.24.3
pip install keras=2.10.0

python $HOME/Comp3-FinalProject/HPC_script.py $SLURM_ARRAY_TASK_ID 
