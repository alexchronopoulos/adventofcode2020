def parse_input(line: str) -> dict:
    return {
            "min": int(line.split("-")[0]),
            "max": int(line.split("-")[1][0:2]),
            "letter": line.split(" ")[1][0],
            "pw": line.split(":")[1].strip()
        }

def count_letters(pw: str) -> dict:
    output = {}
    for letter in pw:
        if letter in output.keys():
            output[letter] = output[letter] + 1
        else:
            output.setdefault(letter, 1)
    return output

def check_compliance_by_count(letter_count: dict, rule: dict) -> bool:
    if rule["letter"] in letter_count and \
        letterCount[rule["letter"]] in range(rule["min"], (rule["max"] + 1)):
        return True
    else:
        return False

def check_compliance_by_position(rule: dict) -> bool:
    password = ''.join(('0',rule["pw"])) 
    letterKey = rule["letter"]
    position1 = rule["min"]
    position2 = rule["max"]
    
    if letterKey in password:

        if len(password) <= position2:
            if letterKey == password[position1]:
                return True
            else:
                return False

        elif len(password) >= position2:
            if letterKey in password[position1] and \
                letterKey in password[position2]:
                return False

            elif letterKey not in password[position1] and \
                letterKey in password[position2]:
                return True

            elif letterKey in password[position1] and \
                letterKey not in password[position2]:
                return True
            
            elif position1 == position2 and \
                letterKey in password[position1]:
                return True

            elif letterKey != password[position1] and \
                letterKey != password[position2]:
                return False

    elif letterKey  not in password:
        return False

if __name__ == "__main__":
    with open("./day2-input.txt") as infile:
        compliantPWsByCount = []
        compliantPWsByPosition = []
        for line in infile:
            pw = parse_input(line)
            letterCount = count_letters(pw["pw"])
            compliantPWsByCount.append(check_compliance_by_count(letterCount, pw))
            compliantPWsByPosition.append(check_compliance_by_position(pw))
            print("")
    print(f"Compliant passwords by count: {compliantPWsByCount.count(True)}")
    print(f"Non-compliant passwords by count: {compliantPWsByCount.count(False)}")
    print("\n")
    print(f"Compliant passwords by position: {compliantPWsByPosition.count(True)}")
    print(f"Non-compliant passwords by position: {compliantPWsByPosition.count(False)}")
    print(f"Unmatched passwords by position: {compliantPWsByPosition.count(None)}")

