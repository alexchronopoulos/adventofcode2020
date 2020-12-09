def parse_code(code: str, maxNum: int) -> range:
    totalRange = range(0, maxNum)
    for letter in code:
        half = abs(int((totalRange.stop - totalRange.start) / 2))
        lowerHalf =  range(totalRange.start, totalRange.start + half)
        upperHalf = range(totalRange.start + half, totalRange.stop)
        if letter == 'F' or letter == 'L':
            totalRange = lowerHalf
        elif letter == 'B' or letter == 'R':
            totalRange = upperHalf
    return totalRange

def choose_number(letter: str, options: range) -> int:
    if letter == 'F' or letter == 'L':
        return min(options)
    elif letter == 'B' or letter == 'R':
        return max(options)

def get_seat_id(row: int, multiplier: int, column: int) -> int:
    return row * multiplier + column

def find_missing_seat(seatIds: list) -> int:
    index = 1
    for seatId in seatIds[1:]:
        previousSeat = seatIds[(index - 1)]
        if (seatId - 1) != previousSeat:
            return seatId
        else:
            index += 1


with open("./inputs/day5-input.txt") as infile:
    seatIds = []
    for line in infile:
        line = line.strip()
        rowOptions = parse_code(line[0:6], 128)
        rowNumber = choose_number(line[6], rowOptions)
        columnOptions = parse_code(line[7:9], 8)
        columnNumber = choose_number(line[9], columnOptions)
        seatId = get_seat_id(rowNumber, 8, columnNumber)
        seatIds.append(seatId)

    print(f"Max seat ID is {max(seatIds)}") 
    your_seat = find_missing_seat(sorted(seatIds))
    print(f"Your seat is {your_seat - 1}")           