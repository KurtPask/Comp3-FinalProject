#!/bin/bash
#SBATCH --array=1-99
#SBATCH --output=batch_print_outputs/out_%a.txt

. /etc/profile
module load lang/python/3.8.11
pip install protobuf==3.20.0

output_file="$HOME/Comp3-FinalProject/print_outputs/out_${SLURM_ARRAY_TASK_ID}.txt"

python $HOME/Comp3-FinalProject/HPC_script.py $SLURM_ARRAY_TASK_ID > $output_file
