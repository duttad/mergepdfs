# mergepdfs
A tool for inserting, merging, and general manipulation of pages in multiple pdf documents.

## Installation

### To install the latest development in the main branch

#### Directly from github
`$ pip install git+https://github.com/duttad/mergepdfs.git@main`

#### After cloning the repo
Navigate to the directory containing the pyproject.toml file and use pip install.

`$ pip install .`

### To install a specific tag

#### Directly from github
`$ pip install git+https://github.com/duttad/mergepdfs.git@<tag>`

E.g., 
`$ pip install git+https://github.com/duttad/mergepdfs.git@v0.1.1`

#### After cloning the repo
`$ git checkout tags/<tag> -b <tag>-branch`

Make sure you are in the directory containing the pyproject.toml file and use pip install.

`$ pip install .`


## Usage
`$ mergepdfs merge doc_1 start_page_1 end_page_1 doc_2 start_page_2 end_page_2 doc_3 start_page_3 end_page_3 doc_1 start_page_4 end_page_4 doc_2 start_page_5 end_page_5 ...`

`doc1, doc2,` etc. are the filenames of the pdf documents with or without the .pdf suffix.
Page numbering is `1-based`. That is, the first page of the document has the page number `1`, etc. 
The special page number `end_page = 0` indicates end of the document (last page).

As in the example, pages from a document can appear in any order in the final merged document.

The output filename can be chosen with the option `--op outputfilename` (without the .pdf suffix)

If no option is given, the defult output filename is `output.pdf`

## Sample use case
Your financial institution sends you a pdf document and asks you return a scanned copy of it after signing pages 2 and the last page. with this tool, you can print only the relevant pages, sign, and then "replace" the relevant pages with the scanned copies of the signed pages.
