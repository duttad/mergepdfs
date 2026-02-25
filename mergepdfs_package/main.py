from typing import List
import typer
from mergepdfs_package import Docptr, Merger, Splitter


app = typer.Typer()


@app.command()
def merge(ar: List[str], op: str = "output"):
    arlen = len( ar )
    try:
        docptrs = [ Docptr(ar[i], int(ar[i+1]), int(ar[i+2])) for i in range(0,arlen,3) ]
    except Exception as e:
        print( f"Please check your input. Exception: {e} " )
    merger = Merger(docptrs=docptrs, output_filename=op)
    merger.merge()


@app.command()
def split(ar: List[str]):
    arlen = len( ar )
    filename = ar[0]
    splitter = Splitter(filename=filename)
    splitter.split()

if __name__ == "__main__":
    app()