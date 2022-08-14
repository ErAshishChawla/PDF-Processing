# PDFs with python

'''
In Python we can work with any file like images, text files, pdfs, excels,
csv and many more

We use PyPDF2 library to interact with PDFs
We can open a pdf using open()
But it has to be opened in binary mode
'rb' -> read binary

'''

import PyPDF2

with open('.\\dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)  # reads the pdf file
    print(reader)  # pypdf2 reader object
    print(reader.numPages)  # returns the number of pages in the pdf file
    print(reader.getPage(0))  # Returns a page object
    # print(reader.getPage(1))  # error because it has only one page
    # Pages in pdf are indexed from 0

    '''
    We have a reader object for the pdf. This object reads the pdf. Using this object we can use the getPage() method
    to get a page as a page object and perform operations.
    Like we can rotate the page using page.rotateCounterClockwise(angle)
    '''

    page = reader.getPage(0)
    rotated_page = page.rotateCounterClockwise(90)
    '''
    This returns a page object rotated counter-clockwise by 90 degrees.
    Now we need to save this to a new pdf.
    For this we need to create a writer object. This writer object is created by
    writer = PyPDF2.PDFWriter()
    Now we need to add pages to this writer object using
    writer.addpage(page)
    '''
    writer = PyPDF2.PdfWriter()
    writer.addPage(rotated_page)

    '''
    After adding the page we need to save this to a file. For that we need to create a new pdf file using open()
    after opening the file we use .write method of the writer to write it to a file
    writer.write(file_to_be_written_to)
    '''

    with open('.\\rotated_dummy_pdf.pdf', mode='wb') as new_file:
        writer.write(new_file)

with open('.\\twopage.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    print(reader)  # pypdf2 reader object
    print(reader.numPages)
    print(reader.getPage(0))
    print(reader.getPage(1))  # here it works because pdf has two pages

'''
Very important note, when the writer objects adds a page it adds reference to the
pdf page from where it is picked. Once the file is closed, even if you copy the writer object
it wont be able to write it to a new file

eg: you opened a pdf file and added all the pages to a writer and stored it 
in a global scope variable. Then you closed the parent pdf
now you open a new pdf and then you write with that writer it will fail 
because the parent file is closed
'''
