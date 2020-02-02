class Worker:
    def __init__(self, name, surname, position, __wage, __bonus):

        self.name = name
        self.surname = surname
        self.position = position
        self.wage = __wage
        self.bonus = __bonus
        self.income={"wage": __wage, "bonus": __bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя: {self.surname} {self.name}')

    def get_total_income(self):
        print(f"{self.position} {self.surname} получит {int(self.income.get('wage')) + int(self.income.get('bonus'))}")


first_worker = Position("Petr", "Ivanov", "carpenter", 1000, 500)
first_worker.get_full_name()
first_worker.get_total_income()
