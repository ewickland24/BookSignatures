#================================================#
# Filename: Signatures.py
# Author: Eliana Wickland
# Purpose: To transform a PDF manuscript into
#          book-signature format.
# Assumptions: The file given is a PDF in default
#              formatting. 1 book-page per page in
#              sequential order, oriented with the
#              page top at the top of the page.
# Completed: TBD
# Developed on a Windows 11 machine
#=================================================#

#=====================================
# WHAT TO WORK ON NEXT TIME
# make it so it breaks longer pdfs into
# 32-page long signatures
# handle case of when less than 32 long
#=====================================

from PyPDF2 import PdfWriter, PdfReader
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

# if not divisible by 4 add blank pages to beginning until it is
modFour = page_count % 4
if modFour != 0:
    new_page_count = page_count
    while(new_page_count % 4 != 0):
        new_page_count += 1
        print('new pg cnt:', new_page_count)
    offset = new_page_count - page_count
    print('offset:', offset)
    template_page = inReader.pages[0]
    for i in range(offset):
        outWriter.add_blank_page(
            # uses the first pg for dimensions of new pg
            width= template_page.mediabox.width,
            height= template_page.mediabox.height
        )


# METHOD to add pages in order to make a single signature
def make_a_taco(start_pg_index, end_pg_index, num_pages):
    print("making a taco...")
    pgs_added_count = 0
    i = start_pg_index
    j = 0
    # print('start_pg', start_pg)
    while(pgs_added_count != num_pages):
        outWriter.add_page(inReader.pages[i])
        print('added page', i)
        pgs_added_count += 1
        if(pgs_added_count == num_pages):
            break
        outWriter.add_page(inReader.pages[end_pg_index - j].rotate(180))
        print('added page', end_pg_index - i)
        pgs_added_count += 1
        i += 1
        j += 1


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

#    try:
#       end_pg = inReader.pages[start_pg + 32]
#    catch index error:
#       end_pg = inReader.pages[-1]
#    make_a_taco(start_pg, end_pg)

# first page = 0
# find 32nd page and set as last page
# add the pages in order for that signature
# set first page to the one after the last page
# try to set the last page to the next jump of 32
# if index out of bounds error, set last page to the actual last page
# taco time!
# 
# index 0 to 31 is 32 pages
# 32 to 63 is the next 32
# (64 + 31 is 95)
# 96+31 is 127
# #

# if page_count < 32, add pages into single signature
else:
    make_a_taco(0, page_count - 1, page_count)



# else:
#    start_pg = inReader.pages[0]
#    end_pg =  inReader.pages[-1]
#    make_a_taco(start_pg, end_pg)


# create the outfile name (filename+_Signature.pdf)
outfile_name = infile_name[:-4] + "_Signature.pdf"
# write to the outfile
with open(outfile_name, "wb") as outfile:
    outWriter.write(outfile)