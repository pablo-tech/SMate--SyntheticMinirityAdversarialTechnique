# TARGET: 32,32,3 CIFAR-10
# 
# REFERENCES
# https://machinelearningmastery.com/how-to-develop-a-generative-adversarial-network-for-a-cifar-10-small-object-photographs-from-scratch/
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Reshape
from keras.layers import Conv2D, Conv2DTranspose, UpSampling2D
from keras.layers import LeakyReLU, Dropout
from keras.layers import BatchNormalization
from keras.optimizers import Adam, RMSprop


# Batch normalization before RELU
# Decreasing number of filters, all same size
class DifferetiableNetwork(object):
    
    def __init__(self, input_n): 
        self.net_config = self.get_new_config()
        self.net_config['input_n'] = input_n
        self.neural_net = self.get_new_model()

    def get_new_config(self):
        config = {}
#         config['filter_size'] = 5
#         config['dropout'] = 0.4 # avoid generated images looking like noise
#         config['momentum'] = 0.9
#         config['dim'] = 7
#         config['depth'] = 64+64+64+64
#         config['volume'] = config['dim'] * config['dim'] * config['depth']
#         config['reshape'] = (config['dim'], config['dim'], config['depth'])
        return config
        
    def get_new_model(self):
        sequence = Sequential()

        latent_dim = self.net_config['input_n']
        # foundation for 4x4 image
        n_nodes = 256 * 4 * 4
        sequence.add(Dense(n_nodes, input_dim=latent_dim))
        sequence.add(LeakyReLU(alpha=0.2))
        sequence.add(Reshape((4, 4, 256)))
        # upsample to 8x8
        sequence.add(Conv2DTranspose(128, (4,4), strides=(2,2), padding='same'))
        sequence.add(LeakyReLU(alpha=0.2))
        # upsample to 16x16
        sequence.add(Conv2DTranspose(128, (4,4), strides=(2,2), padding='same'))
        sequence.add(LeakyReLU(alpha=0.2))
        # upsample to 32x32
        sequence.add(Conv2DTranspose(128, (4,4), strides=(2,2), padding='same'))
        sequence.add(LeakyReLU(alpha=0.2))
        # output layer
        sequence.add(Conv2D(3, (3,3), activation='tanh', padding='same'))
        
#         # input: fully connected
#         sequence.add(Dense(self.net_config['volume'], input_dim=self.net_config['input_n'])) 
#         sequence.add(BatchNormalization(momentum=self.net_config['momentum']))
#         sequence.add(Activation('relu'))
        
#         # upsample
#         sequence.add(Reshape(self.net_config['reshape']))
#         sequence.add(Dropout(self.net_config['dropout']))
#         sequence.add(UpSampling2D())
        
#         # hidden: convolutional
#         sequence.add(Conv2DTranspose(filters = int(self.net_config['depth'] / 2), 
#                                      kernel_size = self.net_config['filter_size'], 
#                                      padding = 'same'))
#         sequence.add(BatchNormalization(momentum=self.net_config['momentum']))
#         sequence.add(Activation('relu'))

#         sequence.add(UpSampling2D()) 

#         # hidden: convolutional
#         sequence.add(Conv2DTranspose(filters = int(self.net_config['depth'] / 4), 
#                                      kernel_size = self.net_config['filter_size'], 
#                                      padding = 'same'))
#         sequence.add(BatchNormalization(momentum=self.net_config['momentum']))
#         sequence.add(Activation('relu'))
        
#         # hidden: convolutional
#         sequence.add(Conv2DTranspose(filters = int(self.net_config['depth'] / 8), 
#                                      kernel_size = self.net_config['filter_size'], 
#                                      padding = 'same'))
#         sequence.add(BatchNormalization(momentum=self.net_config['momentum']))
#         sequence.add(Activation('relu'))
        
#         # hidden: convolutional
#         sequence.add(Conv2DTranspose(filters = 1, 
#                                      kernel_size = self.net_config['filter_size'], 
#                                      padding = 'same'))                     
        
#         # output
#         sequence.add(Activation('sigmoid'))
        
        return sequence
                                        
    def get_model(self):
        return self.neural_net
    
    def get_config(self):
        return self.net_config
        