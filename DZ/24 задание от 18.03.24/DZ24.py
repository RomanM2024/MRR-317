class AreaCalculator:
    triangle_count: int = 0
    rectangle_count: int = 0
    square_count: int = 0

    @staticmethod
    def calculate_triangle_area(a: float, b: float, c: float = None, method: str = 'основание_высота') -> float:
        AreaCalculator.triangle_count += 1
        if method == 'основание_высота':
            if c is not None:
                raise ValueError("Для метода 'основание_высота' не должно быть передано третье значение")
            return 0.5 * a * b
        elif method == 'Герон':
            if c is None:
                raise ValueError("Для метода 'Герон' должно быть передано три значения")
            semi_perimeter = (a + b + c) / 2
            return (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5
        else:
            raise ValueError("Неверный метод для вычисления площади треугольника")

    @staticmethod
    def calculate_rectangle_area(length: float, width: float) -> float:
        AreaCalculator.rectangle_count += 1
        return length * width

    @staticmethod
    def calculate_square_area(side: float) -> float:
        AreaCalculator.square_count += 1
        return side ** 2

    @staticmethod
    def get_total_count() -> int:
        return AreaCalculator.triangle_count + AreaCalculator.rectangle_count + AreaCalculator.square_count


triangle_area_heron = AreaCalculator.calculate_triangle_area(3, 4, 5, method='Герон')
print(f"Площадь треугольника по формуле Герона (3, 4, 5): {triangle_area_heron}")

triangle_area_base_height = AreaCalculator.calculate_triangle_area(6, 7, method='основание_высота')
print(f"Площадь треугольника через основание и высоту (6, 7): {triangle_area_base_height}")

square_area = AreaCalculator.calculate_square_area(7)
print(f"Площадь квадрата (7): {square_area}")

rectangle_area = AreaCalculator.calculate_rectangle_area(2, 6)
print(f"Площадь прямоугольника (2, 6): {rectangle_area}")

print("Количество подсчетов площади:", AreaCalculator.get_total_count())
