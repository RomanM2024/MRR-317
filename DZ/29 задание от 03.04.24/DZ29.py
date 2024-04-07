class IntegerCoordinate:

    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, instance: 'Point3D', owner: type) -> int:
        return instance.__dict__[self.name]

    def __set__(self, instance: 'Point3D', value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Значение координаты должно быть целым числом")
        instance.__dict__[self.name] = value


class Point3D:

    def __init__(self, x: int, y: int, z: int) -> None:
        self._x: int = IntegerCoordinate('_x')
        self._y: int = IntegerCoordinate('_y')
        self._z: int = IntegerCoordinate('_z')

        self._x = x
        self._y = y
        self._z = z

    def __repr__(self) -> str:
        return f"{{'_x': {self._x}, '_y': {self._y}, '_z': {self._z}}}"


point = Point3D(1, 2, 3)
print(point)
