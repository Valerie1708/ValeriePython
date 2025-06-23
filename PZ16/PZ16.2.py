# 1. Создание базового класса "Работник" и его наследование для создания классов
# "Менеджер" и "Инженер". В классе "Работник" будут общие методы, такие как
# "работать" и "получать зарплату", а классы-наследники будут иметь свои
# уникальные методы и свойства, такие как "управлять командой" и "проектировать
# системы"
class Worker:
    name = ''

    def work(self):
        print(f'Сотрудник {self.name} работает')
    def receive_salary(self):
        print(f'Сотрудник {self.name} получает зарплату')

class Manager(Worker):

    def manage_a_team(self):
        print(f'Менеджер {self.name} управляет командой')

class Engineer(Worker):

    def design_systems(self):
        print(f'Инженер {self.name} проектирует системы')

manager = Manager()
manager.name = 'Егор'
manager.manage_a_team()
print(dir(manager))

engineer = Engineer()
engineer.name = 'Федор'
engineer.design_systems()
print(dir(engineer))