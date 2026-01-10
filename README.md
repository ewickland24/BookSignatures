# BookSignatures

**BookSignatures is a command line tool for converting PDF manuscripts into a PDF with the page order needed to print it like a book.** Printed booklets have 4 pages on each sheet of printer paper, with 2 on the front and 2 on the back.

### Prerequisites
- Python 3.10 or newer
- pip (included with Python)

### Quick Start
1. Install Python 3
2. Download the BookSignatures repository as a ZIP file and extract
3. Open a command prompt in the folder where it was extracted
4. Run these commands:
```bash
python -m pip install -r requirements.txt
python Signatures.py
```

## Installation

### Step 1: Download Python
If you don't already have Python3, you can download it at https://www.python.org/downloads/. Make sure to download the version appropriate for your machine.

### Step 2: Download BookSignatures
There are two ways to download BookSignatures onto your device. If you don't have Git, use the first option.

FIRST OPTION:
Find the green "<>Code" button on the repository page.
![An image of the BookSignatures repository page showing the "<>Code" button](assets\Screenshot 2026-01-09 161006.png)

Click it, then look at the bottom of the menu and select "Download ZIP".
![An image showing the "Download ZIP" button.](assets\Screenshot 2026-01-09 161724.png)

Extract the ZIP file to a dedicated place in your file system.

SECOND OPTION:
If you have Git installed, enter the following command into your command prompt.
```bash
git clone https://github.com/ewickland24/BookSignatures
```

### Step 3: Install Software Dependencies
BookSignatures uses PyPDF2. It is highly recommended to set up a virtual environment (venv) before installing the dependencies and to run BookSignatures there to keep all the needed software in one place (though not required).

To download BookSignatures' dependencies **without a venv**, enter the command below.
```bash
python -m pip install -r requirements.txt
```

### Step 4: Setting up a Virtual Environment (HIGHLY RECOMMENDED)
To set up a venv, enter the following command into your command prompt:

Windows:
```bash
python -m venv venv
```
Then activate it using the following command:
```bash
venv\Scripts\activate
```

Mac:
```bash
python3 -m venv venv
```
Then activate it using the following command:
```bash
source venv/bin/activate
```
Now that you've set up the venv, you can install BookSignatures' dependencies by entering the following command into your command prompt:
```bash
python -m pip install -r requirements.txt
```

## Usage

### Step 1: Installation
If you haven't already, please follow the installation instructions above.

### Step 2: Running BookSignatures
Go to your command prompt (or Terminal on Mac), navigate to the folder BookSignatures is stored in, and enter the following command:

Windows and Mac:
 ```bash
python Signatures.py
```
Note: Some Windows users may need to use py instead of python.

If the program successfully boots, it will request the filename of a PDF:
```txt
Please enter the filename: 
```
Paste the path to the PDF into the command prompt. You can usually copy the file path by navigating to the file in your file explorer, and either copying the path out of the bar at the top, or by finding an option "Copy path" in a menu. Hit enter.

BookSignatures will then attempt to find the PDF in your file system and read it. If the path is invalid, the program will exit. Check and correct the file path and try again, starting with Step 2.

When it is finished, BookSignatures will display the following message:
```txt
Process complete!
C:\ExampleDirectory\example_Signature.pdf is ready.

Thank you for using BookSignatures!
```

### Step 3: Locating Your New PDF
BookSignatures will store the new PDF in the same folder as the original. You can search for it by pasting the filename given by the program into the search bar in your file explorer.

It should be noted that **if there is already a file with the name assigned by the program when BookSignatures is run, BookSignatures will overwrite that file**. This would occur if the program is run multiple times using the same original PDF or PDFs with the same name. If you want to keep previous generated PDFs, then it would be best to rename the file you want to keep. For example, one could change myStory_Signature.pdf to myStory_Signature1.pdf. Then, when BookSignatures is run on myStory.pdf again, it will generate a different PDF named myStory_Signature.pdf and not overwrite the first one it generated.

### Step 4: Printing
Search for the new PDF by entering the name displayed by the program into your file explorer. When it appears, open it in your browser by double-clicking the file.
![An image showing an example PDF open in a browser.](assets\Screenshot 2026-01-09 162511.png)
Select the "Print" option, and change the settings so that there are 2 pages per page and the printing will be double-sided.
![An image showing the correct print settings.](assets\Screenshot 2026-01-09 162832.png)

Hit the "Print" button.

When the document prints, it will print all at once. For an easier time keeping the signatures separate, remove each group of 8 sheets of paper as they get printed. If preferreed, you can also separate the pages after the printing is complete or collate the sheets if your printer supports that.

## Printing Assumptions

The following are key assumptions made what the user wants and how they will print the new PDF:

1. The desired signature size is 32 pages.
2. The user will assign 2 pages per page **using the printing dialog menu** and print double-sided. 
3. The pages in original PDF will be in consecutive order.
4. The user will input a path to a PDF only.

## Background

This project was developed to help amateur authors test-print their manuscripts in a book-like format on a printer at home. For larger manuscripts, it's often easier to bind smaller groups of pages, or signatures, together into a full book, and so manuscript pages are often broken up into signatures. This program uses 32-page signatures. BookSignatures will also properly format documents shorter than 32 pages.

## Features

NEW PDF: BookSignatures does not change the original PDF provided by the user. It reads the pages of the user's PDF, makes a copy of each page without changes, and generates a new PDF. This PDF will be stored in the same folder as the original.

NAMING SCHEME: The new PDF will append _Signature.pdf to the end of the name used for the original PDF. For example, if the original is named myStory.pdf, the new PDF will be named myStory_Signature.pdf.

DOCUMENT PADDING: When the number of pages in the original document is not evenly divisible by 4, blank pages are added to both the beginning and the end of the new PDF. (This is so that the program can evenly divide pages across sheets of printer paper.) Blank pages are added in alternating order, starting at the end. Each blank page has the same dimensions as the first page of the original PDF.

SIGNATURES: BookSignatures breaks the original document up into 32-page signatures and organizes the signatures in consecutive order. If the original document contains fewer than 32 pages, then the entire document will be contained in one signature which may be printed as a booklet.

PAGE SIZE AND IMAGES: Any page size will work with BookSignatures. Any PDF information that can be interpreted by PyPDF2, including images, will be preserved in the new PDF.

## Support

If you run into any issues while using BookSignatures or have any questions, please send an email to elianawickland@letu.edu and I'll get back to you as soon as I can!

## Roadmap (Future Updates)

JANUARY 2026: Proper error-handling for an invalid path.

FEBRUARY 2026: Support for printing single-signature booklets that are larger than 32 pages.

## License

Standard Copyright, 2026.