import xlrd
import numpy as np

_p = xlrd.open_workbook("D:\\felix\py\snake2048\p.xls").sheets()[0]
_rows = [_p.row(row)[1:] for row in range(1, 51)]
_dats = np.zeros((51, 50), int)
for i in range(50):
    for j in range(50):
        _dats[i + 1][j] = int(_rows[i][j].value)
    for j in range(1, 50):
        _dats[i + 1][j] += _dats[i + 1][j - 1]
# for i in range(50):
#     for j in range(50):
#         if _dats[i + 1][j] == 0:
#             _dats[i + 1][j] = -1
PROBABILITY = _dats
