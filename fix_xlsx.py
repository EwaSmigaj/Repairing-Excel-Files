
s = [10]
print(s)








# import openpyxl
#
# headers = []
# header_1 = ['Adress', 'Name', 'Bit 7', 'Bit 6', 'Bit 5', 'Bit 4', 'Bit 3', 'Bit 2', 'Bit 1', 'Bit 0', 'Page']
# header_2 = ['Offset', 'Name', 'Bit Pos.', '', '', '', '', '', '', '', '']
# headers.append(header_1)
# headers.append(header_2)
# offset = []
#
#
# def delete_and_move_others(sheet, column, row):
#     cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
#     rangee = str(cols[column-1]+str(row+1)+':'+cols[column-1]+str(sheet.max_row))
#     sheet.move_range(rangee, rows=-1, cols=0)
#     print(f"moved {rangee} o -1 ")
#
#
# def pages_length(sheet, start_column, start_row, stop_condition): # returns position of the next header
#     row = start_row+1
#     while sheet.cell(column=start_column, row=row).value != stop_condition:
#         row += 1
#     return row-start_row+1
#
#
# def fix_headers(sheet, header_model):
#     found = 99
#     for i in range(1, sheet.max_column):
#         if sheet.cell(column=i, row=1).value == header_model[0]:
#             found = i
#     for j in range(1, sheet.max_row):
#         if str(sheet.cell(column=found, row=j).value) == header_model[0]:
#             if j == 1:
#                 for a in range(0, len(header_model)):
#                     sheet.cell(column=found+a, row=j).value = header_model[a]
#                     print(sheet.cell(column=found+a, row=j).value)
#             else:
#                 sheet.delete_rows(j)
#
#
# def fix_reserved(sheet):
#     for i in range(1, sheet.max_row):
#         if sheet.cell(column=1, row=i).value == '...':
#             #print(i)
#             sheet.cell(column=2, row=i-1).value += ('\n ... \n' + sheet.cell(column=1, row=i+1).value)
#             sheet.cell(column=3, row=i-1).value = sheet.cell(column=2, row=i+1).value
#             sheet.delete_rows(i)
#             sheet.delete_rows(i)
#
#
# def get_offset(sheet):
#     c_of = 0
#     for i in range(sheet.max_col):
#         if str(sheet.cell(column=i, row=1).value) == "Offset":
#             c_of = i
#     for j in range(sheet.max_row):
#         if str(sheet.cell(column=c_of, row=j).value).find("0x") >= 0:
#             offset.append(str(sheet.cell(column=c_of, row=j).value))
#
#
# def repair_rows(sheet):
#     for i in range(1, sheet.max_row+1):
#         if sheet.cell(column=1, row=i).value is None:
#             empty_cells = 0
#             for j in range(1, sheet.max_column+1):
#                 if sheet.cell(column=j, row=i).value is None:
#                     empty_cells += 1
#             if empty_cells == sheet.max_column:
#                 sheet.delete_rows(i)
#                 print(i)
#
#
#
#
# # def repair_offset()
#
#
#
#
# def fix_andcells(sheet):
#     c_nb = 0
#     iterator = 0
#     for a in range(1, sheet.max_column):
#         if str(sheet.cell(column=a, row=1).value) == "Name":
#             c_nb = a
#
#     c_nb_one = []
#     c_nb_two = []
#
#     for i in range(1, sheet.max_row):
#
#         if str(sheet.cell(column=c_nb, row=i).value).find(' and') is not -1 and str(sheet.cell(column=c_nb, row=i).value)[-3:] != 'and':
#             sheet.cell(column=c_nb+2, row=i+1).value = sheet.cell(column=c_nb+1, row=i+1).value
#             print(f"daje komorce c= {c_nb + 2} r = {i+1} wartosc komorki c= {c_nb +1} r = {i + 1}")
#
#             sheet.cell(column=c_nb + 1, row=i + 1).value = sheet.cell(column=c_nb, row=i + 1).value
#             print(f"daje komorce c= {c_nb + 1} r = {i + 1} wartosc komorki c= {c_nb} r = {i + 1}")
#
#             sheet.cell(column=c_nb, row=i + 1).value = None
#             print(f"usuwam wartosc komorki c = {c_nb} r = {i + 1}")
#             c_nb_one.append(i)
#
#         if str(sheet.cell(column=c_nb, row=i).value).find(' and') is not -1 and str(sheet.cell(column=3, row=i).value)[-3:] == 'and':
#             sheet.cell(column=c_nb, row=i).value += (' ' + sheet.cell(column=c_nb-2, row=i+1).value)
#             sheet.cell(column=c_nb+1, row=i).value = sheet.cell(column=c_nb-1, row=i+1).value
#             print(f"daje komorce c= {c_nb+1} r = {i} wartosc komorki c= {c_nb-1} r = {i+1}... czyli {sheet.cell(column=c_nb-1, row=i+1).value}")
#
#             sheet.cell(column=c_nb+1, row=i+1).value = sheet.cell(column=c_nb, row=i+2).value
#             print(f"daje komorce c= {c_nb + 1} r = {i+1} wartosc komorki c= {c_nb} r = {i + 2}... czyli {sheet.cell(column=c_nb, row=i+2).value}")
#
#             sheet.cell(column=c_nb+2, row=i).value = sheet.cell(column=c_nb, row=i+1).value
#             print(f"daje komorce c= {c_nb + 2} r = {i} wartosc komorki c= {c_nb} r = {i + 1}... czyli {sheet.cell(column=c_nb, row=i+1).value}")
#
#             sheet.cell(column=c_nb+2, row=i+1).value = sheet.cell(column=c_nb+1, row=i+2).value
#             print(f"daje komorce c= {c_nb + 2} r = {i+1} wartosc komorki c= {c_nb+1} r = {i + 2}... czyli {sheet.cell(column=c_nb+1, row=i+2).value}")
#
#             sheet.cell(column=c_nb - 1, row=i + 1).value = None
#             print(f"usuwam wartosc komorki c = {c_nb-1} r = {i + 1}")
#
#             sheet.cell(column=c_nb, row=i + 2).value = None
#             print(f"usuwam wartosc komorki c = {c_nb} r = {i + 2}")
#
#             sheet.cell(column=c_nb, row=i + 1).value = None
#             print(f"usuwam wartosc komorki c = {c_nb} r = {i + 1}")
#
#             sheet.cell(column=c_nb + 1, row=i + 2).value = None
#             print(f"usuwam wartosc komorki c = {c_nb+1} r = {i + 2}")
#
#             sheet.cell(column=c_nb - 2, row=i + 1).value = None
#             print(f"usuwam wartosc komorki c = {c_nb-2} r = {i + 1}")
#             c_nb_two.append(i)
#
#     # for c in c_nb_one:
#     #     # sheet.merge_cells(start_row=c-1, start_column=c_nb, end_row=c, end_column=c_nb)
#     #     # print(f"merged {c-1} {c_nb} i {c} {c_nb}")
#     #
#     for c in c_nb_two:
#         delete_and_move_others(sheet, c_nb - 1, c + 1)
#     #     # sheet.merge_cells(start_row=c-1, start_column=c_nb, end_row=c, end_column=c_nb)
#     #     # print(f"merged {c-1} {c_nb} i {c} {c_nb}")
#
#
#
# def repair_file(path):
#     wb = openpyxl.load_workbook(path)
#     sheet = wb['Arkusz1']
#
#
#     # print(sheet['A1'].value)
#
#     if sheet['A1'].value == headers[0][0] or sheet['A2'].value == headers[0][0]:
#         file_type = 0
#     else:
#         file_type = 1
#     fix_headers(sheet, headers[file_type])
#     fix_offset(sheet)
#     fix_andcells(sheet)
#
#     if sheet['A1'].value == 'Unnamed: 0':
#         sheet.delete_cols(1)
#
#
#
#     repair_rows(sheet)
#     wb.save(path)
#
# repair_file('Zeszyt1.xlsx')
