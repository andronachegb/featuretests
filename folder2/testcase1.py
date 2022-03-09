from classes import class1
from params import params1

var1 = 4
test = class1.Test(var1)

print(f"{var1} {test.is_odd()} and {var1}! is {test.factorial()}.")
print(f"Host is {params1.mainParameters['mainParameters'][0]['host']}.")


if __name__ == '__main__':
    pass