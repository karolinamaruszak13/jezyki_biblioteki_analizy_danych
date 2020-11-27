class Figure:
    def __init__(self, color, name, size=1, center=[0, 0]): # lista jako wartość domyślna to słaby pomysł
        self.center = center
        self.border_color = color
        self.background_color = color
        self.name = name
        self.size = size
        self.rotation = 0
        self.figure_representation = lambda name: f"{self.background_color} {name}  with id {self.name} and size equal to {self.size} " \
                                                  f"centered on {self.center} rotated by {self.rotation}° with {self.border_color} border." # lepiej zdefiniować metodę, niż zapisywać lambdę
    # coś mało tej funkcjonalności

class Circle(Figure):
    def __init__(self, color, name, **kwargs):
        super().__init__(color, name, **kwargs)

    def __str__(self):
        return self.figure_representation('Circle')


class Square(Figure):
    def __init__(self, color, name, **kwargs):
        super().__init__(color, name, **kwargs)

    def __str__(self):
        return self.figure_representation('Square')


class Rectangle(Figure):
    def __init__(self, color, name, **kwargs):
        super().__init__(color, name, **kwargs)

    def __str__(self):
        return self.figure_representation('Rectangle')


class Triangle(Figure):
    def __init__(self, color, name, **kwargs):
        super().__init__(color, name, **kwargs)

    def __str__(self):
        return self.figure_representation('Triangle')


