
def degree_selection(dataset,degree):
    if degree == 1:
        return dataset[['x_1','x_2','y']]
    if degree == 2:
        dataset['x_1_2'] = dataset['x_1']**2
        dataset['x_1_x_2'] = dataset['x_1']*dataset['x_2']
        dataset['x_2_2'] = dataset['x_1']**2
        return dataset[['x_1','x_2','x_1_2','x_1_x_2','x_2_2','y']]
    if degree == 3:
        dataset['x_1_2'] = dataset['x_1'] ** 2
        dataset['x_1_x_2'] = dataset['x_1'] * dataset['x_2']
        dataset['x_2_2'] = dataset['x_1'] ** 2
        dataset['x_1_3'] = dataset['x_1']**3
        dataset['x_1_2_x_2'] = dataset['x_1']**2 * dataset['x_2']
        dataset['x_1_x_2_2'] = dataset['x_1'] * dataset['x_2']**2
        dataset['x_2_3'] = dataset['x_1']**3
        return dataset[['x_1','x_2','x_1_2','x_1_x_2','x_2_2','x_1_3','x_1_2_x_2','x_1_x_2_2','x_2_3','y']]
    if degree == 4:
        dataset['x_1_2'] = dataset['x_1'] ** 2
        dataset['x_1_x_2'] = dataset['x_1'] * dataset['x_2']
        dataset['x_2_2'] = dataset['x_1'] ** 2
        dataset['x_1_3'] = dataset['x_1'] ** 3
        dataset['x_1_2_x_2'] = dataset['x_1'] ** 2 * dataset['x_2']
        dataset['x_1_x_2_2'] = dataset['x_1'] * dataset['x_2'] ** 2
        dataset['x_2_3'] = dataset['x_1'] ** 3
        dataset['x_1_4'] = dataset['x_1'] ** 4
        dataset['x_1_3_x_2'] = dataset['x_1']**3 * dataset['x_2']
        dataset['x_1_2_x_2_2'] = dataset['x_1']**2 * dataset['x_2']**2
        dataset['x_1_x_2_3'] = dataset['x_1'] * dataset['x_2']**3
        dataset['x_2_4'] = dataset['x_2']**4
        return dataset[['x_1','x_2','x_1_2','x_1_x_2','x_2_2','x_1_3','x_1_2_x_2','x_1_x_2_2','x_2_3','x_1_4','x_1_3_x_2','x_1_2_x_2_2','x_1_x_2_3','x_2_4','y']]
    if degree == 5:
        dataset['x_1_2'] = dataset['x_1'] ** 2
        dataset['x_1_x_2'] = dataset['x_1'] * dataset['x_2']
        dataset['x_2_2'] = dataset['x_1'] ** 2
        dataset['x_1_3'] = dataset['x_1'] ** 3
        dataset['x_1_2_x_2'] = dataset['x_1'] ** 2 * dataset['x_2']
        dataset['x_1_x_2_2'] = dataset['x_1'] * dataset['x_2'] ** 2
        dataset['x_2_3'] = dataset['x_1'] ** 3
        dataset['x_1_4'] = dataset['x_1'] ** 4
        dataset['x_1_3_x_2'] = dataset['x_1'] ** 3 * dataset['x_2']
        dataset['x_1_2_x_2_2'] = dataset['x_1'] ** 2 * dataset['x_2'] ** 2
        dataset['x_1_x_2_3'] = dataset['x_1'] * dataset['x_2'] ** 3
        dataset['x_2_4'] = dataset['x_2'] ** 4
        dataset['x_1_5'] = dataset['x_1'] ** 5
        dataset['x_1_4_x_2'] = dataset['x_1'] ** 4 * dataset['x_2']
        dataset['x_1_3_x_2_2'] = dataset['x_1']** 3 * dataset['x_2']**2
        dataset['x_1_2_x_2_3'] = dataset['x_1'] ** 2 * dataset['x_2'] ** 3
        dataset['x_1_x_2_4'] = dataset['x_1'] * dataset['x_2'] ** 4
        dataset['x_2_5'] = dataset['x_2'] ** 5
        return dataset[['x_1', 'x_2', 'x_1_2', 'x_1_x_2', 'x_2_2', 'x_1_3', 'x_1_2_x_2', 'x_1_x_2_2', 'x_2_3', 'x_1_4','x_1_3_x_2', 'x_1_2_x_2_2', 'x_1_x_2_3', 'x_2_4', 'x_1_5', 'x_1_4_x_2', 'x_1_3_x_2_2', 'x_1_2_x_2_3', 'x_1_x_2_4', 'x_2_5', 'y']]