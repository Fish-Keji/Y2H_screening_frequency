# -*- coding: utf-8 -*-
"""
Calculate the frequency of Y2H screening results
"""
import xlrd
import pandas as pd

Y2H_book = xlrd.open_workbook('/FILE_PATH/FILE_NAME.xlsx')
prey_sheet = Y2H_book.sheet_by_name('SHEET_NAME')
prey_list = prey_sheet.col_values(0)
prey_freq = pd.value_counts(prey_list)

prey_freq.to_excel('/FILE_PATH/FILE_NAME.xlsx')
