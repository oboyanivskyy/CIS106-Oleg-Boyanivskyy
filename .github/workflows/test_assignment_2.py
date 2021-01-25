# Test Assignment 2.

import test


def test_assignment_2_folder_structure():
    test.check_assignment_folder_structure(
        "Assignment 2",
        r"activity( *|_)#?1\.(fprg|txt|cs|java|js|py)|package-lock.json")


def test_assignment_2_required_flowgorithm_files():
    test.check_required_files("Assignment 2", "fprg", 1)


def test_assignment_2_required_pseudocode_files():
    test.check_required_files("Assignment 2", "txt", 1)


def test_assignment_2_required_source_code_files():
    test.check_required_files("Assignment 2", "(cs|java|js|py)", 1)


def test_assignment_2_activity_1_flowgorithm_comments():
    test.check_source_code_comments("Assignment 2", "Activity 1", 1, "fprg")


def test_assignment_2_activity_1_flowgorithm_output():
    test.check_flowgorithm_output("Assignment 2", "Activity 1", 1)


def test_assignment_2_activity_1_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 2", "Activity 1")


def test_assignment_2_activity_1_pseudocode_comments():
    test.check_source_code_comments("Assignment 2", "Activity 1", 1, "txt")


def test_assignment_2_activity_1_pseudocode_output():
    test.check_pseudocode_output("Assignment 2", "Activity 1", 1)


def test_assignment_2_activity_1_source_code_comments():
    test.check_source_code_comments("Assignment 2", "Activity 1", 1)


def test_assignment_2_activity_1_source_code_output():
    test.check_source_code_output(
        "Assignment 2",
        "Activity 1",
        "",
        "\n",
        "hello.+?$",
        "Output does not match requirements.")


def test_assignment_2_git_log():
    test.check_git_log(
        "Assignment 2",
        "hello.+?world",
        "Git log is missing required \"Hello world!\" text. "
            "You must commit Activity 1 changes before working on "
            "Activity 2.")
