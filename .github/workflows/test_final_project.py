# Test Final Project.

import os
import test
import urllib.request

def setup_module(module):
    url = "https://www.w3schools.com/xml/cd_catalog.xml"
    text = urllib.request.urlopen(url).read().decode()
    with open("cd_catalog.xml", "w") as file:
        file.write(text)


def teardown_module(module):
    files = [
        "cd_catalog.xml",
        "plant_catalog.xml",
        "simple.xml"
    ]

    for file in files:
        if os.path.exists(file):
            os.remove(file)


def test_final_project_folder_structure():
    test.check_assignment_folder_structure(
        "Final Project",
        r"final[ _]project\.(class|cs|java|js|lua|py)|"
        "package-lock.json|test.csproj")


def test_final_project_required_source_code_files():
    test.check_required_files("Final Project", "(cs|java|js|lua|py)", 1)


def test_final_project_source_code_comments():
    test.check_source_code_comments("Final Project", "Final Project", 1)


# def test_final_project_source_code_functions():
#     test.check_source_code_functions("Final Project", "Final Project", 0, 1, 1)


def test_final_project_source_code_formatting():
    test.check_source_code_formatting("Final Project", "Final Project")


def test_final_project_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Final Project", "Final Project")


def test_final_project_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Final Project", "Final Project")


def test_final_project_source_code_identifier_length():
    test.check_source_code_identifier_length("Final Project", "Final Project")


def test_final_project_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Final Project", "Final Project")


def test_final_project_output():
    url = "https://www.w3schools.com/xml/cd_catalog.xml"
    text = urllib.request.urlopen(url).read().decode()
    with open("cd_catalog.xml", "w") as file:
        file.write(text)

    test.check_source_code_output(
        "Final Project",
        "Final Project",
        "",
        "",
        r"Empire Burlesque - Bob Dylan - USA - \$?10.90 - 1985",
        "Expected first line to match:\n"
            "Empire Burlesque - Bob Dylan - USA - 10.90 - 1985"
    )

    test.check_source_code_output(
        "Final Project",
        "Final Project",
        "",
        "",
        r"26.+?9\.12",
        "Expected total line to contain:\n"
            "26 items - $9.12 average price"
    )

    if os.path.exists("cd_catalog.xml"):
        os.remove("cd_catalog.xml")


def test_final_project_missing_file():
    if os.path.exists("cd_catalog.xml"):
        os.remove("cd_catalog.xml")

    test.check_source_code_output(
        "Final Project",
        "Final Project",
        "",
        "Missing file",
        r"error|missing|does not exist|doesn't exist",
        "Error message is missing or incorrect. "
            "Expected 'File is missing'.")


def test_final_project_empty_file():
    with open("cd_catalog.xml", "w") as file:
        file.write("")

    test.check_source_code_output(
        "Final Project",
        "Final Project",
        "",
        "Empty file",
        r"error|missing|empty|bad|no",
        "Error message is missing or incorrect. "
            "Expected 'File is empty'.")

    if os.path.exists("cd_catalog.xml"):
        os.remove("cd_catalog.xml")


def test_final_project_no_records():
    with open("cd_catalog.xml", "w") as file:
        file.write("<?xml version=""1.0"" encoding=""UTF-8""?>")
        file.write("<CATALOG>")
        file.write("</CATALOG>")


    test.check_source_code_output(
        "Final Project",
        "Final Project",
        "",
        "No records",
        r"error|missing|empty|bad|no",
        "Error message is missing or incorrect. "
            "Expected 'File is empty' or 'No data'.")

    if os.path.exists("cd_catalog.xml"):
        os.remove("cd_catalog.xml")


def test_final_project_missing_fields():
    url = "https://www.w3schools.com/xml/cd_catalog.xml"
    text = urllib.request.urlopen(url).read().decode()
    text = text.replace("    <ARTIST>Bob Dylan</ARTIST>\r\n", "")
    with open("cd_catalog.xml", "w") as file:
        file.write(text)

    test.check_source_code_output(
        "Final Project",
        "Final Project",
        "",
        "Missing fields",
        r"error|missing|empty|bad|no",
        "Error message is missing or incorrect. "
            "Expected 'Error: Missing or bad data'.")

    if os.path.exists("cd_catalog.xml"):
        os.remove("cd_catalog.xml")


def test_final_project_bad_data():
    url = "https://www.w3schools.com/xml/cd_catalog.xml"
    text = urllib.request.urlopen(url).read().decode()
    text = text.replace("<PRICE>10.90</PRICE>", "<PRICE>x</PRICE>")
    with open("cd_catalog.xml", "w") as file:
        file.write(text)

    test.check_source_code_output(
        "Final Project",
        "Final Project",
        "",
        "Bad data",
        r"missing|empty|bad|no",
        "Error message is missing or incorrect. "
            "Expected 'Error: Missing or bad data'.")

    if os.path.exists("cd_catalog.xml"):
        os.remove("cd_catalog.xml")


def test_final_project_source_code_error_handling():
    test.check_file_contains(
        "Final Project",
        "Final Project",
        r"(cs|java|js)",
        "try",
        "include try/catch error handling for file processing.")

    test.check_file_contains(
        "Final Project",
        "Final Project",
        r"(cs|java|js)",
        "catch",
        "include try/catch error handling for file processing.")


def test_final_project_lua_error_handling():
    test.check_file_contains(
        "Final Project",
        "Final Project",
        "lua",
        "pcall",
        "include pcall error handling for file processing.")


def test_final_project_python_error_handling():
    test.check_file_contains(
        "Final Project",
        "Final Project",
        "py",
        "try",
        "include try/except error handling for file processing.")

    test.check_file_contains(
        "Final Project",
        "Final Project",
        "py",
        "except",
        "include try/except error handling for file processing.")
