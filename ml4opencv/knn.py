from cv2 import dft
import numpy as np
import cv2
import matplotlib.pyplot as plt

plt.style.use('ggplot')


#single_data_point=np.random.randint(0,100,size=2)
#single_lable=np.random.randint(0,2)
#print(single_data_point)
#print(single_lable)
def generate_data(num_samples,num_features=2):
    #np.random.seed(42)
    data_size=(num_samples,num_features)
    train_data=np.random.randint(0,100,size=data_size)
    label_size=(num_samples,1)
    labels=np.random.randint(0,2,size=label_size)
    return train_data.astype(np.float32),labels

if __name__ == '__main__':
    print('Hello World!')
    train_data,train_label=generate_data(11)
    print(train_data)