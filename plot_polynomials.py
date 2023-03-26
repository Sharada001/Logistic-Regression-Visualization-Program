import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from degree import degree_selection

def plot_curve(degree,theta):
    number_of_pairs = 500
    x_1 = np.linspace(-50,300,num=number_of_pairs)
    x_2 = np.linspace(-50,300,num=number_of_pairs)

    plot_data = np.array([(x,y) for x in x_1 for y in x_2])
    x_1 = plot_data[:,0]
    x_2 = plot_data[:,1]
    plot_data = pd.DataFrame({'x_1':x_1,'x_2':x_2}).astype(float)

    plot_data[['x_1','x_2']] = (plot_data[['x_1','x_2']]-plot_data[['x_1','x_2']].mean())/(plot_data[['x_1','x_2']].max()-plot_data[['x_1','x_2']].min())
    plot_data['y'] = 0
    plot_data = degree_selection(plot_data, degree)
    plot_data = np.hstack((np.ones((len(plot_data),1)),plot_data))
    plot_data = np.array(plot_data)
    plot_data = plot_data[:,:-1]

    evaluated_values = plot_data@theta
    threshold = 0.01
    x_values_for_1_class = (plot_data[(-1*threshold<evaluated_values[:,0]) & (evaluated_values[:,0]<threshold)])[:,1:3]
    x_values_for_2_class = (plot_data[(-1 * threshold < evaluated_values[:, 1]) & (evaluated_values[:, 1] < threshold)])[:, 1:3]
    x_values_for_3_class = (plot_data[(-1 * threshold < evaluated_values[:, 2]) & (evaluated_values[:, 2] < threshold)])[:, 1:3]
    plt.scatter(x_values_for_1_class[:,0],x_values_for_1_class[:,1])
    plt.scatter(x_values_for_2_class[:, 0], x_values_for_2_class[:, 1])
    plt.scatter(x_values_for_3_class[:, 0], x_values_for_3_class[:, 1])
    plt.show()
