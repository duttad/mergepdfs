# local-pdftool
a tool for inserting, merging, and general manipulation of pages in multiple pdf documents.

## installation

### to install the latest development in the main branch

#### directly from github
`$ pip install git+https://github.com/duttad/mergepdfs.git@main`

#### after cloning the repo
navigate to the directory containing the pyproject.toml file and use pip install.

`$ pip install .`

### to install a specific tag

#### directly from github
`$ pip install git+https://github.com/duttad/mergepdfs.git@<tag>`

e.g., 
`$ pip install git+https://github.com/duttad/mergepdfs.git@v0.1.1`

#### after cloning the repo
`$ git checkout tags/<tag> -b <tag>-branch`

make sure you are in the directory containing the pyproject.toml file and use pip install.

`$ pip install .`


## usage
`$ mergepdfs merge doc1 start_page1 end_page1 doc2 start_page2 end_page2 doc3 start_page3 end_page3 doc1 start_page4 end_page4 doc2 start_page5 end_page5 ...`

`doc1, doc2,` etc. are the filenames of the pdf documents with or without the .pdf suffix.
`end_page = 0` indicates end of the document.

as in the example, pages from a document can appear in any order in the final merged document.

the output filename can be chosen with the option `--op outputfilename` (again, without the .pdf suffix)

if no option is given, the defult output filename is `output.pdf`

## sample use case
your financial institution sends you a pdf document and asks you return a scanned copy of it after signing pages 2 and the last page. with this tool, you can print only the relevant pages, sign and then "replace" the relevant pages with the scanned copies of the signed pages.