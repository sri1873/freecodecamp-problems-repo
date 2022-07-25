from __future__ import annotations


class Rectangle:
    def __init__(self, width, length):
        self.length = length
        self.width = width

    def __str__(self):
        output = f"{self.__class__.__name__}(width={self.__getattribute__('width')}, height={self.__getattribute__('length')})"
        return (output)

    def set_width(self, width_giv):
        self.width = width_giv

    def set_height(self, length_giv):
        self.length = length_giv

    def get_area(self):
        return (self.length * self.width)

    def get_perimeter(self):
        return (2 * (self.length + self.width))

    def get_diagonal(self):
        return ((self.width**2 + self.length**2)**.5)

    def get_picture(self):
      if self.length>50 or self.width>50:
        return("Too big for picture.")
      else:
        output = ""
        print(self.length,self.width)
        for i in range(0, self.length):
            output += "*" * self.width + '\n'
        return (output)

    def get_amount_inside(self, obj: Square):
      rect_ar=self.get_area()
      sq_ar=obj.get_area()
      output=rect_ar//sq_ar
      return (output)


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.length = side
        self.width = side

    def __str__(self):
        output = f"{self.__class__.__name__}(side={self.__getattribute__('side')})"
        return (output)

    def set_side(self, side_giv):
        self.side = side_giv
        self.length = side_giv
        self.width = side_giv

    def set_width(self, width_giv):
        self.side = width_giv

    def set_height(self, length_giv):
        self.side = length_giv


# class Square:
