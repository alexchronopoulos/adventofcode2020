import re

file = "./inputs/day8-input.txt"

def reset_program(file: object) -> list:
    with open(file) as infile:
        return infile.readlines()

def change_command(program: list, command: dict) -> str:
    if command["command"] == "nop":
        command["command"] = "jmp"
    elif command["command"] == "jmp":
        command["command"] = "nop"
    else:
        command = command
    program[command["position"]] = command
    return program

def create_command_dict(command: str, number: str, position: int) -> dict:
    return {
        "command": command,
        "number": number,
        "position": position
    }

def run_program(program: list) -> bool:
    accumulator = 0
    start = 0
    commandLog = []
    while start < len(program):
        command = program[start]
        if command in commandLog:
            print("INFINITE LOOP")
            return (False, accumulator)
        else:
            commandLog.append(command)
            if command["command"] == 'nop':
                start += 1
            elif command["command"] == 'acc':
                accumulator += command["number"]
                start += 1
            elif command["command"] == 'jmp':
                if command["number"] >= 0:
                    start += command["number"]
                elif command["number"] < 0:
                    start = start + command["number"]
    return (True, accumulator)

def command_log_to_program(programList: list) -> list:
    program = []
    for item in programList:
        program.append(item["command"] + " " + item["number"])
    return program

def command_list_to_program(program: list) -> list:
    commandLog = []
    index = 0
    while index < len(program):
        for command in program:
            fullCommand = command.strip()
            command = fullCommand[0:3]
            number = int(re.search(r"\+.+|-.+", fullCommand).group())
            commandDict = create_command_dict(command, number, index)
            commandLog.append(commandDict)
            index += 1
    return commandLog

if __name__ == "__main__":
    program = open(file).readlines()
    program = command_list_to_program(program)
    for command in program:
        newProgram = change_command(program, command)
        result = run_program(newProgram)
        if result[0] == True:
            print(f"Accumulator is {result}")
            break
        else:
            program = reset_program(file)
            program = command_list_to_program(program)
    