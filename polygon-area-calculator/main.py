class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self) -> str:
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        picture = ""
        for i in range(0, self.height):
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, shape) -> int:
        otherArea = shape.get_area()
        thisArea = self.get_area()
        return int(thisArea / otherArea)

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, length) -> None:
        super().__init__(length, length)

    def set_side(self, length):
        self.height = length
        self.width = length

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self) -> str:
        return f"Square(side={self.height})"