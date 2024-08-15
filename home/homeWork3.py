class Bank:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    def moneyX(self):
        try:
            amount = float(input("Сколько денег хотите добавить? "))
            if amount > 0:
                self._balance += amount
                print(f"Ваш новый баланс: {self._balance}")
            else:
                print("Сумма должна быть положительной.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    def _kill(self):
        self._balance = 0
        print("Ваш счет был обнулен.")

    def __jackpot(self):
        self._balance *= 10
        print(f"Вы выиграли джекпот! Ваш новый баланс: {self._balance}")

    def _merge_balance(self, another_account):
        if isinstance(another_account, Bank):
            self._balance += another_account._balance
            another_account._balance = 0
            print(f"Баланс объединен. Ваш новый баланс: {self._balance}")
        else:
            print("Ошибка: Объект не является экземпляром класса Bank.")

# Пример использования
if __name__ == "__main__":
    account1 = Bank("Иван", 1000)
    account2 = Bank("Анна", 500)

    account1.moneyX()  # Добавление денег на счет
    account1._kill()  # Обнуление счета
    account1._merge_balance(account2)  # Объединение балансов
    account1._Bank__jackpot()  # Выигрыш джекпота
