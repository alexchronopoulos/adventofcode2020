def read_input(filename: str) -> list:
    infile = open(filename)
    numbers = []
    for line in infile:
        numbers.append(int(line))
    return numbers

def add_numbers(number: int, numbers: list) -> list:
    totals = []
    for n in numbers:
        totals.append(number + n)
    return totals

def check_2020(numbers: list) -> int:
    output = []
    for number in numbers:
        totals = add_numbers(number, numbers)
        if 2020 in totals:
            output.append(number)
    return output

def multiply_numbers(number1: int, number2: int) -> int:
    product = number1 * number2
    return product

if __name__ == "__main__":
    numbers = read_input("./input.txt")
    answerNumbers = check_2020(numbers) 
    finalAnswer = multiply_numbers(answerNumbers[0],answerNumbers[1])
    print(finalAnswer)  