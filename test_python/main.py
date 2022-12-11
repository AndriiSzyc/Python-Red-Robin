def numbers(a: int) -> str:  # sintax - what return function return (string)
    return {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four"}.get(
        a, "Unexpected argument"
    )

class Taras:
    def __init__(self, age, sex):
        self.age = age
        self.sex = sex

    def question(self):
        return 'command execution Make show'