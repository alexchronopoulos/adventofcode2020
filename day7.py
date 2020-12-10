import re

file = './inputs/day7-input.txt'
myBag = 'shiny gold'
validBags = []

# part 1
def check_valid_bags(file: object, myBag: str) -> list:
    with open(file) as infile:
        for line in infile:
            line = line.strip()
            bag = re.match(r"(\w+\s\w+)\sbags\s", line).groups()[0]
            otherBags = re.search("bags.+", line).group()
            if myBag in otherBags:
                validBags.append(bag)
                check_valid_bags(file, bag)

check_valid_bags(file, myBag)
print(f"Total valid bags is {len(set(validBags))}")

# part 2
total = []
def check_number_of_bags(file:object, myBag: str) -> int:
    with open(file) as infile:
            for line in infile:
                line = line.strip()
                bag = re.match(r"(\w+\s\w+)\sbags\s", line).groups()[0]
                if bag == myBag:
                    otherBags = re.findall(r"(\d) (\w+\s\w+)", line)
                    for number, bag in otherBags:
                        total.append(int(number))
                        recursion = 0
                        while recursion < int(number):
                            check_number_of_bags(file, bag)
                            recursion += 1                        

check_number_of_bags(file, myBag)
print(f"Total number of bags is {sum(total)}")
