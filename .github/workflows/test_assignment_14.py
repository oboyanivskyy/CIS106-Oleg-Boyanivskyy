# Test Assignment 14.

import os
import test


def test_assignment_14_folder_structure():
    test.check_assignment_folder_structure(
        "Assignment 14",
        r"activity[ _]?#?\d\.(class|cs|java|js|lua|py)|"
        "package-lock.json|test.csproj|scores.txt|addresses.txt")


def test_assignment_14_required_source_code_files():
    test.check_required_files("Assignment 14", "(cs|java|js|lua|py)", 2)


def test_assignment_14_activity_1_source_code_comments():
    test.check_source_code_comments("Assignment 14", "Activity 1", 1)


def test_assignment_14_activity_1_source_code_functions():
    test.check_source_code_functions("Assignment 14", "Activity 1", 0, 1, 1)


def test_assignment_14_activity_1_source_code_formatting():
    test.check_source_code_formatting("Assignment 14", "Activity 1")


def test_assignment_14_activity_1_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 14", "Activity 1")


def test_assignment_14_activity_1_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 14", "Activity 1")


def test_assignment_14_activity_1_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 14", "Activity 1")


def test_assignment_14_activity_1_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 14", "Activity 1")


def test_assignment_14_activity_1_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 14", "Activity 1")


def test_assignment_14_activity_1_output():
    with open("scores.txt", "w") as file:
        file.write("Name,Score\n")
        file.write("Joe Besser,70\n")
        file.write("Curly Joe DeRita,0\n")
        file.write("Larry Fine,80\n")
        file.write("Curly Howard,65\n")
        file.write("Moe Howard,100\n")
        file.write("Shemp Howard,85")

    test.check_source_code_output(
        "Assignment 14",
        "Activity 1",
        "",
        "",
        r"100.+?(high|maximum)|(high|maximum).+?100",
        "high output value or label is missing or incorrect. "
            "Expected high: 2. "
            "Include output label on same line as result.")

    test.check_source_code_output(
        "Assignment 14",
        "Activity 1",
        "",
        "",
        r"0.+?(low|minimum)|(low|minimum).+?0",
        "low output value or label is missing or incorrect. "
            "Expected low: 1. "
            "Include output label on same line as result.")

    test.check_source_code_output(
        "Assignment 14",
        "Activity 1",
        "",
        "",
        r"(66|67).+?(average|mean)|(average|mean).+?(66|67)",
        "average calculation output is incorrect.")

    os.remove("scores.txt")


def test_assignment_14_activity_2_source_code_comments():
    test.check_source_code_comments("Assignment 14", "Activity 2", 1)


def test_assignment_14_activity_2_source_code_functions():
    test.check_source_code_functions("Assignment 14", "Activity 2", 0, 1, 1)


def test_assignment_14_activity_2_source_code_formatting():
    test.check_source_code_formatting("Assignment 14", "Activity 2")


def test_assignment_14_activity_2_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 14", "Activity 2")


def test_assignment_14_activity_2_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 14", "Activity 2")


def test_assignment_14_activity_2_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 14", "Activity 2")


def test_assignment_14_activity_2_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 14", "Activity 2")


def test_assignment_14_activity_2_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 14", "Activity 2")


def test_assignment_14_activity_2_output():
    with open("scores.txt", "w") as file:
        file.write("Name,Score\n")
        file.write("Joe Besser,70\n")
        file.write("Curly Joe DeRita,0\n")
        file.write("Larry Fine,80\n")
        file.write("Curly Howard,65\n")
        file.write("Moe Howard,100\n")
        file.write("Shemp Howard,85")

    test.check_source_code_output(
        "Assignment 14",
        "Activity 2",
        "",
        "",
        r"100.+?(high|maximum)|(high|maximum).+?100",
        "high output value or label is missing or incorrect. "
            "Expected high: 2. "
            "Include output label on same line as result.")

    test.check_source_code_output(
        "Assignment 14",
        "Activity 2",
        "",
        "",
        r"0.+?(low|minimum)|(low|minimum).+?0",
        "low output value or label is missing or incorrect. "
            "Expected low: 1. "
            "Include output label on same line as result.")

    test.check_source_code_output(
        "Assignment 14",
        "Activity 2",
        "",
        "",
        r"(66|67).+?(average|mean)|(average|mean).+?(66|67)",
        "average calculation output is incorrect.")

    if os.path.exists("scores.txt"):
        os.remove("scores.txt")


def test_assignment_14_activity_2_missing_file():
    if os.path.exists("scores.txt"):
        os.remove("scores.txt")

    test.check_source_code_output(
        "Assignment 14",
        "Activity 2",
        "",
        "Missing file",
        r"error|missing|does not exist|doesn't exist",
        "Error message is missing or incorrect. "
            "Expected 'File is missing'.")


def test_assignment_14_activity_2_empty_file():
    with open("scores.txt", "w") as file:
        file.write("")

    test.check_source_code_output(
        "Assignment 14",
        "Activity 2",
        "",
        "Empty file",
        r"error|missing|empty|bad|no",
        "Error message is missing or incorrect. "
            "Expected 'File is empty'.")

    if os.path.exists("scores.txt"):
        os.remove("scores.txt")


def test_assignment_14_activity_2_no_records():
    with open("scores.txt", "w") as file:
        file.write("Name,Score")

    test.check_source_code_output(
        "Assignment 14",
        "Activity 2",
        "",
        "No records",
        r"error|missing|empty|bad|no",
        "Error message is missing or incorrect. "
            "Expected 'File is empty' or 'No data'.")

    if os.path.exists("scores.txt"):
        os.remove("scores.txt")


def test_assignment_14_activity_2_missing_fields():
    with open("scores.txt", "w") as file:
        file.write("Name,Score\n")
        file.write("Joe Besser,70\n")
        file.write(",0\n")
        file.write("Larry Fine 80\n")
        file.write("Curly Howard,\n")
        file.write("Moe Howard,100\n")
        file.write("Shemp Howard,85")

    test.check_source_code_output(
        "Assignment 14",
        "Activity 2",
        "",
        "Missing fields",
        r"error|missing|empty|bad|no",
        "Error message is missing or incorrect. "
            "Expected 'Error: Missing or bad data'.")

    if os.path.exists("scores.txt"):
        os.remove("scores.txt")


def test_assignment_14_activity_2_bad_data():
    with open("scores.txt", "w") as file:
        file.write("Name,Score\n")
        file.write("Joe Besser,70\n")
        file.write("Curly Joe DeRita,x\n")
        file.write("Larry Fine,80\n")
        file.write("Curly Howard,65\n")
        file.write("Moe Howard,100\n")
        file.write("Shemp Howard,85")

    test.check_source_code_output(
        "Assignment 14",
        "Activity 2",
        "",
        "Bad data",
        r"missing|empty|bad|no",
        "Error message is missing or incorrect. "
            "Expected 'Error: Missing or bad data'.")

    if os.path.exists("scores.txt"):
        os.remove("scores.txt")


def test_assignment_14_activity_3_source_code_comments():
    test.check_source_code_comments("Assignment 14", "Activity 3", 1)


def test_assignment_14_activity_3_source_code_functions():
    test.check_source_code_functions("Assignment 14", "Activity 3", 1, 1, 1)


def test_assignment_14_activity_3_source_code_formatting():
    test.check_source_code_formatting("Assignment 14", "Activity 3")


def test_assignment_14_activity_3_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 14", "Activity 3")


def test_assignment_14_activity_3_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 14", "Activity 3")


def test_assignment_14_activity_3_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 14", "Activity 3")


def test_assignment_14_activity_3_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 14", "Activity 3")


def test_assignment_14_activity_3_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 14", "Activity 3")


def test_assignment_14_activity_3_input_labels():
    test.check_source_code_output(
        "Assignment 14",
        "Activity 3",
        "",
        "test\n",
        r"enter.+?(filename|file name)",
        "Input label(s) missing or incorrect. "
            "Expecting 'Enter file name'")


def test_assignment_14_activity_3_output():
    pass


def test_assignment_14_activity_4_source_code_comments():
    test.check_source_code_comments("Assignment 14", "Activity 4", 1)


def test_assignment_14_activity_4_source_code_functions():
    test.check_source_code_functions("Assignment 14", "Activity 4", 0, 1, 1)


def test_assignment_14_activity_4_source_code_formatting():
    test.check_source_code_formatting("Assignment 14", "Activity 4")


def test_assignment_14_activity_4_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 14", "Activity 4")


def test_assignment_14_activity_4_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 14", "Activity 4")


def test_assignment_14_activity_4_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 14", "Activity 4")


def test_assignment_14_activity_4_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 14", "Activity 4")


def test_assignment_14_activity_4_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 14", "Activity 4")


def test_assignment_14_activity_4_output():
    pass
