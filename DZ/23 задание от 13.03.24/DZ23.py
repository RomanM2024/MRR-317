class Person:
    def __init__(self, name: str, old: float) -> None:
        self.__name = name
        self.__old = old

    @staticmethod
    def __check_value(value, types) -> bool:
        return isinstance(value, types)

    @property
    def old(self) -> float:
        return self.__old

    @old.setter
    def old(self, value: float) -> None:
        if self.__check_value(value, (int, float)):
            self.__old = value

    @old.deleter
    def old(self) -> None:
        del self.__old

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if self.__check_value(value, str):
            self.__name = value

    @name.deleter
    def name(self) -> None:
        del self.__name


pers1 = Person("Irina", 26)
print(pers1.__dict__)
pers1.name = "Igor"
pers1.old = 31
print(pers1.name)
print(pers1.old)
pers1.old = 26
del pers1.name
print(pers1.__dict__)

