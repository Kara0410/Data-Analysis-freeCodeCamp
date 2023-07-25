import numpy as np


def calculate(list_of_numbers: list):
    print(len(list_of_numbers))
    if len(list_of_numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix_3x3 = np.reshape(list_of_numbers, newshape=(3, 3))

    # axis_1 is for each col and axis_2 is for each row
    axis_1_means = []
    axis_2_means = []
    matrix_mean = np.mean(matrix_3x3)

    axis_1_var = []
    axis_2_var = []
    matrix_var = np.var(matrix_3x3)

    axis_1_std = []
    axis_2_std = []
    matrix_std = np.std(matrix_3x3)

    axis_1_max = []
    axis_2_max = []
    matrix_max = np.max(matrix_3x3)

    axis_1_min = []
    axis_2_min = []
    matrix_min = np.min(matrix_3x3)

    axis_1_sum = []
    axis_2_sum = []
    matrix_sum = np.sum(matrix_3x3)


    for _ in range(3):
        # mean calculation
        axis_1_means.append(np.mean(matrix_3x3[:, _]))
        axis_2_means.append(np.mean(matrix_3x3[_]))

        # variance calculation
        axis_1_var.append(np.var(matrix_3x3[:, _]))
        axis_2_var.append(np.var(matrix_3x3[_]))

        # standard deviation calculation
        axis_1_std.append(np.std(matrix_3x3[:, _]))
        axis_2_std.append(np.std(matrix_3x3[_]))

        # max calculation
        axis_1_max.append(np.max(matrix_3x3[:,  _]))
        axis_2_max.append(np.max(matrix_3x3[_]))

        # min calculation
        axis_1_min.append(np.min(matrix_3x3[:, _]))
        axis_2_min.append(np.min(matrix_3x3[_]))

        # sum calculation
        axis_1_sum.append(np.sum(matrix_3x3[:, _]))
        axis_2_sum.append(np.sum(matrix_3x3[_]))

    output = {
        'mean': [axis_1_means, axis_2_means, matrix_mean],
        'variance': [axis_1_var, axis_2_var, matrix_var],
        'standard deviation': [axis_1_std, axis_2_std, matrix_std],
        'max': [axis_1_max, axis_2_max, matrix_max],
        'min': [axis_1_min, axis_2_min, matrix_min],
        'sum': [axis_1_sum, axis_2_sum, matrix_sum]
    }
    return output
