def numbers(a: int) -> str:  # sintax - what return function return (string)
    return {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four"}.get(
        a, "Unexpected argument"
    )
