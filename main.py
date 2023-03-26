import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from sets_partition import Dataset
from sigmoid import Sigmoid
from model_selection import theta_selection
from model_selection import learning_test
from model_selection import Model
from degree import degree_selection
import numpy as np
from plot_polynomials import plot_curve

df = pd.read_csv('datasheet1.csv',names=['x_1','x_2','y'])

df_x = (df[['x_1','x_2']]-df[['x_1','x_2']].mean())/(df[['x_1','x_2']].max()-df[['x_1','x_2']].min())
df[['x_1','x_2']] = df_x

alpha = 12
#learning_test(df,alpha)

degree = 5
l = .1
df = degree_selection(df, degree)
new_datast = Dataset(df)
x_train, y_train = new_datast.train_set_gen()
theta = theta_selection(degree)
J_theta_reg,theta = Model(x_train, y_train, theta, l, alpha)
x_test, y_test = new_datast.test_set_gen()
predicted = np.array(x_test@theta>=0.5,dtype='i')
acc = [1 if all(x) else 0 for x in predicted==y_test]
accuracy = acc.count(1)/len(acc)*100
print(accuracy)

y_values = new_datast.original_y_test()
plot_set = pd.DataFrame({'x_1':x_test[:,1],'x_2':x_test[:,2],'y':y_values})
for key,value_set in plot_set.groupby('y'):
    plt.scatter(value_set['x_1'],value_set['x_2'])

plot_curve(degree,theta)


'''
fig_1 = figure()
ax_1 = fig_1.add_axes([0, 0, 1, 1])
ax_1.plot(*cost_graph_values)
plt.show()

#plotting
fig_2 = figure()
ax_2 = fig_2.add_axes([0,0,1,1])
#for key,value in x_train.groupby('y'):
#    ax_2.scatter(value.x_1,value.x_2)
x_1_values = np.linspace(0,1,num=100)
theta_1 = theta[:,0]
x_2_values = (-1*theta_1[0]-1*(theta_1[1])*x_1_values)/theta_1[2]
ax_2.plot(x_1_values,x_2_values)
plt.show()
'''

