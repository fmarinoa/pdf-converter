import os
import tkinter as tk
from tkinter import messagebox, filedialog
from pdf_converter import PDFConverter
from pdf_merger import PDFMerger


class ImageToPDFConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to PDF Converter")

        # Configurar el tamaño inicial de la ventana
        self.root.geometry("500x180")  # Ajustar dimensiones según se desee

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
        self.select_pdf_button.grid(row=3, column=0, padx=10, pady=10)

        # Botón para unir PDF's
        self.merge_pdf_button = tk.Button(root, text="Unir PDF's", command=self.merge_pdf, state=tk.DISABLED)
        self.merge_pdf_button.grid(row=3, column=1, padx=10, pady=10)

        self.sort_asc_button = tk.Button(root, text="↑", command=self.move_up)
        self.sort_asc_button.grid(row=0, column=4, padx=10, pady=5, sticky="ew")

        self.sort_desc_button = tk.Button(root, text="↓", command=self.move_down)
        self.sort_desc_button.grid(row=1, column=4, padx=10, pady=5, sticky="ew")

        # Botones para ordenar por nombre ascendente y descendente
        self.sort_asc_button = tk.Button(root, text="Ordenar A - Z", command=self.sort_file_paths_asc)
        self.sort_asc_button.grid(row=2, column=4, padx=10, pady=5, sticky="ew")

        self.sort_desc_button = tk.Button(root, text="Ordenar Z - A", command=self.sort_file_paths_desc)
        self.sort_desc_button.grid(row=3, column=4, padx=10, pady=5, sticky="ew")

        # Etiqueta para que el List Box pueda verse ancho
        self.sort_desc_button = tk.Label(root, text="aaaaaaaaaaaaaaaaaaaaaa", state=tk.DISABLED, width=0, height=0)
        self.sort_desc_button.grid(row=0, column=3)

        # Variable para almacenar las rutas de archivo seleccionadas
        self.file_paths = []

        # Lista para mostrar las rutas de archivo seleccionadas
        self.file_listbox = tk.Listbox(root)
        self.file_listbox.grid(row=0, column=2, rowspan=4, columnspan=2, sticky="nsew")

        # Añadir barra de desplazamiento vertical
        scroll_bar_y = tk.Scrollbar(self.file_listbox, orient="vertical", command=self.file_listbox.yview)
        scroll_bar_y.pack(side="right", fill="y")
        self.file_listbox.config(yscrollcommand=scroll_bar_y.set)

        # Añadir barra de desplazamiento horizontal
        scroll_bar_x = tk.Scrollbar(self.file_listbox, orient="horizontal", command=self.file_listbox.xview)
        scroll_bar_x.pack(side="bottom", fill="x")
        self.file_listbox.config(xscrollcommand=scroll_bar_x.set)

    def select_images(self):
        # Abrir el explorador de archivos para seleccionar imágenes
        file_paths = filedialog.askopenfilenames(filetypes=[("Imágenes", "*.jpg;*.jpeg;*.png")])
        if file_paths:
            self.file_paths = list(file_paths)  # Convertir la tupla a lista
            self.update_file_listbox()
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
                    messagebox.showerror("Error", f"Error al convertir imágenes a PDF: {e}")

    def select_pdfs(self):
        # Abrir el explorador de archivos para seleccionar PDF's
        file_paths = filedialog.askopenfilenames(filetypes=[("PDF", "*.pdf")])
        if file_paths:
            self.file_paths = list(file_paths)  # Convertir la tupla a lista
            self.update_file_listbox()
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
                    os.startfile(output_merge_pdf)
                except Exception as e:
                    messagebox.showerror("Error", f"Error al unir PDF's: {e}")

    # Función para ordenar por nombre de archivo
    def sort_file_paths_asc(self):
        # Ordenar las rutas de archivo en orden ascendente por nombre
        self.file_paths = list(self.file_paths)
        self.file_paths.sort()
        self.update_file_listbox()

    def sort_file_paths_desc(self):
        # Ordenar las rutas de archivo en orden descendente por nombre
        self.file_paths = list(self.file_paths)
        self.file_paths.sort(reverse=True)
        self.update_file_listbox()

    def update_file_listbox(self):
        # Limpiar la lista y agregar los nombres de archivo
        self.file_listbox.delete(0, tk.END)
        for file_path in self.file_paths:
            file_name = os.path.basename(file_path)  # Obtener solo el nombre del archivo
            self.file_listbox.insert(tk.END, file_name)

    def move_up(self):
        # Mover el elemento seleccionado hacia arriba en la lista
        selected_index = self.file_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            if selected_index > 0:
                # Convertir a lista para modificar
                file_paths_list = list(self.file_paths)
                # Intercambiar posiciones en la lista
                file_paths_list[selected_index], file_paths_list[selected_index - 1] = \
                    file_paths_list[selected_index - 1], file_paths_list[selected_index]
                # Convertir de nuevo a tupla
                self.file_paths = tuple(file_paths_list)
                # Actualizar la vista del listbox
                self.update_file_listbox()
                # Mantener el mismo elemento seleccionado
                self.file_listbox.selection_set(selected_index - 1)

    def move_down(self):
        # Mover el elemento seleccionado hacia abajo en la lista
        selected_index = self.file_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            if selected_index < len(self.file_paths) - 1:
                # Convertir a lista para modificar
                file_paths_list = list(self.file_paths)
                # Intercambiar posiciones en la lista
                file_paths_list[selected_index], file_paths_list[selected_index + 1] = \
                    file_paths_list[selected_index + 1], file_paths_list[selected_index]
                # Convertir de nuevo a tupla
                self.file_paths = tuple(file_paths_list)
                # Actualizar la vista del listbox
                self.update_file_listbox()
                # Mantener el mismo elemento seleccionado
                self.file_listbox.selection_set(selected_index + 1)
