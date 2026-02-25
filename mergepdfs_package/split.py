import fitz
import typer 


class Splitter:
    def __init__(self, filename ):
        self.filename = filename


    def split(self):
        doc = fitz.open( self.filename )

        for page_num in range(doc.page_count):
            # Create a new, empty document in memory
            new_doc = fitz.open() 
            # Insert the current page from the original document
            new_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)
            
            output_path = f"{self.filename.rsplit('.', 1)[0]}_page_{(page_num + 1):02}.pdf"
            # Save the new document
            new_doc.save(output_path)
            new_doc.close()
            print(f"Created {output_path}")
        
        doc.close()
    

