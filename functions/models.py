# - imports - 
from tensorflow.keras.layers import Dense, MaxPooling2D,  Flatten, Conv2D
from tensorflow.keras import Sequential, initializers
import time

# - model building function - 
def relu_conv3layer(x_train, y_train, num_first_filters = 32):
    '''
    Function that builds and times a neural network with 3 convolutions. Takes in training data and labels as arguments plus it allows for the alteration of 1 parameters from arguments.

    Parameters
    ----------
    x_train : numpy array
        Input data used to fit model
    y_train : numpy array
        Input labels used to fit model

    Returns
    -------
    model : tensorflow model object
        The trained model 
    '''
    # - start clock - 
    start_time = time.time() # start a timer to evaluate how long the model takes to train. Not currently storing the time, but just FYSA on the print line
    
    # - define model - 
    model = Sequential([Conv2D(num_first_filters, (3,3), activation='relu'), # first convolution layer w/ 3x3 window, num_filters specified in arguments, 
                        MaxPooling2D((2, 2)), # max pooling layer that takes max value along non-overlapping 2x2 squares from first convolution layer output
                        Conv2D(64, (3, 3), activation='relu'), # second convolution layer w/ 3x3 window and 64 filters
                        MaxPooling2D((2, 2)), # max pooling layer that takes max value along non-overlapping 2x2 squares from second convolution layer output                           
                        Conv2D(64, (3, 3), activation='relu'), # third convolution layer w/ 3x3 window and 64 filters
                        Flatten(), # flattens output from third convolution layer into 1-D vector
                        Dense(64, activation='relu'), # fully connected, relu-activated layer w/ 64 neurons
                        Dense(10, activation='softmax', kernel_initializer = initializers.RandomNormal(mean=0.5, stddev=1., seed=0))]) # logit layer that produces probability of each of the 10 classes using softmax activation
    
    # - compile model -
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy']) # compile the model, using adam optimizer, categorical crossentropy loss, and evaluating model based on accuracy
    
    # - train/fit model - 
    model.fit(x_train, y_train, epochs=10,batch_size=64) # fit the model given the training data, w/ 10 epochs and batches of 64
    
    # - stop clock and calculate time taken -
    end_time = time.time() # end the timer
    elapsed_time = end_time - start_time # time take = end-start
    print(f"relu_conv3layer model built. Elapsed time: {elapsed_time:.2f} seconds | {elapsed_time/60:.2f} minutes.") # printout to say how long it took
    
    return model # return trained model
