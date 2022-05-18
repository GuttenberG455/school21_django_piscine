
import random
import beverages

class CoffeeMachine:

    class EmptyCup(beverages.HotBeverage):

        def __init__(self, price=0.9, name="empty cup"):
            beverages.HotBeverage.__init__(self, price, name)

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        raise Exception("This coffee machine has to be repaired.")

    def __init__(self):
        self.usages_left = 10

    def repair(self):
        self.usages_left = 10

    def serve(self, drink):
        if (self.usages_left <= 0):
            raise CoffeeMachine.BrokenMachineException
        self.usages_left -= 1
        if random.random() >= 0.1:
            return CoffeeMachine.EmptyCup()
        return drink()


if __name__ == '__main__':
    machine = CoffeeMachine()
    machine.serve(beverages.Coffee)