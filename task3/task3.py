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

def generate_report(tests_file, report_file, id_dict):
    with open(tests_file, "r") as tests, open(report_file, "w") as report:
        for line in tests:
            printline = line
            if line.find('"id"') != -1:
                cur_id = int(line.split(": ")[1][:-2])
            if line.find('"value"') != -1:
                value = id_dict[cur_id]
                printline = line.replace('""', '"' + value + '"')
            report.writelines(printline)

if __name__ == '__main__':
    values, tests, report = read_input()
    id_dict = create_id_dict(values)
    generate_report(tests, report, id_dict)
