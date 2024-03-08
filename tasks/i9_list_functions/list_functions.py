from dataclasses import dataclass
from typing import List

__all__ = ["MyList"]


@dataclass
class MyList:
    __main_list = []
    __available_commands = [
        "insert",
        "print",
        "remove",
        "append",
        "sort",
        "pop",
        "reverse",
    ]
    __commands_that_require_no_arguments = ["print", "sort", "pop", "reverse"]

    @staticmethod
    def _checking_available_command(func):
        def wrapper(self, *args, **kwargs):
            command = args[0]
            if command not in self.__available_commands:
                raise ValueError(f"Invalid command: {command}")
            else:
                return func(self, *args)

        return wrapper

    @staticmethod
    def _checking_the_number_of_arguments(func):

        def wrapper(self, *args):
            command = args[0]
            if command in self.__commands_that_require_no_arguments and len(args) > 1:
                raise ValueError(f"Command '{command}' does not accept arguments")
            elif command == "insert" and len(args) != 3:
                raise ValueError(f"Command '{command}' requires two arguments")
            elif (
                command not in self.__commands_that_require_no_arguments
                and command != "insert"
                and len(args) != 2
            ):
                raise ValueError(f"Command '{command}' requires one argument")
            return func(self, *args)

        return wrapper

    @staticmethod
    def _checking_command_params_are_int(func):
        def wrapper(self, *args):
            command = args[0]
            try:
                first_param = args[1]

                if not isinstance(first_param, int):
                    raise ValueError(f"{command} first param must be an integer")
            except:
                pass
            try:
                second_param = args[2]
                if not isinstance(second_param, int):
                    raise ValueError(f"'{command}' second param must be an integer")
            except:
                pass
            return func(self, *args)

        return wrapper

    def _append_element(self, element) -> None:
        self.__main_list.append(element)

    def _remove_element(self, element) -> None:
        self.__main_list.remove(element)

    def _insert_element(self, position, element) -> None:
        self.__main_list.insert(position, element)

    def _sort__main_list(self) -> None:
        self.__main_list.sort()

    def _pop_elem(self) -> None:
        self.__main_list.pop()

    def _reverse__main_list(self) -> None:
        self.__main_list.reverse()

    def _print(self) -> List[int]:
        return self.__main_list

    @_checking_available_command
    @_checking_the_number_of_arguments
    @_checking_command_params_are_int
    def do_function(self, *args) -> List[int] | None:
        command = args[0]
        param_1 = (
            args[1]
            if command not in self.__commands_that_require_no_arguments
            else None
        )

        match command:
            case "append":
                self._append_element(param_1)
            case "remove":
                self._remove_element(param_1)
            case "insert":
                param_2 = args[2]
                self._insert_element(param_1, param_2)
            case "sort":
                self._sort__main_list()
            case "pop":
                self._pop_elem()
            case "reverse":
                self._reverse__main_list()
            case "print":
                return self._print()
