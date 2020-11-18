class CoffeeMachine:
    command = None
    water_to_add = None
    milk_to_add = None
    beans_to_add = None
    cups_to_add = None

    water, milk, beans, cups = 400, 540, 120, 9
    money = 550

    def printer(self):
        print("The coffee machine has:")
        print("{} of water".format(self.water))
        print("{} 0f milk".format(self.milk))
        print("{} 0f coffee beans".format(self.beans))
        print("{} of disposable cups".format(self.cups))
        print("${} of money\n".format(self.money))

        self.command = None

    def buy(self, options):
        if options is None:
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 = cappuccino, back - to main menu')
            return

        elif options == 'back':
            self.command = None
            return
        else:
            options = int(options)
        if options == 1:
            if (self.water < 250) or (self.beans < 16) or (self.cups < 1):
                print('Sorry, not enough resources!\n')
            else:
                print('I have enough resources, making you a coffee!\n')
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4

        elif options == 2:
            if (self.water < 350) or (self.milk < 75) or (self.beans < 20) or (self.cups < 1):
                print('Sorry, not enough water!\n')
            else:
                print('I have enough resources, making you a coffee!\n')
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7

        elif options == 3:
            if (self.water < 200) or (self.milk < 100) or (self.beans < 12) or (self.cups < 1):
                print('Sorry, not enough resources!\n')
            else:
                print('I have enough resources, making you a coffee!\n')
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6

        self.command = None

    def fill(self, options):
        if options is None:
            print("Write how many ml of water do you want to add:")
            return

        elif self.water_to_add is None:
            self.water_to_add = int(options)
            print('Write how many ml of milk do you want to add:')
            return

        elif self.milk_to_add is None:
            self.milk_to_add = int(options)
            print('Write how many grams of coffee beans do you want to add:')
            return

        elif self.beans_to_add is None:
            self.beans_to_add = int(options)
            print('Write how many cups of coffee do you want to add:')
            return
        else:
            self.cups_to_add = int(options)

        self.water += self.water_to_add
        self.milk += self.milk_to_add
        self.beans += self.beans_to_add
        self.cups += self.cups_to_add

        self.command = None
        self.water_to_add = None
        self.milk_to_add = None
        self.cups_to_add = None
        self.beans_to_add = None

    def take(self):
        print("I gave you ${}\n".format(self.money))
        self.money = 0
        self.command = None

    def handle(self, options):
        if self.command is None:
            self.command = options
            options = None
        if self.command == 'buy':
            self.buy(options)

        elif self.command == 'fill':
            self.fill(options)

        elif self.command == 'take':
            self.take()

        elif self.command == 'remaining':
            self.printer()

        if self.command is None:
            self.get_command()

    def get_command(self):
        print('Write action (buy, fill, take, remaining, exit):')


def run():
    coffee_machine = CoffeeMachine()
    serve(coffee_machine)


def serve(machine, command=None):
    if command != 'exit':
        machine.handle(command)
        serve(machine, input().strip())


run()
