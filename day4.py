import re

file = './day4-input.txt'

def check_byr(byr: str) -> bool:
    match = re.findall(r"\d\d\d\d", byr)
    if match and int(byr) in range(1920,2003):
        return True
    else:
        return False

def check_iyr(iyr: str) -> bool:
    match = re.findall(r"\d\d\d\d", iyr)
    if match and int(iyr) in range(2010,2021):
        return True
    else:
        return False

def check_eyr(eyr: str) -> bool:
    match = re.findall(r"\d\d\d\d", eyr)
    if match and int(eyr) in range(2020,2031):
        return True
    else:
        return False

def check_hgt(hgt: str) -> bool:
    match = re.match(r"(\d+)(cm|in)", hgt)
    if match:
        if match.group(2) == 'cm' and int(match.group(1)) in range(150,194):
            return True
        elif match.group(2) == 'in' and int(match.group(1)) in range(59,77):
            return True
        else:
            return False
    else:
        return False

def check_hcl(hcl: str) -> bool:
    match = re.findall(r"#[0-9|a-f]{6}", hcl)
    if match:
        return True
    else:
        return False

def check_ecl(ecl: str) -> bool:
    match = re.findall(r"[amb|blu|brn|gry|grn|hzl|oth]{1}", ecl)
    if match:
        return True
    else:
        return False

def check_pid(pid: str) -> bool:
    match = re.findall(r"\d{9}", pid)
    if match:
        return True
    else:
        return False

def check_passport(passportDict: dict) -> bool:
    if "cid" in passportDict.keys():
        passportDict.pop("cid")
    expected_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    actual_keys = list(passportDict.keys())
    if sorted(expected_keys) == sorted(actual_keys):
        byr_valid = check_byr(passportDict["byr"])
        iyr_valid = check_iyr(passportDict["iyr"])
        eyr_valid = check_eyr(passportDict["eyr"])
        hgt_valid = check_hgt(passportDict["hgt"])
        hcl_valid = check_hcl(passportDict["hcl"])
        ecl_valid = check_ecl(passportDict["ecl"])
        pid_valid = check_pid(passportDict["pid"])
        if byr_valid and iyr_valid and eyr_valid and hgt_valid and hcl_valid and ecl_valid and pid_valid:
            return True
        else:
            return False
    else:
        return False

with open(file) as infile:
    passports = []
    passportDict = {}
    for line in infile:
        if line.strip():
            line = line.strip()
            pairs = line.split(' ')
            for pair in pairs:
                passportDict.setdefault(pair.split(':')[0], pair.split(':')[1])
        else:
            print("SKIP")
            passports.append(passportDict)
            passportDict = {}

results = []
for passport in passports:
    results.append(check_passport(passport))

print(f"Valid passports: {results.count(True)}")
print(f"Invalid passports: {results.count(False)}")
            



            
            
            
    