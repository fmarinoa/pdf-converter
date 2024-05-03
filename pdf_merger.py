import os
import shutil
from pypdf import PdfMerger


class PDFMerger:
    def merge_pdfs(self, pdf_paths, output_pdf):
        merger = PdfMerger()
        for pdf_path in pdf_paths:
            merger.append(pdf_path)

        # Crear un archivo temporal para el PDF combinado
        temp_output_pdf = output_pdf + '.tmp'
        with open(temp_output_pdf, 'wb') as temp_file:
            merger.write(temp_file)

        # Cerrar el merger
        merger.close()

        # Reemplazar el archivo original con el archivo temporal
        if os.path.exists(output_pdf):
            os.remove(output_pdf)
        shutil.move(temp_output_pdf, output_pdf)
