# -- custom methods --
from functions.load_data import load_MNIST_data, load_CIFAR_data, load_SVHN_data # data loading
from functions.models import relu_conv3layer # model training

# -- standard packages --
import pandas as pd # used to read in parameter data
import sys # used to get argument
import json # used to store outputs
import os # used to get current file directory

# -- get parameters --
index = int(sys.argv[1]) # index == first command line argument
df_params = pd.read_csv('hpc_parameters.csv') # load parameters CSV
row_params = df_params[df_params['index']==index].to_dict() # get the row corresponding to the index argument
p_filters = row_params['num_filters'][index-1] # defines number of convolution layers to include in the first convolutional layer
p_dataset = row_params['dataset'][index-1] # get datasets, 1=MNIST, 2=SVHN, 3=CIFAR

# -- load in dataset --
if p_dataset == 1:
    # - load MNIST data -
    x_train, x_test, y_train, y_test = load_MNIST_data(desired_classes=list(range(10)))
    x_train = x_train.reshape(-1,28,28,1)
    x_test = x_test.reshape(-1,28,28,1)
elif p_dataset == 2:
    # - load SVHN data -
    x_train, x_test, y_train, y_test = load_SVHN_data(desired_classes=list(range(10)))
    x_train = x_train.reshape(-1,32,32,3)
    x_test = x_test.reshape(-1,32,32,3)
elif p_dataset == 3:
    # - load CIFAR-10 data -
    x_train, x_test, y_train, y_test = load_CIFAR_data(desired_classes=list(range(10)))
    x_train = x_train.reshape(-1,32,32,3)
    x_test = x_test.reshape(-1,32,32,3)

# -- build model -- 
trained_model = relu_conv3layer(x_train=x_train, y_train=y_train, num_first_filters=p_filters)

# -- evaluate model --
loss, acc = trained_model.evaluate(x_test, y_test)

# -- write performance outputs to JSON file -- 
dict_outputs = {'loss':loss,
                'acc':acc,
                'dataset':p_dataset,
                'p_filters':p_filters} # store key data outputs as a dictionary
home_directory = os.path.expanduser("~") # get home directory
file_path = os.path.join(home_directory, "Comp3-FinalProject", "data_outputs") # build file path w/ home_directory in mind
with open(f"{file_path}/final_outputs_{index}.json", "w") as outfile: # open/create a JSON to store the data outputs 
    json.dump(dict_outputs, outfile) # dump dictionary into file
