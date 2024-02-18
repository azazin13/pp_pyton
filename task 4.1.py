if __name__ == "__main__":
    class Phone:
        def __init__(self, number: int, owner: str):
            """
            Конструктор базового класса телефон.

            :param number: номер телефона
            :param owner: владелец телефона
            """

            if not isinstance(number, int):
                raise TypeError("Номер должен быть типа int")
            if number < 0:
                raise ValueError("Номер не может быть отрицательным числом")
            self._number = number  # номер телефона нельзя изменять

            if not isinstance(owner, str):
                raise TypeError("Имя владельца должно быть типа str")
            self._owner = owner  # владельца нельзя менять

        @property
        def number(self):
            return self._number

        @property
        def owner(self):
            return self._owner

        def __str__(self) -> str:
           return f"Номер: {self.number}, Владелец: {self.owner}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(number={self.number!r}, owner={self.owner!r})"

        def call(self) -> None:
            """
            Звонит на данный номер.
            """
            ...

        def add_contact(self) -> None:
            """
            Добавляет номер и владельца в телефонную книгу
            """
            ...


    class MobilePhone(Phone):
        def __init__(self, number: int, owner: str, operator: list):
            """
            Конструктор мобильного телефона.

            :param number: номер телефона
            :param owner: владелец телефона
            :param operator: оператор связи
            """
            super().__init__(number, owner)
            self.operator = operator

            @property
            def operator(self):
                return self._operator

            @operator.setter
            def operator(self, operator):
                if not isinstance(operator, list):
                    raise TypeError("Имя оператора связи должно быть типа list")
                self._operator = operator

        #Наследуем метод __str__ тк считаем, что пользователю не нужно знать оператора связи
        #Перегружаем метод __repr__ для грамотной работы конструктора при подставлении кода
        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(number={self.number!r}, owner={self.owner!r}, operator={self.operator})"

        #Наследуем метод add_contact, перегружаем метод call
        def call(self) -> None:
            """
            Звонит на данный номер. Даёт выбрать оператора связи из списка возможных
            (Перегружаем тк теперь проверяется атрибут дочернего класса)
            """
            ...



    class HomePhone(Phone):
        def __init__(self, number: str, owner: str, address: str):
            """
            Конструктор домашнего телефона.

            :param number: номер телефона
            :param owner: владелец телефона
            :param address: адрес
            """
            super().__init__(number, owner)
            self.address = address

            @property
            def adress(self):
                return self._adress

            @adress.setter
            def operator(self, adress):
                if not isinstance(adress, str):
                    raise TypeError("Адресс должен быть типа str")
                self._adress = adress

            # Наследуем метод __str__ тк считаем, что пользователю не нужно знать адрес
            # Перегружаем метод __repr__ для грамотной работы конструктора при подставлении кода

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(number={self.number!r}, owner={self.owner!r}, adress={self.adress!r})"

        # Наследуем метод call, перегружаем метод add_contact

        def add_contact(self) -> None:
            """
            Добавляет номер, владельца и его адрес в телефонную книгу (перегружаем тк
            теперь добавляется ещё один атрибут)
            """
            ...
