from jezyki_biblioteki_analizy_danych.zad5.commands import Commands
from jezyki_biblioteki_analizy_danych.zad5.my_exceptions import *
import re


class Image2D:
    def __init__(self):
        self.figures = []

    def find_figure(self, name):
        for figure in self.figures: # nie lepszy byłby słownik?
            if figure.name == name:
                return figure
        raise FigureNotFoundError("Invalid name of figure")


def get_command(commands):
    command_input = re.split("\s{1,}", input().strip()) # zwykły split na stringu zrobi to samo
    command_input = [re.compile(r"\(|\)|,").sub("", m) for m in command_input]
    if command_input[0] in commands.available_commands:
        return command_input
    else:
        raise CommandNotFoundError("Invalid command, please enter 'help' for more information")


def main():
    commands = Commands()
    image = Image2D()
    while not commands.quit:
        print('Type command:')
        try:
            command_input = get_command(commands)
        except CommandNotFoundError as e:
            print(e)
            continue
        command = command_input[0]
        command = commands.available_commands[command]
        # print(command_input)
        if callable(command.run):
            if len(command_input) - 1 != command.number_of_run_args:
                print(f"Command {command.name} takes {command.number_of_run_args} arguments")
            else:
                try:
                    command.run(*command_input[1:], image)
                except FigureNotFoundError as e:    # except (Type1, Type2) as e
                    print(e)
                except ColorNotFoundError as e:
                    print(e)
                except InvalidNameError as e:
                    print(e)
                except InvalidArgumentError as e:
                    print(e)
    for figure in image.figures:
        print(str(figure))


if __name__ == "__main__":
    main()
