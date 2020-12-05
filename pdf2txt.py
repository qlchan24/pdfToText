from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
from pathlib import Path
import sys
import shutil


def convertPDF(input_path, output_path, temp_path):
    '''
    Converts a pdf file into a text file 
    '''

    file_name = input_path.stem
    PDF_file = str(input_path)

    '''
    Converting PDF to images
    '''

    # Store all the pages of the PDF in a variable
    pages = convert_from_path(PDF_file)

    # Counter to store images of each page of PDF to image
    image_counter = 1

    # Iterate through all the pages stored above
    for page in pages:

        # Declaring filename for each page of PDF as JPG
        image_dir = temp_path
        imagefilename = image_dir+file_name+"_page_"+str(image_counter)+".jpg"

        # Save the image of the page in system
        page.save(imagefilename, 'JPEG')

        # Increment the counter to update filename
        image_counter = image_counter + 1

    '''
    Recognizing text from the images using OCR
    '''

    # Variable to get count of total number of pages
    filelimit = image_counter-1

    # Creating a text file to write the output
    output_dir = output_path
    outfile = Path(output_dir, file_name+".txt")

    # Open the file in append mode so that
    # All contents of all images are added to the same file
    f = open(str(outfile), "a")

    # Iterate from 1 to total number of pages
    for i in range(1, filelimit + 1):

        # Set filename to recognize text from
        imagefilename = image_dir+file_name+"_page_"+str(i)+".jpg"

        # Recognize the text as string in image using pytesserct
        text = str(((pytesseract.image_to_string(Image.open(imagefilename)))))

        # The recognized text is stored in variable text
        # Any string processing may be applied on text
        # Here, basic formatting has been done:
        # In many PDFs, at line ending, if a word can't
        # be written fully, a 'hyphen' is added.
        # The rest of the word is written in the next line
        text = text.replace('-\n', '')

        # Finally, write the processed text to the file.
        f.write(text)

    # Close the file after writing all the text.
    f.close()


def main(argv, temp_dir):
    '''
    Main driver of the conversion algorithm
    '''

    basepath = Path(argv[0])

    # List all files in directory using pathlib
    files_in_basepath = basepath.iterdir()

    for item in files_in_basepath:

        # convert pdf
        if item.is_file():
            convertPDF(item, argv[1], temp_dir)

        # recursively copies the structure of the input file directory into the output file directory
        if item.is_dir():

            output_dir_path = Path(argv[1], item.name)

            if not output_dir_path.exists():
                output_dir_path.mkdir()

            main([str(item), str(output_dir_path)], temp_dir)


if __name__ == "__main__":

    # check for excess or missing arguments
    if len(sys.argv) != 3:
        print('Invalid format!\n Correct format: \npy pdf2txt.py <input directory filepath> <output directory path>\n')
        sys.exit(2)

    # directory to store temporary images
    TEMP_DIR = "images\\"

    # create directory if it does not exist
    if not Path(TEMP_DIR).exists():
        Path(TEMP_DIR).mkdir()

    main(sys.argv[1:], TEMP_DIR)

    # remove temporary directory and its contents
    try:
        shutil.rmtree(TEMP_DIR)
    except OSError as e:
        print(f'Error: {TEMP_DIR} : {e.strerror}')
