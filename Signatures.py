#================================================#
# Filename: Signatures.py
# Author: Eliana Wickland
# Purpose: To transform a PDF manuscript into
#          book-signature format.
# Assumptions: The file given is a PDF in default
#              formatting.
#              The user has Python and PyPDF2
#              downloaded.
#              The desired signature size is 32
#              pages.
#              The user will put 2 pages per sheet
#              using the print dialogue menu and
#              print double-sided.
# Initially Completed: 1/7/2026
# Developed on a Windows 11 machine
#=================================================#


from PyPDF2 import PdfWriter, PdfReader, PageObject
import sys

# get filename
infile_name = input("\nPlease enter the file path to the PDF: ")

# create reader and writer
try:
    inReader = PdfReader(infile_name)
except(FileNotFoundError):
    print("\nERROR: File not found. Check to see if file path is correct and run again.\n")
    sys.exit(1)
outWriter = PdfWriter()

# get page count of original PDF
page_count = len(inReader.pages)

# create a list to hold the unordered, padded new document
padded_doc = []

for i in range(page_count):
    padded_doc.append(inReader.pages[i])

# if num of original pages not divisible by 4 add blank pages to a list until it is
modFour = page_count % 4
if modFour != 0:
    new_page_count = page_count
    while(new_page_count % 4 != 0):
        new_page_count += 1
    offset = new_page_count - page_count

    # set dimensions of blank pages
    template_page = inReader.pages[0]
    pg_width = template_page.mediabox.width
    pg_height = template_page.mediabox.height

    # add blanks to list of ordered pages
    for i in range(offset):
        blank = PageObject.create_blank_page(width = pg_width, height = pg_height)
        padded_doc.append(blank)
        

# METHOD to convert the padded_doc list into a list with the printing format
def convert_to_signatures(origin_list):
    output_list = []
    group_start = 0

    while group_start < len(origin_list):
        group_size = min(32, len(origin_list) - group_start)
        sheets = group_size // 4
        for i in range(sheets):
            output_list.append(origin_list[group_start + group_size - i*2 - 1])
            output_list.append(origin_list[group_start + i*2])
            output_list.append(origin_list[group_start + i*2 + 1])
            output_list.append(origin_list[group_start + group_size - i*2 - 2])
            
        group_start += group_size
    
    return output_list


# create a list to hold the ordered signature pages
ordered_pages = convert_to_signatures(padded_doc)

# write the ordered list to the output PDF
for i in range(len(ordered_pages)):
    outWriter.add_page(ordered_pages[i])


# OUTPUT FILE =====================================================================
# create the outfile name (filename+_Signature.pdf)
outfile_name = infile_name[:-4] + "_Signature.pdf"
# write to the outfile
with open(outfile_name, "wb") as outfile:
    outWriter.write(outfile)

print('Process complete!\n', outfile_name, 'is ready.\n\nThank you for using BookSignatures!\n')