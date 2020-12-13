file = './inputs/day9-input.txt'

def read_file(file: object) -> list:
    with open(file) as infile:
        return [ int(line.strip()) for line in infile ]


def calculate_sums(preambleStart: int, preambleEnd: int, numbers: list) -> list:
    sums = []
    numbers = numbers[preambleStart:preambleEnd]
    for number in numbers :
        index = 0
        while index < (preambleEnd - preambleStart):
            sums.append(number + numbers[index])
            index += 1
    return sums

def find_weakness(numbers: list) -> list:
        results = []
        preambleStart = 0
        preambleEnd = 25
        for number in numbers[preambleEnd:]:
            sums = calculate_sums(preambleStart, preambleEnd, numbers)
            if number in sums:
                pass
            elif number not in sums:
                return number
            preambleStart += 1
            preambleEnd += 1
        return results

def find_group_sum(keyNumber: int, batchSize: int, numbers) -> list:
    sums = []
    startIndex = 0
    while startIndex < len(numbers):
        batchNumbers = numbers[startIndex: (startIndex + batchSize)]
        sums.append(sum(batchNumbers))
        if keyNumber in sums:
            return batchNumbers
        else:
            startIndex += 1

if __name__ == "__main__":
        numbers = read_file(file)
        number = find_weakness(numbers)
        # part 1
        print(number)
        batchNumbers = []
        batchSize = 2
        while not batchNumbers:
            batchNumbers = find_group_sum(number, batchSize, numbers)
            batchSize += 1
        answer = min(batchNumbers) + max(batchNumbers)
        # part 2
        print(answer)
        


        
