import numpy as np
import pandas as pd
from sigmoid import Sigmoid
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
from sets_partition import Dataset
from degree import degree_selection

def theta_selection(degree):
    division_value = 100
    if degree == 1:
        return np.random.random((3, 3))/division_value
    if degree == 2:
        return np.random.random((6, 3))/division_value
    if degree == 3:
        return np.random.random((10, 3))/division_value
    if degree == 4:
        return np.random.random((15, 3))/division_value
    if degree == 5:
        return np.random.random((21, 3))/division_value

def Model(x_train,y_train,theta,l,alpha):
    m = len(x_train)
    for x in range(1000):
        J_theta = (-1 / m) * (
            sum(sum(y_train * np.log(Sigmoid(x_train @ theta)) + (1-y_train) * np.log(1-Sigmoid(x_train @ theta)))))
        J_theta_reg = J_theta + (l / (2 * m)) * sum(sum(np.power(theta[1:], 2)))
        theta = theta - (alpha / m) * ((x_train.transpose() @ (Sigmoid(x_train @ theta) - y_train)) + l * np.vstack(
            (np.zeros((1, 3)), theta[1:])))
    return J_theta_reg,theta

def cost_function(x_set,y_set,theta):
    m = len(x_set)
    J_theta = (-1/m) * (sum(sum(y_set * np.log(Sigmoid(x_set @ theta)) + (1-y_set) * np.log(1-Sigmoid(x_set @ theta)))))
    return J_theta

def learning_test(df,alpha):
    lambdas = [0.00001,0.00003,0.0001,0.0003,0.001,0.003,0.01,0.03,0.1,0.3,1,3,10]
    degrees = range(1,4)
    fig_1, axes =plt.subplots(len(degrees),len(lambdas))
    for l_index,l in enumerate(lambdas):
        df = df[['x_1','x_2','y']]
        for degree_index,degree in enumerate(degrees):
            df = degree_selection(df, degree)
            new_datast = Dataset(df)
            x_train, y_train = new_datast.train_set_gen()
            x_cv, y_cv = new_datast.cv_set_gen()
            train_graph_values = [[], []]
            cv_graph_values = [[], []]
            theta = theta_selection(degree)
            J_theta_reg,theta = Model(x_train, y_train, theta, l, alpha)
            for i in range(1,len(x_cv)):
                x_train_temp = x_train[0:i]
                x_cv_temp = x_cv[0:i]
                y_train_temp = y_train[0:i]
                y_cv_temp = y_cv[0:i]
                train_graph_values[0].append(i)
                train_graph_values[1].append(cost_function(x_train_temp,y_train_temp,theta))
                cv_graph_values[0].append(i)
                cv_graph_values[1].append(cost_function(x_cv_temp, y_cv_temp, theta))
            axes[degree_index][l_index].plot(*train_graph_values,*cv_graph_values)
        print(l_index)
    plt.show()

