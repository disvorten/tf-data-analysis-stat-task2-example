import pandas as pd
import numpy as np

from scipy.stats import uniform

chat_id = 1109095907


def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    x_n = x.max()
    left = 0.071 + (x_n / (1 + uniform.ppf(1 - alpha / 2)))
    right = 0.071 + (x_n / (1 + uniform.ppf(alpha / 2)))
    return left, right


# np.random.seed(42)

# if __name__ == '__main__':
#     b = 1
#     mas = np.random.uniform(0.071, b, 1000)
#     a, c = solution(0.99, mas)
#     # print(c - a)
#     p = 0.7
#     iter_size = 10000
#     test_stat = [{
#         "sample_size": 3
#     }, {
#         "sample_size": 10
#     }, {
#         "sample_size": 100
#     }, {
#         "sample_size": 1000
#     }]
#
#     solution_list = [{
#         "name": "clt",
#         "function": solution
#     }]
#
#     for test_element in test_stat:
#         x = uniform(loc=0.071, scale=b).rvs(size=[iter_size, test_element["sample_size"]])
#         for i in range(iter_size):
#             for solution_element in solution_list:
#                 left_side, right_side = solution_element["function"](p, x[i])
#
#                 total_error_col = solution_element["name"] + "_total_error"
#                 total_interval_length_col = solution_element["name"] + "_total_interval_length"
#
#                 test_element[total_error_col] = test_element.get(total_error_col, 0) \
#                                                 + (1 if (b < left_side or right_side < b) else 0)
#                 test_element[total_interval_length_col] = test_element.get(total_interval_length_col, 0) \
#                                                           + right_side - left_side
#
#         for solution_element in solution_list:
#             total_error_col = solution_element["name"] + "_total_error"
#             mean_error_col = solution_element["name"] + "_mean_error"
#             test_element[mean_error_col] = test_element[total_error_col] / iter_size
#
#             total_interval_length_col = solution_element["name"] + "_total_interval_length"
#             mean_interval_length_col = solution_element["name"] + "_mean_interval_length"
#             test_element[mean_interval_length_col] = test_element[total_interval_length_col] / iter_size
#
#     column_description = [{
#         "column": "sample_size",
#         "description": "Размер выборки"
#     }, {
#         "column": "exact_mean_error",
#         "description": "Частота ошибок точного интервала"
#     }, {
#         "column": "clt_mean_error",
#         "description": "Частота ошибок асимптотического интервала"
#     }, {
#         "column": "exact_mean_interval_length",
#         "description": "Средняя длина точного интервала"
#     }, {
#         "column": "clt_mean_interval_length",
#         "description": "Средняя длина асимптотического интервала"
#     }]

    # test_data = pd.DataFrame(test_stat)
    # test_data.to_csv('res.csv')
    # print(test_data)
    # test_data[[el["column"] for el in column_description]] \
    #     .rename(columns={el["column"]: el["description"]
    #                      for el in column_description})
