with open('./day3-input.txt') as infile:
    startPosition = 0
    trees = 0
    right = 1
    skip = False
    for line in infile:
        line = line.strip()
        print(line)
        if not skip:
            if startPosition >= len(line):
                line = line * 100

            terrain = line[startPosition]

            if terrain == '#':
                trees = trees + 1

            startPosition = startPosition + right
            skip = True
        else:
            skip = False
            

    print(trees)
        

