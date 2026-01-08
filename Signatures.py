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

from PyPDF2 import PdfWriter, PdfReader, PageObject
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

# create a list to hold the unordered, padded document
padded_doc = []

for i in range(page_count):
    padded_doc.append(inReader.pages[i])

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
        blank = PageObject.create_blank_page(width = pg_width, height = pg_height)
        padded_doc.append(blank)
        # outWriter.add_blank_page(width = pg_width, height = pg_height)
        
print('after blank: len list', len(padded_doc))


# # METHOD to add pages in order to make a single signature
# def make_a_taco(start_pg_index, end_pg_index, group_size):
#     print("making a taco...")
#     pgs_added_count = 0
#     i = start_pg_index
#     j = 0
#     # print('start_pg', start_pg)
#     while(pgs_added_count != group_size):
#         # flip two added pgs if j is even
#         # if(j % 2 == 0):
#         #     ordered_pages.append(inReader.pages[i].rotate(180))
#         #     # outWriter.add_page(inReader.pages[i].rotate(180))
#         #     #print('added page', i)
#         #     pgs_added_count += 1
#         #     if(pgs_added_count == num_pages):
#         #         break
#         #     ordered_pages.append(inReader.pages[end_pg_index - j].rotate(180))
#         #     # outWriter.add_page(inReader.pages[end_pg_index - j].rotate(180))
#         #     #print('added page', end_pg_index - i)
#         #     pgs_added_count += 1

#         # # add pages without flipping when j is odd
#         # else:
#         ordered_pages.append(inReader.pages[i])
#         # outWriter.add_page(inReader.pages[i])
#         #print('added page', i)
#         pgs_added_count += 1
#         if(pgs_added_count == group_size):
#             raise RuntimeError('BAD THINGS HAPPENED')
#         ordered_pages.append(inReader.pages[end_pg_index - j])
#         # outWriter.add_page(inReader.pages[end_pg_index - j])
#         #print('added page', end_pg_index - i)
#         pgs_added_count += 1
#         i += 1 # goes to next front page
#         j += 1
    
#     print('after rest:', len(ordered_pages))


# convert document into ordered signatures
#ensureSourceHasMultipleOf4Pages() 
#firstPage = 0
#while firstPage < totalPages
#  groupPages = min(32, totalPages - firstPage
#  realPages = (groupPages // 4)
#  For i in realPages 
#    add(flip(pages[groupStart + groupPages - i*2 - 1]))
#    add(flip(pages[groupStart + i*4]) ))
#    add(pages[groupStart + groupPages - i*2 - 1])
#    add(pages[groupStart + i*4 + 1]))
#  firstPage += groupPages

# METHOD to convert the padded_doc list into a list with the printing format
def convert_to_signatures(origin_list):
    output_list = []
    group_start = 0

    while group_start < len(origin_list):
        group_size = min(32, len(origin_list) - group_start)
        sheets = group_size // 4
        for i in range(sheets):
            output_list.append(origin_list[group_start + group_size - i*2 - 1])#.rotate(180))
            output_list.append(origin_list[group_start + i*2])#.rotate(180))
            output_list.append(origin_list[group_start + i*2 + 1])
            output_list.append(origin_list[group_start + group_size - i*2 - 2])
            
        group_start += group_size
    
    return output_list

# # if page_count > 32, divide into several signatures
# if(page_count > 32):
#     # calculate how many signatures there will be
#     num_signatures = math.ceil(page_count / 32)
#     #print(page_count, '/', 32, '=', math.ceil(page_count / 32))
#     #print(num_signatures)
#     for sig in range(num_signatures):
#         start_pg_index = sig * 32
#         print('start pg:', start_pg_index)
#         if(start_pg_index + 31 >= page_count):
#             print("final page signature!")
#             end_pg = page_count - 1
#             print('end_pg:', end_pg)
#             make_a_taco(start_pg_index, end_pg, (page_count - (start_pg_index + 1)))
#         else:
#             end_pg = start_pg_index + 31
#             print('end_pg:', end_pg)
#             make_a_taco(start_pg_index, end_pg, 32)


# # if page_count < 32, add pages into single signature
# else:
#     make_a_taco(0, page_count - 1, page_count)


# create a list to hold the ordered signature pages
ordered_pages = convert_to_signatures(padded_doc)

print('num pages', len(ordered_pages))

# for i in range(0, len(ordered_pages), 4):
#     outWriter.add_page(ordered_pages[i].rotate(180))
#     outWriter.add_page(ordered_pages[i + 1].rotate(180))
#     outWriter.add_page(ordered_pages[i + 2])
#     outWriter.add_page(ordered_pages[i + 3])

# 63, 32, 62, 33
# for i in range(len(ordered_pages) // 2):
#     if(i % 2 == 0):
#         print('flipped when i was', i)
#         ordered_pages[i].rotate(180)
#         ordered_pages[i + 1].rotate(180)

# for i in range(len(ordered_pages)):
#     outWriter.add_page(ordered_pages[i])
    
#print(ordered_pages)
# merge_pages(ordered_pages)

# write the ordered list to the output PDF
for i in range(len(ordered_pages)):
    outWriter.add_page(ordered_pages[i])

# OUTPUT FILE =====================================================================
# create the outfile name (filename+_Signature.pdf)
outfile_name = infile_name[:-4] + "_Signature.pdf"
# write to the outfile
with open(outfile_name, "wb") as outfile:
    outWriter.write(outfile)