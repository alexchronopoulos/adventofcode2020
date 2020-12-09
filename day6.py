# part 1
with open('./inputs/day6-input.txt') as infile:
    total = 0
    answers = []
    for line in infile:
        if line == '\n':
            total += len(set(answers))
            answers = []
        else:
            line = line.strip()
            for letter in line:
                answers.append(letter)
    print(f"Total is {total}")

# part 2
with open('./inputs/day6-input.txt') as infile:
    total = 0
    answers = {}
    people = 0
    for line in infile:
        if line == '\n':
            for letter in list(answers.keys()):
                if answers[letter] == people:
                    total += 1
            answers = {}
            people = 0
        else:
            people += 1
            line = line.strip()
            for letter in line:
                if letter in list(answers.keys()):
                    answers[letter] += 1
                else:
                    answers.setdefault(letter, 1)
    print(f"Total is {total}")
            
        