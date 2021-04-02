import tkinter as tk
from tkinter import ttk
from editBar import EditBar
from imageViewer import ImageViewer


class Main(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.filename = ""
        self.original_image = None
        self.processed_image = None
        self.is_image_selected = False
        self.is_draw_state = False
        self.is_crop_state = False

        self.filter_frame = None
        self.adjust_frame = None

        self.title("Image Editor")

        self.editbar = EditBar(master=self)
        separator1 = ttk.Separator(master=self, orient=tk.VERTICAL)
        self.image_viewer = ImageViewer(master=self)

        self.editbar.pack(pady=10,fill=tk.Y,side=tk.LEFT)
        separator1.pack(fill=tk.Y, padx=20, pady=5)
        self.image_viewer.pack(fill=tk.BOTH, padx=20, pady=10, expand=1)
