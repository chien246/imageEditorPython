from tkinter import Toplevel, Button, RIGHT, Scale, HORIZONTAL, Label
import numpy as np
import cv2


class FilterFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.original_image = self.master.processed_image
        self.filtered_image = None

        self.negative_button = Button(master=self, text="Negative")
        self.black_white_button = Button(master=self, text="Black White")
        self.sepia_button = Button(master=self, text="Sepia")
        self.sepia_label = Label(self, text="Sepia")
        self.sepia_scale = Scale(self, from_=-200, to_=200, length=250, resolution=1,orient=HORIZONTAL)
        self.emboss_label = Label(self, text="Emboss")
        self.emboss_scale = Scale(self, from_=-200, to_=200, length=250, resolution=1,orient=HORIZONTAL)

        self.gaussian_blur_label = Label(self, text="Gaussian Blur")
        self.gaussian_blur_scale = Scale(self, from_=0, to_=10, length=250, resolution=1,orient=HORIZONTAL)

        # self.gaussian_blur_button = Button(master=self, text="Gaussian Blur")
        self.cancel_button = Button(master=self, text="Cancel")
        self.apply_button = Button(master=self, text="Apply")

        self.negative_button.bind("<ButtonRelease>", self.negative_button_released)
        self.black_white_button.bind("<ButtonRelease>", self.black_white_released)
        self.sepia_scale.bind("<ButtonRelease>", self.sepia_scale_released)
        self.emboss_scale.bind("<ButtonRelease>", self.emboss_scale_released)
        self.gaussian_blur_scale.bind("<ButtonRelease>", self.gaussian_blur_scale_released)
        # self.gaussian_blur_button.bind("<ButtonRelease>", self.gaussian_blur_button_released)
        self.apply_button.bind("<ButtonRelease>", self.apply_button_released)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        self.negative_button.pack()
        self.black_white_button.pack()
        self.sepia_label.pack()
        self.sepia_scale.pack()
        self.emboss_label.pack()
        self.emboss_scale.pack()
        self.gaussian_blur_scale.pack()
        # self.gaussian_blur_button.pack()
        self.cancel_button.pack(side=RIGHT)
        self.apply_button.pack()

    def negative_button_released(self, event):
        self.negative()
        self.show_image()

    def black_white_released(self, event):
        self.black_white()
        self.show_image()

    def sepia_scale_released(self, event):
        self.sepia()
        self.show_image()

    def emboss_button_released(self, event):
        self.emboss()
        self.show_image()

    def emboss_scale_released(self, event):
        self.emboss()
        self.show_image()

    def gaussian_blur_scale_released(self, event):
        self.gaussian_blur()
        self.show_image()

    def apply_button_released(self, event):
        self.master.processed_image = self.filtered_image
        self.show_image()
        self.close()

    def cancel_button_released(self, event):
        self.master.image_viewer.show_image()
        self.close()

    def show_image(self):
        self.master.image_viewer.show_image(img=self.filtered_image)

    def negative(self):
        self.filtered_image = cv2.bitwise_not(self.original_image)

    def black_white(self):
        self.filtered_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        self.filtered_image = cv2.cvtColor(self.filtered_image, cv2.COLOR_GRAY2BGR)

    def sepia(self):
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel, delta=self.sepia_scale.get())

    def emboss(self):
        kernel = np.array([[0, -1, -1],
                           [1, 0, -1],
                           [1, 1, 0]])

        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel, delta=self.emboss_scale.get())
        

    def gaussian_blur(self):
        size = self.gaussian_blur_scale.get()*10 + 1
        self.filtered_image = cv2.GaussianBlur(self.original_image, (size, size), 0)

    def close(self):
        self.destroy()
