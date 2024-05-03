from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os


class PDFConverter:
    def convert_images_to_pdf(self, image_paths, output_pdf, orientation='horizontal'):
        if orientation == 'horizontal':
            page_width, page_height = A4[1], A4[0]  # Intercambiar ancho y alto
        else:
            page_width, page_height = A4

        c = canvas.Canvas(output_pdf, pagesize=(page_width, page_height))

        for image_path in image_paths:
            if os.path.isfile(image_path):
                img = Image.open(image_path)
                if img.mode != 'RGB':
                    img = img.convert('RGB')

                # Obtener el tamaño de la imagen
                img_width, img_height = img.size

                # Calcular el tamaño escalado de la imagen para que quepa en la página A4
                scale = min(page_width / img_width, page_height / img_height)
                scaled_width = img_width * scale
                scaled_height = img_height * scale

                # Calcular las coordenadas para posicionar la imagen centrada en la página
                x = (page_width - scaled_width) / 2
                y = (page_height - scaled_height) / 2

                # Agregar la imagen al PDF
                c.drawImage(image_path, x, y, width=scaled_width, height=scaled_height, preserveAspectRatio=True)
                c.showPage()  # Agregar una nueva página para la siguiente imagen
            else:
                print(f"Warning: File '{image_path}' not found. Skipping...")

        # Guardar el PDF
        c.save()
