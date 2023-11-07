#!/bin/bash
#SBATCH --array=1-100

. /etc/profile
module load lang/python/3.8.11

output_file="$HOME/COMP3/print_outputs/out_${SLURM_ARRAY_TASK_ID}.txt"

python $HOME/COMP3/HPC_script.py $SLURM_ARRAY_TASK_ID > $output_file
