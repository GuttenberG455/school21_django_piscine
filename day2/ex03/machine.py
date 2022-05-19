
import random
import beverages


class CoffeeMachine:

    class EmptyCup(beverages.HotBeverage):
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self) -> None:
            super().__init__("This coffee machine has to be repaired.")

    def __init__(self) -> None:
        self.usages_left = 10

    def repair(self) -> None:
        self.usages_left = 10

    def serve(self, beverage):
        if self.usages_left <= 0:
            raise CoffeeMachine.BrokenMachineException
        self.usages_left -= 1
        if random.random() > 0.8:
            return CoffeeMachine.EmptyCup()
        return beverage()


if __name__ == '__main__':
    machine = CoffeeMachine()
    for _ in range(5):
        try:
            print(machine.serve(beverages.Coffee))
            print(machine.serve(beverages.Tea))
            print(machine.serve(beverages.Chocolate))
        except Exception as e:
            print(e)
            machine.repair()
