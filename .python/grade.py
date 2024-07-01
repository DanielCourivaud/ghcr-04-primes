# generate_grade.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

import xml.etree.ElementTree as ET

def parse_junit_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    tests = 0
    failures = 0
    errors = 0
    skipped = 0
    for testsuite in root.findall('testsuite'):
        tests += int(testsuite.attrib.get('tests', 0))
        failures += int(testsuite.attrib.get('failures', 0))
        errors += int(testsuite.attrib.get('errors', 0))
        skipped += int(testsuite.attrib.get('skipped', 0))
    passed = tests - failures - errors - skipped
    return tests, passed, failures, errors, skipped

def generate_grade(tests, passed):
    grade = (passed / tests) if tests > 0 else 0
    return grade

if __name__ == "__main__":
    results_file = 'results.xml'  # Path to your JUnit XML file
    tests, passed, failures, errors, skipped = parse_junit_xml(results_file)
    grade = generate_grade(tests, passed)
    # print(f"Total Tests: {tests}")
    # print(f"Passed Tests: {passed}")
    # print(f"Failed Tests: {failures}")
    # print(f"Errors: {errors}")
    # print(f"Skipped: {skipped}")
    print(f"{grade:.2f}")