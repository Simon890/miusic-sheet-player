import tensorflow as tf

class Model(tf.keras.Model):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conv1 = tf.keras.layers.Conv2D(128, (5, 5), activation="relu") #(128, 128) -> (126, 126)
        self.max_pool1 = tf.keras.layers.MaxPool2D((2, 2)) #(126, 126) -> (127, 127)
        self.conv2 = tf.keras.layers.Conv2D(64, (3, 3), activation="relu") #(127, 127) -> (127, 127)
        self.max_pool2 = tf.keras.layers.MaxPool2D((2, 2)) #(127, 127) -> (128, 128) 
        self.conv3 = tf.keras.layers.Conv2D(64, (5, 5), activation="relu") #(128, 128) -> (126, 126)
        self.avg_pool1 = tf.keras.layers.Flatten() #Flatten (126, 126) -> 15876
        self.dense1 = tf.keras.layers.Dense(128, activation=tf.keras.activations.relu) #15876 -> 128
        self.dense2 = tf.keras.layers.Dense(3) #128 -> 3
    
    def call(self, inputs, training=None, mask=None):
        layer = self.conv1(inputs)
        layer = self.max_pool1(layer)
        layer = self.conv2(layer)
        layer = self.max_pool2(layer)
        layer = self.conv3(layer)
        layer = self.avg_pool1(layer)
        layer = self.dense1(layer)
        layer = self.dense2(layer)
        return layer
        
        