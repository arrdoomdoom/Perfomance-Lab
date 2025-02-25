import json

def read_input():
    line = input().split(' ')
    file1 = line[0]
    if len(line) == 3:
        file2 = line[1]
        file3 = line[2]
    else:
        file2 = input()
        file3 = input()
    
    return file1, file2, file3

def create_id_dict(values_file):
    id_dict = {}
    with open(values_file, "r") as file:
        data = json.load(file)
        for item in data["values"]:
            id_dict[item["id"]] = item["value"]
    
    return id_dict

def fill_report(report_file, tests):
    with open(report_file, "w") as file:
        json.dump(tests, file, indent=1)

def fill_tests(tests, id_dict):
    for test in tests:
        if "value" in test:
            test["value"] = id_dict[test["id"]]
        if "values" in test and test["values"]: 
            test["values"] = fill_tests(test["values"], id_dict)
            
    return tests


if __name__ == '__main__':
    values, tests, report = read_input()

    with open(tests, "r") as tests_file:
        test = json.load(tests_file)
        id_dict = create_id_dict(values)
        ready_tests = fill_tests(test["tests"], id_dict)
        fill_report(report, ready_tests)

