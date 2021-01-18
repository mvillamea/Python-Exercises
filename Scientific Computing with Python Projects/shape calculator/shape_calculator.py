
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return 'Rectangle(width='+str(self.width)+', height='+str(self.height)+')'

    def set_width(self, new_width):
        self.width=new_width

    def set_height(self, new_height):
        self.height=new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*self.width + 2*self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        picture = ''
        if self.height>50 or self.width>50:
            picture = 'Too big for picture.'
        else:
            for i in range(self.height):
                picture += '*'*self.width + '\n'
        return picture

    def get_amount_inside(self, shape):
        return int(self.width//shape.width)*int(self.height//shape.height)


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.width = self.side
        self.height = self.side

    def __str__(self):
        return 'Square(side='+str(self.side)+')'

    def set_side(self, new_side):
        self.side = new_side
        self.height = new_side
        self.width = new_side

    def set_height(self, new_side):
        self.set_side(new_side)

    def set_width(self, new_side):
        self.set_side(new_side)



