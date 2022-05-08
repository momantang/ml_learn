import numpy as np
import matplotlib.pyplot as plt
import cv2
np.random.seed(42)

y_true=np.random.randint(0,2,size=5)
print(y_true)

y_pred=np.ones(5,dtype=np.int32)
print(y_pred)

test_set_size=len(y_true)
predict_correct=np.sum(y_true==y_pred)
predict_correct_rate=predict_correct/test_set_size
print(predict_correct_rate)

from sklearn import metrics
print(metrics.accuracy_score(y_true,y_pred))


truly_a_positive=(y_true==1)
prediected_a_positive=(y_pred==1)
ture_positive=np.sum(prediected_a_positive*truly_a_positive)
print(ture_positive)
