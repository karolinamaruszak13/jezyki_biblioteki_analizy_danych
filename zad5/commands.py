from jezyki_biblioteki_analizy_danych.zad5.figure import *
from jezyki_biblioteki_analizy_danych.zad5.my_exceptions import *
import re


class Commands:
    def __init__(self):
        self.quit = False
        self.available_figures = ["circle", "square", "rectangle", "triangle"]
        self.colors = ["black", "white", "red", "green", "blue", "cyan", "magenta", "yellow"]
        command_help = Command('help', 'help', number_of_run_args=0, run=self.help)
        command_quit = Command('quit', 'quit', number_of_run_args=0, run=self.quit_f)
        command_add = Command('add', 'add <figure> <name> <size>', number_of_run_args=3, run=self._add)
        command_move = Command('move', 'move <name> <vector>', number_of_run_args=3, run=self._move)
        command_remove = Command('remove', 'remove <name>', number_of_run_args=1, run=self._remove)
        command_scale = Command('scale', 'scale <name> <ratio>', number_of_run_args=2, run=self._scale)
        command_rotate = Command('rotate', 'rotate <name> <angle>', number_of_run_args=2, run=self._rotate)
        command_set_border_color = Command('set_border_color', 'set border color <name> <color>', number_of_run_args=2,
                                           run=self._set_border_color)
        command_set_background_color = Command('set_background_color', 'set background color <name> <color>',
                                               number_of_run_args=2, run=self._set_background_color)
        self.available_commands = {command_add.name: command_add, command_move.name: command_move,
                                   command_remove.name: command_remove,
                                   command_scale.name: command_scale,
                                   command_rotate.name: command_rotate,
                                   command_set_border_color.name: command_set_border_color,
                                   command_set_background_color.name: command_set_background_color,
                                   command_help.name: command_help, command_quit.name: command_quit}

    def _add(self, figure, name, size, image):
        size = float(size)
        if figure not in self.available_figures:
            raise FigureNotFoundError("Invalid name of figure")
        if not bool(re.fullmatch('^[a-z]\w+$', name)):
            raise InvalidNameError('Invalid id name')
        if size <= 0:
            raise InvalidArgumentError("Size must be a positive value")

        else:
            figure = figure.lower()
            if figure == 'circle':
                image.figures.append(Circle(color="blue", name=name, size=size))
            if figure == 'square':
                image.figures.append(Square(color="yellow", name=name, size=size))
            if figure == 'rectangle':
                image.figures.append(Rectangle(color="red", name=name, size=size))
            if figure == 'triangle':
                image.figures.append(Triangle(color="green", name=name, size=size))

    def _move(self, name, first, second, image):
        try:
            figure = image.find_figure(name)
        except FigureNotFoundError as e:
            print(e)
            return
        figure.center[0] += float(first)
        figure.center[1] += float(second)

    def _remove(self, name, image):
        try:
            figure = image.find_figure(name)
        except FigureNotFoundError as e:
            print(e)
            return
        image.figures.remove(figure)

    def _scale(self, name, ratio, image):
        ratio = float(ratio)
        try:
            figure = image.find_figure(name)
        except FigureNotFoundError as e:
            print(e)
            return
        # print(figure.scale)
        if ratio == 0:
            raise InvalidArgumentError("Ratio can't be 0")
        figure.size = ratio

    def _rotate(self, name, angle, image):
        angle = float(angle)
        try:
            figure = image.find_figure(name)
        except FigureNotFoundError as e:
            print(e)
            return
        figure.rotation = angle


    def _set_border_color(self, name, color, image):
        try:
            figure = image.find_figure(name)
        except FigureNotFoundError as e:
            print(e)
            return
        if color not in self.colors:
            raise ColorNotFoundError('Invalid color')
        figure.border_color = color

    def _set_background_color(self, name, color, image):
        try:
            figure = image.find_figure(name)
        except FigureNotFoundError as e:
            print(e)
            return
        if color not in self.colors:
            raise ColorNotFoundError('Invalid color')
        figure.background_color = color

    def help(self, *args):
        for key, value in self.available_commands.items():
            print(value.usage)

    def quit_f(self, *args):
        self.quit = True


class Command:
    def __init__(self, name, usage, run, number_of_run_args=0):
        self.name = name
        self.usage = usage
        self.number_of_run_args = number_of_run_args
        self.run = run
