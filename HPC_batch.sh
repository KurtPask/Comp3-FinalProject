#!/bin/bash
#SBATCH --array=1-99

. /etc/profile
module load lang/python/3.8.11

output_file="$HOME/Comp3-FinalProject/print_outputs/out_${SLURM_ARRAY_TASK_ID}.txt"

python $HOME/Comp3-FinalProject/HPC_script.py $SLURM_ARRAY_TASK_ID > $output_file
