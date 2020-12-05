pdfToText by Chan Qin Liang

Adapted from this algorithm for the conversion of individual pdf files: 
https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/

Description:
This is a CLI tool for batch conversion of text-based pdf files to txt files. 

Motivation:
While there are many existing free tools that convert pdfs with textual data to txt, they do not work if the text is stored as images in the pdf and hence cannot be indexed. In such cases, OCR tools have to be used to process the images into textual data instead. Those that are able to do so are either paid, or that they can only convert one pdf at a time. I wrote this script to convert the pdfs generated from my previous mobile notetaking app to txt files in bulk so that I can transfer old notes to a new notetaking app after switching phones.

Requirements (other than specified in requirements.txt):
Tesseract OCR
python 3

Command format:
py <path to pdf2txt.py> <input directory filepath> <output directory path>

Possible improvements:
Use parallel threads



