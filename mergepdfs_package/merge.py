from typing import List
import fitz  # PyMuPDF
import typer 


class Docptr:
    def __init__(self, docpath: str, start_page: int, end_page: int):
        self.docpath = docpath        
        self.start_page = start_page
        self.end_page = end_page


class Merger:
    def __init__(self, docptrs:List[Docptr], output_filename:str):
        self.docptrs = docptrs
        self.output_filename = output_filename + ".pdf"

    def merge(self):        
        # Create a new PDF to store merged pages
        output_pdf = fitz.open()

        for docptr in self.docptrs:       
            try:
                # Open the source PDF
                if not ".pdf" in docptr.docpath:
                    docptr.docpath += ".pdf"
                source_pdf = fitz.open(docptr.docpath)
                num_pages = source_pdf.page_count
                if docptr.end_page == 0:
                    docptr.end_page = num_pages

                # Validate page ranges
                if docptr.start_page < 1 or docptr.end_page > num_pages or docptr.start_page > docptr.end_page:
                    typer.secho(
                        f"Invalid page range for {docptr.docpath}: {docptr.start_page}-{docptr.end_page} (Total pages: {num_pages})",
                        fg=typer.colors.RED,
                    )
                    continue

                # Add pages to the output PDF
                output_pdf.insert_pdf(source_pdf, from_page=docptr.start_page-1, to_page=docptr.end_page-1)

                typer.secho(f"Added pages {docptr.start_page}-{docptr.end_page} from {docptr.docpath}", fg=typer.colors.GREEN)
            except Exception as e:
                typer.secho(f"Error processing {docptr.docpath}: {e}", fg=typer.colors.RED)

        # Save the merged PDF
        try:
            output_pdf.save(self.output_filename)
            typer.secho(f"Merged PDF saved to {self.output_filename}", fg=typer.colors.CYAN)
        except Exception as e:
            typer.secho(f"Error saving output PDF: {e}", fg=typer.colors.RED)
