import json

values_file = r'C:\Users\Bartin\Desktop\Proba\test_rabota\task3\values.json'
tests_file = r'C:\Users\Bartin\Desktop\Proba\test_rabota\task3\tests.json'
report_file = r'C:\Users\Bartin\Desktop\Proba\test_rabota\task3\report.json'

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def fill_values(test_structure, values_dict):
    if 'id' in test_structure and test_structure['id'] in values_dict:
        test_structure['value'] = values_dict[test_structure['id']]

    if 'values' in test_structure:
        for sub_test in test_structure['values']:
            fill_values(sub_test, values_dict)

def main():

    values_data = load_json(values_file)
    tests_data = load_json(tests_file)


    values_dict = {item['id']: item['value'] for item in values_data['values']}


    for test in tests_data['tests']:
        fill_values(test, values_dict)

    save_json(tests_data, report_file)

if __name__ == "__main__":
    main()
