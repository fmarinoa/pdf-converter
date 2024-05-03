from PIL import Image
import os


class PDFConverter:
    def convert_images_to_pdf(self, image_paths, output_pdf, quality=100):
        """
        Convierte una lista de imágenes en un archivo PDF.

        Args:
            image_paths (list): Lista de rutas de archivo de las imágenes.
            output_pdf (str): Ruta de archivo para guardar el archivo PDF de salida.
            quality (int, optional): Calidad de compresión del archivo PDF (valor entre 0 y 100).
                                      Default es 95.
        """
        images = []
        for image_path in image_paths:
            if os.path.isfile(image_path):
                img = Image.open(image_path)
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                images.append(img)
            else:
                print(f"Warning: File '{image_path}' not found. Skipping...")

        if images:
            images[0].save(output_pdf, save_all=True, append_images=images[1:], quality=quality)
        else:
            print("Error: No valid images found to convert.")
