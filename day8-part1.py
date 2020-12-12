import re

file = 'inputs/day8-sample.txt'

def create_command_dict(command: str, position: int) -> dict:
    return {
        "command": command,
        "position": start
    }

# part 1
accumulator = 0
with open(file) as infile:
    program = infile.readlines()
    start = 0
    commandLog = []
    while start < len(program):
        command = program[start].strip()
        commandDict = create_command_dict(command, start)
        if commandDict in commandLog:
            print("INFINITE LOOP")
            print(f"Accumulator is {accumulator}")
            break
        else:
            commandLog.append(commandDict)
            if command[0:3] == 'nop':
                start += 1
            elif command[0:3] == 'acc':
                number = re.search(r"\+.+|-.+", command).group()
                accumulator += int(number)
                start += 1
            elif command[0:3] == 'jmp':
                number = re.search(r"\+.+|-.+", command).group()
                if int(number) >= 0:
                    start += int(number)
                elif int(number) < 0:
                    start = start + int(number)    