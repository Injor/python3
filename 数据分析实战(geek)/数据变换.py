
from sklearn import preprocessing
import numpy as np
x = np.array([[5000.],[16000.],[58000.]])
min_max_scaler = preprocessing.MinMaxScaler()
minmax_x = min_max_scaler.fit_transform(x)
print(minmax_x)
