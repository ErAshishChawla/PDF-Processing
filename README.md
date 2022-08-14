# PDF-Processing
This repository contains basic info about how to interact with PDFs using Python and perform PDF Merging and PDF Watermarking

This folder contains sample pdfs for practice.(dummy.pdf, twopage.pdf, wtr.pdf)

PDFs with Python.py file contains the basic info about the library used and how to interact with pdfs

MergingPDFs.py file contains code about how to merge pdfs. This code should be run through command line
using python MergingPDFs.py <file1> <file2> <file3> ...
You can provide any number of pdf files as arguments. Condition is that the file must be present in the same folder as of the code file.
This code also checks the format of the file and various other constraints.

PDF_Watermarker.py file contains the code about watermarking pdfs. This code should be run through command line using 
python PDF_Watermarker.pdf <watermarkerfile> <file1> <file2>.......
You can provide any number of arguments. Condition is the first file must be the pdf watermarker and other files should be
the files to be watermarked. Another requirement is that the file must be present in the same folder as of the code file.
This code also checks the format of the file and various other constraints.
