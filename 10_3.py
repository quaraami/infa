def make_multiplier(multiplier):
    def multiply(number):
        return multiplier * number
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # Выведет 10
print(triple(5))  # Выведет 15