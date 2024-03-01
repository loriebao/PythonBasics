import pandas as pd
import numpy as np

"""
Example 1: use np array as input
"""
np.set_printoptions(precision=4)  
a1 = np.random.randn(4, 5)
print(a1.shape, a1.dtype)
print(a1)

df = pd.DataFrame(a1, columns=['A', 'B ', 'C', 'D', 'E'])
print(df)

"""
Example 2: use Dictionary array as input
"""
df = pd.DataFrame(
    {
        "User Name": ["A", "B", "C", "D", "E"],
        "Age": [10, 20, 30, 40, 5],
        "Weight": [100, 200, 300, 400, 500], 
        "Sex": ["Male", "Female", "Male", "Female", "Male"] 
    }
)
print(df)
print("max age = ", df.Age.max())
print(df["Age"])
print(df.describe())

