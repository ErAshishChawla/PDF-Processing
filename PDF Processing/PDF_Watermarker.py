# Watermarking a pdf

"""
Build a script that watermarks the pdfs. Multiple pdfs can be given as an input
python PDF_Watermarker.py <watermark> <file1> <file2>

To watermark a pdf we need to merge the watermark page and the original page.
Before that we need to store the mediabox of the original page somewhere
then merge pages using page.mergePage(watermark)
Then replace the mediabox of the merged page with original page
Then write it to the file.
"""

import PyPDF2
import sys
import os
import re
import time


class NoArgumentPassed(Exception):
    pass


class PdfNotPresentInDir(Exception):
    pass


class FileIsNotPdf(Exception):
    pass


class OnlyWaterMark(Exception):
    pass


regex = r"[a-zA-Z0-9_-]+[\.][p]{1}[d]{1}[f]{1}$"
pattern = re.compile(regex)
date_time_format = '%y%m%d-%H%M%S'
current_path = '.\\'


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'Time lapsed {t2 - t1}s')
        return result

    return wrapper


@performance
def water_marker(water_mark, file_list):
    with open(os.path.join(current_path, water_mark), mode='rb') as water_mark_file:
        water_mark_reader = PyPDF2.PdfReader(water_mark_file)
        water_mark_page = water_mark_reader.getPage(0)
        for file_name in file_list:
            file_path = os.path.join(current_path, file_name)
            with open(file_path, mode='r+b') as file:
                file_reader = PyPDF2.PdfReader(file)
                file_writer = PyPDF2.PdfWriter()
                for page_index in range(0, file_reader.numPages):
                    page = file_reader.getPage(page_index)
                    temp_mediabox = page.mediabox
                    page.mergePage(water_mark_page)  # this modifies the page in place
                    page.mediabox = temp_mediabox
                    file_writer.addPage(page)
                file_writer.write(file)
    return True


try:
    if (num_files := len(sys.argv) - 1) < 1:
        raise NoArgumentPassed

    if num_files == 1:
        raise OnlyWaterMark

    for file in sys.argv[1:]:
        path = os.path.join(current_path, file)

        if not os.path.isfile(path):
            raise PdfNotPresentInDir

        if not pattern.fullmatch(file):
            raise FileIsNotPdf
    water_mark = sys.argv[1]
    file_list = sys.argv[2:]
    # output_file = f'Merged_pdf_{datetime.now().strftime(date_time_format)}.pdf'
    output_file = 'WaterMarked.pdf'

    result = water_marker(water_mark, file_list)


except NoArgumentPassed:
    print('No file was passed while running the program. Please pass a file and re run the program')

except FileIsNotPdf:
    print(f'{file} is not a pdf. Please pass the files correctly and re run the program.')

else:
    if result:
        print('all pdfs watermarked')
