import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

df = pd.read_csv('datasheet.csv',names=['x_1','x_2','y'])


number_of_examples = 2000
rnd_arr_1_x = np.random.normal(loc=300,scale=50,size=(number_of_examples,1))
rnd_arr_1_y = np.random.normal(loc=-50,scale=25,size=(number_of_examples,1))
rnd_arr_1 = np.hstack((rnd_arr_1_x,rnd_arr_1_y))
rnd_arr_2_x = np.random.normal(loc=0,scale=100,size=(number_of_examples,1))
rnd_arr_2_y = np.random.normal(loc=0,scale=200,size=(number_of_examples,1))
rnd_arr_2 = np.hstack((rnd_arr_2_x,rnd_arr_2_y))

x_threshold = 70
y_threshold = 110
all_valid = np.array([((rnd_arr_2_x>x_threshold)|(rnd_arr_2_x<-1*x_threshold)) | ((rnd_arr_2_y>y_threshold)|(rnd_arr_2_y<-1*y_threshold))]).reshape(2000,1)
rnd_arr_2 = np.array([x for i,x in enumerate(rnd_arr_2) if all_valid[i]==True])

rnd_arr_3_x = np.random.normal(loc=0,scale=20,size=(number_of_examples,1))
rnd_arr_3_y = np.random.normal(loc=0,scale=25,size=(number_of_examples,1))
rnd_arr_3 = np.hstack((rnd_arr_3_x,rnd_arr_3_y))
x = np.vstack((rnd_arr_1[:len(rnd_arr_2)],rnd_arr_2,rnd_arr_3[:len(rnd_arr_2)]))
#y = np.vstack((np.ones((number_of_examples,1)),np.ones((number_of_examples,1))*2,np.ones((number_of_examples,1))*3))
y = np.vstack((np.ones((len(rnd_arr_2),1)),np.ones((len(rnd_arr_2),1))*2,np.ones((len(rnd_arr_2),1))*3))
df = pd.DataFrame(np.hstack((x,y)),columns=['x_1','x_2','y'])

#df = df.sample(frac=1,ignore_index=True)


df['x_1']=df['x_1'].astype(float)
df['x_2']=df['x_2'].astype(float)
df['y']=df['y'].astype(int)

#df.to_csv('datasheet2.csv',index=False,header=False)



print(df)
fig = figure()
ax = fig.add_axes([0,0,1,1])
for key,value_set in df.groupby('y'):
    ax.scatter(value_set.x_1,value_set.x_2)
plt.show()



