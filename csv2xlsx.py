import sys
import os
import pandas


# dir_path = sys.argv[1]
# files = os.listdir(dir_path)
# for file in files:
#     excel_file =


def csv_to_xlsx():
    if len(sys.argv) > 1:
        dir_path = sys.argv[1]
    else:
        dir_path = os.path.dirname(sys.argv[0]) + "\\PDF2CSV_Extracted"

    files = os.listdir(dir_path)
    # //print(files)

    if not os.path.exists(dir_path+'\\Excel_Files'):
        os.mkdir(dir_path+'\\Excel_Files')

    excel_dir_path = dir_path+'\\Excel_Files'

    for file in files:
        # if file[-4:] != ".csv":
        #     continue
        full_path = dir_path + '\\' + file
        excel_file_full_path = excel_dir_path + "\\" + file[:-3] + 'xlsx'
        # read_file = pandas.read_csv(full_path, delimiter="\t")
        # read_file.to_excel(excel_file_full_path, index=None, header=True)
        print(excel_file_full_path)




csv_to_xlsx()






# read_file = pandas.read_csv(r'C:\\Users\\nicdo\\Desktop\\PDF2CSV_Extracted\\ATmega8A_RegSum.csv', delimiter="\t")
# read_file.to_excel(r'C:\\Users\\nicdo\\Desktop\\PDF2CSV_Extracted\\AAAAAA.xlsx', index=None, header=True)