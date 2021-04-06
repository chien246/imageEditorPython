from tkinter import Frame, Button, LEFT, X, BOTTOM, RIGHT, TOP
from tkinter import filedialog
from tkinter import *
from filterFrame import FilterFrame
from adjustFrame import AdjustFrame
import cv2


class EditBar(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master=master,bg="#EED5D2")

        self.new_icon = PhotoImage(file="icon/new.png")
        self.new_icon = self.new_icon.subsample(15, 15)
        self.save_icon = PhotoImage(file="icon/save.png")
        self.save_icon = self.save_icon.subsample(15, 15)
        self.crop_icon = PhotoImage(file="icon/crop.png")
        self.crop_icon = self.crop_icon.subsample(15, 15)
        self.draw_icon = PhotoImage(file="icon/draw.png")
        self.draw_icon = self.draw_icon.subsample(25,25)
        self.adjust_icon = PhotoImage(file="icon/adjust.png")
        self.adjust_icon = self.adjust_icon.subsample(15, 15)
        self.filter_icon = PhotoImage(file="icon/filter.png")
        self.filter_icon = self.filter_icon.subsample(15, 15)
        self.clear_icon = PhotoImage(file="icon/clear.png")
        self.clear_icon = self.clear_icon.subsample(15, 15)

        self.new_button = Button(self, text="New",image=self.new_icon,compound=LEFT,anchor="w",bg="#CDB7B5")
        self.save_button = Button(self, text="Save",image=self.save_icon,compound=LEFT,anchor="w",bg="#CDB7B5")
        self.save_as_button = Button(self, text="Save As",image=self.save_icon,compound=LEFT,anchor="w",bg="#CDB7B5")
        self.draw_button = Button(self, text="Draw",image=self.draw_icon,compound=LEFT,anchor="w",bg="#CDB7B5")
        self.crop_button = Button(self, text="Crop",image=self.crop_icon,compound=LEFT,anchor="w",bg="#CDB7B5")
        self.filter_button = Button(self, text="Filter",image=self.filter_icon,compound=LEFT,anchor="w",bg="#CDB7B5")
        self.adjust_button = Button(self, text="Adjust",image=self.adjust_icon,compound=LEFT,anchor="w",bg="#CDB7B5")
        self.clear_button = Button(self, text="Clear",image=self.clear_icon,compound=LEFT,anchor="w",bg="#CDB7B5")

        self.new_button.bind("<ButtonRelease>", self.new_button_released)
        self.save_button.bind("<ButtonRelease>", self.save_button_released)
        self.save_as_button.bind("<ButtonRelease>", self.save_as_button_released)
        self.draw_button.bind("<ButtonRelease>", self.draw_button_released)
        self.crop_button.bind("<ButtonRelease>", self.crop_button_released)
        self.filter_button.bind("<ButtonRelease>", self.filter_button_released)
        self.adjust_button.bind("<ButtonRelease>", self.adjust_button_released)
        self.clear_button.bind("<ButtonRelease>", self.clear_button_released)

        self.new_button.pack(side=TOP,fill=X,padx=20,pady=5)
        self.save_button.pack(side=TOP,fill=X,padx=20,pady=5)
        self.save_as_button.pack(side=TOP,fill=X,padx=20,pady=5)
        self.draw_button.pack(side=TOP,fill=X,padx=20,pady=5)
        self.crop_button.pack(side=TOP,fill=X,padx=20,pady=5)
        self.filter_button.pack(side=TOP,fill=X,padx=20,pady=5)
        self.adjust_button.pack(side=TOP,fill=X,padx=20,pady=5)
        self.clear_button.pack(side=TOP,fill=X,padx=20,pady=5)

    def new_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.new_button:
            if self.master.is_draw_state:
                self.master.image_viewer.deactivate_draw()
            if self.master.is_crop_state:
                self.master.image_viewer.deactivate_crop()

            filename = filedialog.askopenfilename()
            image = cv2.imread(filename, cv2.IMREAD_COLOR)
            print(image)

            if image is not None:
                self.master.filename = filename
                self.master.original_image = image.copy()
                self.master.processed_image = image.copy()
                self.master.image_viewer.show_image()
                self.master.is_image_selected = True

    def save_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_button:
            if self.master.is_image_selected:
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()

                save_image = self.master.processed_image
                image_filename = self.master.filename
                cv2.imwrite(image_filename, save_image)

    def save_as_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_as_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                original_file_type = self.master.filename.split('.')[-1]
                filename = filedialog.asksaveasfilename()
                filename = filename + "." + original_file_type

                save_image = self.master.processed_image
                cv2.imwrite(filename, save_image)

                self.master.filename = filename

    def draw_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.draw_button:
            if self.master.is_image_selected:
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                else:
                    self.master.image_viewer.activate_draw()

    def crop_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.crop_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                else:
                    self.master.image_viewer.activate_crop()

    def filter_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.filter_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.filter_frame = FilterFrame(master=self.master)
                self.master.filter_frame.grab_set()

    def adjust_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.adjust_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.adjust_frame = AdjustFrame(master=self.master)
                self.master.adjust_frame.grab_set()

    def clear_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.clear_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.processed_image = self.master.original_image.copy()
                self.master.image_viewer.show_image()
