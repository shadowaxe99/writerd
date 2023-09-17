```python
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def normalize_data(data):
    """
    Function to normalize data using MinMaxScaler from sklearn
    """
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)
    return normalized_data

def split_data(data, test_size=0.2):
    """
    Function to split data into training and testing sets
    """
    data_length = len(data)
    split_index = int(data_length * (1 - test_size))
    train_data = data[:split_index]
    test_data = data[split_index:]
    return train_data, test_data

def convert_to_numpy(data):
    """
    Function to convert data to numpy array
    """
    return np.array(data)

def reshape_data(data, new_shape):
    """
    Function to reshape data
    """
    return data.reshape(new_shape)
```