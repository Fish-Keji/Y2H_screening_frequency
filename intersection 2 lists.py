
import xlrd
Y2H_book = xlrd.open_workbook('/PATH/FILE.xlsx')
sheet1 = Y2H_book.sheet_by_name('SHEET1')
list1 = sheet1.col_values(0)
sheet2 = Y2H_book.sheet_by_name('SHEET2')
list2 = sheet2.col_values(0)

x = set(list1).intersection(set(list2))

print(x)
