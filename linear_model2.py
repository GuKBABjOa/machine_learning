import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("data_two.csv")
x = data['X'].values
y = data['y'].values


theta = np.zeros(4)  
alpha = 0.01  
iterations = 500  


m = len(x)
for _ in range(iterations):
    y_pred = theta[0] + theta[1]*x + theta[2]*x**2 + theta[3]*x**3  
    error = y_pred - y  
    gradient = [np.sum(error) / m, 
                np.sum(error * x) / m, 
                np.sum(error * x**2) / m, 
                np.sum(error * x**3) / m]  
    theta -= alpha * np.array(gradient)  


plt.scatter(x, y, label='Data')  
plt.plot(x, theta[0] + theta[1]*x + theta[2]*x**2 + theta[3]*x**3, color='red')  
plt.show()
