# Final Project Repo for Comp 3

This repo contains the data, functions, and scripts needed to run our final project files in our HPC environment.

### Intended use: Log into Hamming, clone repo into a "COMP3" folder, and then run .sh script

### How to clone this repo into your Hamming directory:

1. Login to Hamming
2. Ensure you are in home directory by running bash command: *cd $HOME*
3. Create a "COMP3" directory by running bash command: *mkdir COMP3*
4. Navigate into "COMP3" directory by running bash command: *cd COMP3*
5. Clone this repo into your "COMP3" directory by running bash command: *git clone https://github.com/KurtPask/Comp3-FinalProject*

### How to run the .sh script

To run the default settings already included in the repo, just run the bash command *sbatch $HOME/COMP3/HPC_batch.sh*

If you want to alter the parameters used, you can adjust the *HPC_parameters.csv* file with the parameter changes you want. You must then ensure the *HPC_batch.sh* script gets updated if you change the number of indices used (currently its 99).
