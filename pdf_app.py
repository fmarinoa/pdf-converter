import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pdf_converter import PDFConverter
from pdf_merger import PDFMerger


class ImageToPDFConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to PDF Converter")

        # Configurar el tamaño inicial de la ventana
        self.root.geometry("300x150")  # Ajustar dimensiones según se desee

        # Variable para almacenar la orientación seleccionada
        self.orientation = tk.StringVar()
        self.orientation.set("vertical")  # Establecer orientación vertical por defecto

        # Botones de orientación
        self.vertical_button = tk.Radiobutton(root, text="Vertical", variable=self.orientation, value="vertical")
        self.vertical_button.grid(row=1, column=1, padx=10, pady=10)

        self.horizontal_button = tk.Radiobutton(root, text="Horizontal", variable=self.orientation, value="horizontal")
        self.horizontal_button.grid(row=1, column=0, padx=10, pady=10)

        # Botón para seleccionar imágenes
        self.select_img_button = tk.Button(root, text="Seleccionar imágenes", command=self.select_images)
        self.select_img_button.grid(row=0, column=0, padx=10, pady=10)

        # Botón para convertir imágenes a PDF
        self.convert_img_button = tk.Button(root, text="Convertir a PDF", command=self.convert_to_pdf,
                                            state=tk.DISABLED)
        self.convert_img_button.grid(row=0, column=1, padx=10, pady=10)

        # Botón para seleccionar PDF's
        self.select_pdf_button = tk.Button(root, text="Seleccionar PDF's", command=self.select_pdfs)
        self.select_pdf_button.grid(row=2, column=0, padx=10, pady=10)

        # Botón para unir PDF's
        self.merge_pdf_button = tk.Button(root, text="Unir PDF's", command=self.merge_pdf, state=tk.DISABLED)
        self.merge_pdf_button.grid(row=2, column=1, padx=10, pady=10)

    def select_images(self):
        # Abrir el explorador de archivos para seleccionar imágenes
        file_paths = filedialog.askopenfilenames(filetypes=[("Imágenes", "*.jpg;*.jpeg;*.png")])
        if file_paths:
            self.file_paths = file_paths
            self.convert_img_button.config(state=tk.NORMAL)

    def convert_to_pdf(self):
        # Convertir las imágenes seleccionadas a PDF
        if hasattr(self, 'file_paths'):
            converter = PDFConverter()
            output_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF", "*.pdf")])
            if output_pdf:
                try:
                    orientation = self.orientation.get()  # Obtener la orientación seleccionada por el usuario
                    converter.convert_images_to_pdf(self.file_paths, output_pdf, orientation)
                    messagebox.showinfo("Éxito", "Las imágenes se han convertido exitosamente a PDF.")
                    os.startfile(output_pdf)
                except Exception as e:
                    messagebox.showerror("Error", f"Error al unir PDF's: {e}")

    def select_pdfs(self):
        # Abrir el explorador de archivos para seleccionar PDF's
        file_paths = filedialog.askopenfilenames(filetypes=[("PDF", "*.pdf")])
        if file_paths:
            self.file_paths = file_paths
            self.merge_pdf_button.config(state=tk.NORMAL)

    def merge_pdf(self):
        # Unir los PDF's seleccionados
        if hasattr(self, 'file_paths'):
            merger = PDFMerger()
            output_merge_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF", "*.pdf")])
            if output_merge_pdf:
                try:
                    merger.merge_pdfs(self.file_paths, output_merge_pdf)
                    messagebox.showinfo("Éxito", "Los PDF's se han unido exitosamente.")
                    # Abrir el archivo PDF en el navegador predeterminado
                    os.startfile(output_merge_pdf)
                except Exception as e:
                    messagebox.showerror("Error", f"Error al unir PDF's: {e}")
