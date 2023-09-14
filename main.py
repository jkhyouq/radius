import math

class GeometryCalculator:
    @staticmethod
    def calculate_circle_area(radius):
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным.")
        return math.pi * radius ** 2

    @staticmethod
    def calculate_triangle_area(side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Длины сторон треугольника должны быть положительными.")

        # Проверка на прямоугольность треугольника
        is_right_triangle = GeometryCalculator.is_right_triangle(side_a, side_b, side_c)

        s = (side_a + side_b + side_c) / 2.0
        area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))

        return area

    @staticmethod
    def is_right_triangle(side_a, side_b, side_c):
        sides = [side_a, side_b, side_c]
        sides.sort()

        a_square = sides[0] ** 2
        b_square = sides[1] ** 2
        c_square = sides[2] ** 2

        return math.isclose(a_square + b_square, c_square, rel_tol=1e-9)

if __name__ == "__main__":
    # Пример использования библиотеки
    calculator = GeometryCalculator()

    circle_area = calculator.calculate_circle_area(5)
    print(f"Площадь круга с радиусом 5: {circle_area:.2f}")

    triangle_area = calculator.calculate_triangle_area(3, 4, 5)
    print(f"Площадь треугольника с сторонами 3, 4, 5: {triangle_area:.2f}")

    is_right = calculator.is_right_triangle(3, 4, 5)
    print(f"Треугольник с сторонами 3, 4, 5 является прямоугольным: {is_right}")
