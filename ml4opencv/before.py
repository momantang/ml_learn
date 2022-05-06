import numpy as np
from sklearn.tree import plot_tree
print(np.__version__)
import cv2
from sklearn import datasets

iris=datasets.fetch_openml('iris',version=1)
iris_data=iris['data']
iris_target=iris['target']

print(iris_data.shape)
import matplotlib.pyplot as plt
x=np.linspace(0,1,100)

dlgits=datasets.load_digits()
plt.figure(figsize=(14,4))
for i in range(10):
    subplot_index=i+1
    plt.subplot(2,5,subplot_index)
    plt.imshow(dlgits.images[i],cmap='gray')

plt.show()