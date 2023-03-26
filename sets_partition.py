# train, CV, test sets partition
import numpy as np
import pandas as pd

class Dataset:
    def __init__(self,df):

        self.df = df
        self.total_rows = len(df)

        self.m_train_set = np.ceil(self.total_rows*6/10)
        self.m_cv_set = np.ceil(self.total_rows*2/10)
        self.m_test_set = self.total_rows - self.m_train_set - self.m_cv_set

        self.train_set = self.df.loc[0:self.m_train_set]
        self.cv_set = self.df.loc[self.m_train_set+1:self.m_train_set+self.m_cv_set]
        self.test_set = self.df.loc[self.m_train_set+self.m_cv_set+1:self.total_rows-1]

        self.x_train_set = np.hstack((np.ones((len(self.train_set),1)),np.array(self.train_set[self.df.columns[:-1]])))
        self.x_cv_set = np.hstack((np.ones((len(self.cv_set),1)),np.array(self.cv_set[self.df.columns[:-1]])))
        self.x_test_set = np.hstack((np.ones((len(self.test_set),1)),np.array(self.test_set[self.df.columns[:-1]])))

        self.sets_for_loop = [[self.train_set],[self.cv_set],[self.test_set]]
        for x in self.sets_for_loop:
            x.append(np.zeros((len(x[0]),3)))
            x.append(np.array(x[0]['y'])-1)
            for i in range(len(x[0])):
                x[1][i,x[2][i]] = 1

    def train_set_gen(self):
        return self.x_train_set, self.sets_for_loop[0][1]

    def cv_set_gen(self):
        return self.x_cv_set, self.sets_for_loop[1][1]

    def test_set_gen(self):
        return self.x_test_set, self.sets_for_loop[2][1]

    def original_y_test(self):
        return self.test_set['y']