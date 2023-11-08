# Final Project Repo for Comp 3

This repo contains the data, functions, and scripts needed to run our final project files in our HPC environment.

### Intended use: Log into Hamming, clone repo into a "COMP3" folder, and then run .sh script

### How to clone this repo into your Hamming directory:

1. Open a Hamming session
2. Ensure you are in home directory by running bash command: ```cd $HOME```
3. Clone this repo into your "COMP3" directory by running bash command: ```git clone https://github.com/KurtPask/Comp3-FinalProject```
4. After the download is completed (*will take a minute or two*), confirm repo is cloned by running bash command: ```ls Comp3-FinalProject``` which should reveal the same files and folders you can see in this repo.
   
### How to run the .sh script

1. First, navigate into the new folder created by running this bash command: ```cd Comp3-FinalProject```
2. Next, run this bash command in submit the batch job: ```sbatch HPC_batch.sh```

If you want to alter the parameters used, you can adjust the ```HPC_parameters.csv``` file with the parameter changes you want. You must then ensure the ```HPC_batch.sh``` script gets updated if you change the number of indices used (currently its 99).
