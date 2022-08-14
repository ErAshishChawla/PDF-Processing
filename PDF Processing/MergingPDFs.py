# Merging PDFs

'''
We want to create a program that can receive inputs from command line. These
inputs are pdfs. They can be 2, 3 any amount. We need to merge all these pdfs to create a
single pdf

python MergingPDFs.py dummy.pdf twopage.pdf rotated_dummy_pdf.pdf
'''

import PyPDF2
import sys
import os
import re
import time
from datetime import datetime


class NoArgumentPassed(Exception):
    pass


class PdfNotPresentInDir(Exception):
    pass


class OnePdfPassed(Exception):
    pass


class FileIsNotPdf(Exception):
    pass


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'Time lapsed {t2 - t1}s')
        return result

    return wrapper


# @performance
# def merger(output_file, file_list):
#     merger_obj = PyPDF2.PdfMerger()
#     with open(f'.\\{output_file}', mode='wb') as new_file:  # this is not necessary
#         for file in file_list:
#             merger_obj.append(file)
#         merger_obj.write(new_file)


@performance
def merger(output_file, file_list):
    merger_obj = PyPDF2.PdfMerger()  # We create a merger object
    for file in file_list:
        merger_obj.append(file)  # we append all pdf files to the merger object
    merger_obj.write(output_file)  # we write the merger object to the file passed as an argument
    # If the output file is not present it creates it if present it rewrites it


regex = r"[a-zA-Z0-9_-]+[\.][p]{1}[d]{1}[f]{1}$"
current_path = '.\\'
pattern = re.compile(regex)
date_time_format = '%y%m%d-%H%M%S'

try:
    if (num_files := len(sys.argv) - 1) < 1:
        raise NoArgumentPassed

    for file in sys.argv[1:]:
        path = os.path.join(current_path, file)
        print(path)

        if not os.path.isfile(path):
            raise PdfNotPresentInDir

        if not pattern.fullmatch(file):
            raise FileIsNotPdf

    # output_file = f'Merged_pdf_{datetime.now().strftime(date_time_format)}.pdf'
    output_file = 'super.pdf'
    merger(output_file, sys.argv[1:])


except NoArgumentPassed:
    print('No file was passed while running the program. Please pass a file and re run the program')

except FileIsNotPdf:
    print(f'{file} is not a pdf. Please pass the files correctly and re run the program.')

else:
    print('all pdf merged')
