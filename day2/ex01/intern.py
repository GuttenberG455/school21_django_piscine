class Intern:

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def __init__(self, name='My name? I’m nobody, an intern, I have no name.'):
        self._name = name

    def __str__(self):
        return self._name

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return self.Coffee()


if __name__ == '__main__':
    boka = Intern()
    joka = Intern("Joka")
    print(boka)
    print(joka)
    coffee = boka.make_coffee()
    print(coffee)
    try:
        joka.work()
    except Exception as e:
        print(e)