#================================================#
# Filename: Signatures.py
# Author: Eliana Wickland
# Purpose: To transform a PDF manuscript into
#          book-signature format.
# Assumptions: The file given is a PDF in default
#              formatting. 1 book-page per PDF-page in
#              sequential order, oriented with the
#              page top at the top of the page.
# Completed: TBD
# Developed on a Windows 11 machine
#=================================================#

from PyPDF2 import PdfWriter, PdfReader#, PageObject, Transformation
import math

# get filename
infile_name = input("Please enter the filename: ")

# idea: make a statement that you can enter "info" and then it'll output that it
# makes signatures of 32, adds blank pages to front, and the ending page orientation

# try/catch of file not found: "Check if the file is in the same folder as this program."

# create reader and writer
inReader = PdfReader(infile_name)
outWriter = PdfWriter()

# get page count
page_count = len(inReader.pages)

# consider adding case where there's 0 pages

# create a list to hold the ordered signature pages before merging
#ordered_pages = []

# if not divisible by 4 add blank pages to a list until it is
modFour = page_count % 4
if modFour != 0:
    new_page_count = page_count
    while(new_page_count % 4 != 0):
        new_page_count += 1
        print('new pg cnt:', new_page_count)
    offset = new_page_count - page_count
    print('offset:', offset)
    # set dimensions of blank pages
    template_page = inReader.pages[0]
    pg_width = template_page.mediabox.width
    pg_height = template_page.mediabox.height
    # add blanks to list of ordered pages
    for i in range(offset):
        # blank = PageObject.create_blank_page(width = pg_width, height = pg_height)
        # ordered_pages.append(blank)
        outWriter.add_blank_page(width = pg_width, height = pg_height)


# METHOD to add pages in order to make a single signature
def make_a_taco(start_pg_index, end_pg_index, num_pages):
    print("making a taco...")
    pgs_added_count = 0
    i = start_pg_index
    j = 0
    # print('start_pg', start_pg)
    while(pgs_added_count != num_pages):
        # flip two added pgs if j is even
        if(j % 2 == 0):
            # ordered_pages.append(inReader.pages[i].rotate(180))
            outWriter.add_page(inReader.pages[i].rotate(180))
            #print('added page', i)
            pgs_added_count += 1
            if(pgs_added_count == num_pages):
                break
            # ordered_pages.append(inReader.pages[end_pg_index - j].rotate(180))
            outWriter.add_page(inReader.pages[end_pg_index - j].rotate(180))
            #print('added page', end_pg_index - i)
            pgs_added_count += 1

        # add pages without flipping when j is odd
        else:
            # ordered_pages.append(inReader.pages[i])       
            outWriter.add_page(inReader.pages[i])
            #print('added page', i)
            pgs_added_count += 1
            if(pgs_added_count == num_pages):
                break
            # ordered_pages.append(inReader.pages[end_pg_index - j])
            outWriter.add_page(inReader.pages[end_pg_index - j])
            #print('added page', end_pg_index - i)
            pgs_added_count += 1
        i += 1
        j += 1

# METHOD to merge each 2 properly-ordered pages onto one page
# def merge_pages(page_list):
#     print('merging pages...')
#     page_width = page_list[0].mediabox.width
#     sheet_height = page_list[0].mediabox.height
#     # create the translation for the right page to be on the right side of the sheet
#     to_right_side = Transformation().translate(tx = page_width, ty = 0)

#     for i in range(0, len(page_list), 2):
#         sheet = PageObject.create_blank_page(width = page_width * 2, height = sheet_height)
#         sheet.merge_page(page_list[i])
#         page_list[i + 1].add_transformation(to_right_side)
#         sheet.merge_page(page_list[i + 1])
#         outWriter.add_page(sheet)       


# if page_count > 32, divide into several signatures
if(page_count > 32):
    # calculate how many signatures there will be
    num_signatures = math.ceil(page_count / 32)
    #print(page_count, '/', 32, '=', math.ceil(page_count / 32))
    #print(num_signatures)
    for sig in range(num_signatures):
        start_pg_index = sig * 32
        print('start pg:', start_pg_index)
        if(start_pg_index + 31 >= page_count):
            print("final page signature!")
            end_pg = page_count - 1
            print('end_pg:', end_pg)
            make_a_taco(start_pg_index, end_pg, (page_count - (start_pg_index + 1)))
        else:
            end_pg = start_pg_index + 31
            print('end_pg:', end_pg)
            make_a_taco(start_pg_index, end_pg, 32)


# if page_count < 32, add pages into single signature
else:
    make_a_taco(0, page_count - 1, page_count)

#print(ordered_pages)
# merge_pages(ordered_pages)

# OUTPUT FILE =====================================================================
# create the outfile name (filename+_Signature.pdf)
outfile_name = infile_name[:-4] + "_Signature.pdf"
# write to the outfile
with open(outfile_name, "wb") as outfile:
    outWriter.write(outfile)