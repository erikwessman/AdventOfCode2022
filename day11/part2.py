import math

arr = []
with open('day11/input.txt', 'r') as f:
    arr = f.read().splitlines()

class Monkey():
    items = []
    operation_string = None
    divisibility = None
    throw_divisible = None
    throw_not_divisible = None
    total_inspections = 0

    def __init__(self):
        pass

    def inspect(self, modulo_factor):
        if len(self.items) == 0:
            return

        item = self.items.pop(0)
        item = self.perform_operation(item)
        item = self.apply_modulo_factor(item, modulo_factor)

        is_divisible = self.check_divisibility(item)
        throw_monkey = self.throw_divisible if is_divisible else self.throw_not_divisible

        self.total_inspections += 1
        return item, throw_monkey

    def perform_operation(self, item):
        op = self.operation_string[6:]
        op = op.replace('old', str(item))
        return eval(op)

    def apply_modulo_factor(self, item, modulo_factor):
        return item % modulo_factor

    def check_divisibility(self, item):
        return item % self.divisibility == 0

class Parser():
    def __init__(self):
        pass

    def parse_items(self, s):
        l,r = s.split(':')
        levels_strings = r.split(',')
        worry_levels = []
        for level in levels_strings:
            worry_levels.append(int(level.strip()))
        return worry_levels

    def parse_operation(self, s):
        s_list = s.split(':')
        return s_list.pop().strip()

    def parse_divisibility(self, s):
        s_list = s.split(' ')
        return int(s_list.pop())

    def parse_throw_true(self, s):
        s_list = s.split(' ')
        return int(s_list.pop())

    def parse_throw_false(self, s):
        s_list = s.split(' ')
        return int(s_list.pop())

parser = Parser()
monkeys = []

for i in range(0, len(arr), 7):
    line = arr[i]
    if line.startswith('Monkey'):
        instructions = arr[i+1:i+6]
        
        monkey = Monkey()
        monkey.items = parser.parse_items(instructions[0])
        monkey.operation_string = parser.parse_operation(instructions[1])
        monkey.divisibility = parser.parse_divisibility(instructions[2])
        monkey.throw_divisible = parser.parse_throw_true(instructions[3])
        monkey.throw_not_divisible = parser.parse_throw_false(instructions[4])
        monkeys.append(monkey)

modulo_factor = 1

for monkey in monkeys:
    modulo_factor *= monkey.divisibility

for i in range(10000):
    for monkey in monkeys:
        items = [x for x in monkey.items]
        for item in items:
            inspected_item, throw_monkey = monkey.inspect(modulo_factor)
            monkeys[throw_monkey].items.append(inspected_item)

monkeys.sort(key=lambda x: x.total_inspections, reverse=True)
print(monkeys[0].total_inspections * monkeys[1].total_inspections)