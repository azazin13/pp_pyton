import doctest

class Human:
    def __init__(self, name: str, age: int):
        """
        Создание и подготовка к работе объекта "Человек"

        :param name: Имя человека
        :param age: Возраст человека

        Пример:
        >>> human1 = Human('Nikita', 48)
        """
        if not isinstance(name, str):
            raise TypeError("Имя человека должно быть типа str")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст человека должен быть типа int")
        if age < 0:
            raise ValueError("Возраст человека не может быть отрицательным числом")
        self.age = age

    def is_baby(self) -> bool:
        """
        Функция, которая проверяет является ли человек ребёнком

        :return: Является ли человек ребёнком

        Примеры:
        >>> human2 = Human("Anya", 3)
        >>> human2.is_baby()
        """
        ...

    def getting_older(self, adding_years: int) -> None:
        """
        Функция, которая добавляет к возрасту человека некоторое колличество лет
        :param adding_years: Добавляемый возраст

        Примеры:
        >>> human3 = Human("Boris", 14)
        >>> human3.getting_older(2)
        """
        if not isinstance(adding_years, int):
            raise TypeError("Добавляемый возраст должен быть типа int")
        if adding_years < 0:
            raise ValueError("Добавляемый возраст должен быть положительным числом")
        ...

    def rename(self, new_name: str) -> None:
        """
        Функция, которая переименовывает человека
        :param new_name: Новое имя

        Примеры:
        >>> human4 = Human("Sasha", 12)
        >>> human4.rename("Sanya")
        """
        if not isinstance(new_name, str):
            raise TypeError("Имя должно быть типа str")
        ...


class Hat:
    def __init__(self, cost: int, owner: str):
        """
        Создание и подготовка к работе объекта "Шляпа"

        :param cost: Стоимость шляпы
        :param owner: Имя хозяина шляпы

        Пример:
        >>> hat1 = Hat(2200, 'Nikita')
        """
        if not isinstance(cost, int):
            raise TypeError("Стоимость шляпы должна быть типа int")
        if cost < 0:
            raise ValueError("Стоимость шляпы не может быть отрицательным числом")
        self.cost = cost
        if not isinstance(owner, str):
            raise TypeError("Имя хозяина шляпы должно быть типа str")
        self.owner = owner


    def change_owner(self, new_owner: str) -> None:
        """
        Функция, которая изменяет хозяина шляпы

        :param new_owner: Имя нового хозяина

        Примеры:
        >>> hat2 = Hat(1500, "Anya")
        >>> hat2.change_owner("Nikita")
        """
        if not isinstance(new_owner, str):
            raise TypeError("Имя нового хозяина шляпы должно быть типа str")
        ...

    def change_cost(self, new_cost: int) -> None:
        """
        Функция, которая изменяет стоимость шляпы
        :param new_cost: Новая стоимость

        Примеры:
        >>> hat3 = Hat(300, "Boris")
        >>> hat3.change_cost(500)
        """
        if not isinstance(new_cost, int):
            raise TypeError("Новая стоимость должна быть типа int")
        if new_cost < 0:
            raise ValueError("Новая стоимость должна быть положительным числом")
        ...



class Exam:
    def __init__(self, subject: str, hours: int, cards_to_learn: int):
        """
        Создание и подготовка к работе объекта "Экзамен"

        :param : subject: Предмет
        :param : hours: Осталось часов на подготовку
        :param : cards_to_learn: Осталось выучить билетов

        Пример:
        >>> exam1 = Exam("Physic", 72, 60)
        """
        if not isinstance(subject, str):
            raise TypeError("Название предмета должно быть типа str")
        self.subject = subject
        if not (isinstance(hours, int) or isinstance(cards_to_learn, int)):
            raise TypeError("Часы и количество билетов должны быть типа int")
        if hours < 0 or cards_to_learn < 0:
            raise ValueError("Часы и количество билетов не могут быть отрицательным числом")
        self.hours = hours
        self.cards_to_learn = cards_to_learn

    def time_left(self, hours_passed: int) -> None:
        """
        Функция, которая вычисляет сколько осталось времени на подготовку

        :param hours_passed: Сколько прошло часов

        Примеры:
        >>> exam2 = Exam("Math", 48, 30)
        >>> exam2.time_left(3)
        """
        if not isinstance(hours_passed, int):
            raise TypeError("Количество прошедших часов должно быть типа int")
        ...

    def cards_left(self, cards_learned: int) -> None:
        """
        Функция, которая вычисляет сколько осталось выучить билетов
        :param cards_learned: Выучено билетов

        Примеры:
        >>> exam3 = Exam("English", 12, 50)
        >>> exam3.cards_left(28)
        """
        if not isinstance(cards_learned, int):
            raise TypeError("Количество билетов должно быть типа int")
        if cards_learned < 0:
            raise ValueError("Количество билетов должно быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
