# Test Assignment 9.

import test


def test_assignment_9_folder_structure():
    test.check_assignment_folder_structure(
        "Assignment 9",
        r"activity[ _]?#?\d\.(class|fprg|cs|java|js|lua|py)|"
        "package-lock.json|test.csproj")


def test_assignment_9_required_flowgorithm_files():
    test.check_required_files("Assignment 9", "fprg", 1)


def test_assignment_9_required_source_code_files():
    test.check_required_files("Assignment 9", "(cs|java|js|lua|py)", 2)


def test_assignment_9_activity_1_flowgorithm_comments():
    test.check_source_code_comments("Assignment 9", "Activity 1", 1, "fprg")


def test_assignment_9_activity_1_flowgorithm_functions():
    test.check_flowgorithm_functions("Assignment 9", "Activity 1", 1, 1, 1)


def test_assignment_9_activity_1_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 9", "Activity 1")


def test_assignment_9_activity_1_source_code_comments():
    test.check_source_code_comments("Assignment 9", "Activity 1", 1)


def test_assignment_9_activity_1_source_code_functions():
    test.check_source_code_functions("Assignment 9", "Activity 1", 1, 1, 1)


def test_assignment_9_activity_1_source_code_formatting():
    test.check_source_code_formatting("Assignment 9", "Activity 1")


def test_assignment_9_activity_1_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 9", "Activity 1")


def test_assignment_9_activity_1_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 9", "Activity 1")


def test_assignment_9_activity_1_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 9", "Activity 1")


def test_assignment_9_activity_1_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 9", "Activity 1")


def test_assignment_9_activity_1_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 9", "Activity 1")


def test_assignment_9_activity_1_output_negative_termination():
    test.check_source_code_output(
        "Assignment 9",
        "Activity 1",
        "negative",
        "1\n2\n3\n-1\n",
        r"2.+?average|average.+?2",
        "average calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 9",
        "Activity 1",
        "negative",
        "1\n2\n-1\n",
        r"1\.5.+?average|average.+?1\.5",
        "average calculation output is incorrect.")


def test_assignment_9_activity_2_flowgorithm_comments():
    test.check_source_code_comments("Assignment 9", "Activity 2", 1, "fprg")


def test_assignment_9_activity_2_flowgorithm_functions():
    test.check_flowgorithm_functions("Assignment 9", "Activity 2", 1, 1, 1)


def test_assignment_9_activity_2_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 9", "Activity 2")


def test_assignment_9_activity_2_source_code_comments():
    test.check_source_code_comments("Assignment 9", "Activity 2", 1)


def test_assignment_9_activity_2_source_code_functions():
    test.check_source_code_functions("Assignment 9", "Activity 2", 1, 1, 1)


def test_assignment_9_activity_2_source_code_formatting():
    test.check_source_code_formatting("Assignment 9", "Activity 2")


def test_assignment_9_activity_2_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 9", "Activity 2")


def test_assignment_9_activity_2_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 9", "Activity 2")


def test_assignment_9_activity_2_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 9", "Activity 2")


def test_assignment_9_activity_2_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 9", "Activity 2")


def test_assignment_9_activity_2_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 9", "Activity 2")


def test_assignment_9_activity_2_output():
    test.check_source_code_output(
        "Assignment 9",
        "Activity 2",
        "",
        "h\ne\n",
        r"75",
        "higher guess is incorrect.")

    test.check_source_code_output(
        "Assignment 9",
        "Activity 2",
        "",
        "h\ne\n",
        r"2.+?guess|guess.+?2",
        "number of guesses output or label is missing or incorrect."
            "Expected 2 guesses.")

    test.check_source_code_output(
        "Assignment 9",
        "Activity 2",
        "",
        "l\ne\n",
        r"25",
        "lower guess is incorrect.")

    test.check_source_code_output(
        "Assignment 9",
        "Activity 2",
        "",
        "l\ne\n",
        r"2.+?guess|guess.+?2",
        "number of guesses output or label is missing or incorrect."
            "Expected 2 guesses.")


def test_assignment_9_activity_3_flowgorithm_comments():
    test.check_source_code_comments("Assignment 9", "Activity 3", 1, "fprg")


def test_assignment_9_activity_3_flowgorithm_functions():
    test.check_flowgorithm_functions("Assignment 9", "Activity 3", 1, 1, 1)


def test_assignment_9_activity_3_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 9", "Activity 3")


def test_assignment_9_activity_3_source_code_comments():
    test.check_source_code_comments("Assignment 9", "Activity 3", 1)


def test_assignment_9_activity_3_source_code_functions():
    test.check_source_code_functions("Assignment 9", "Activity 3", 1, 1, 1)


def test_assignment_9_activity_3_source_code_formatting():
    test.check_source_code_formatting("Assignment 9", "Activity 3")


def test_assignment_9_activity_3_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 9", "Activity 3")


def test_assignment_9_activity_3_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 9", "Activity 3")


def test_assignment_9_activity_3_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 9", "Activity 3")


def test_assignment_9_activity_3_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 9", "Activity 3")


def test_assignment_9_activity_3_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 9", "Activity 3")


def test_assignment_9_activity_4_flowgorithm_comments():
    test.check_source_code_comments("Assignment 9", "Activity 4", 1, "fprg")


def test_assignment_9_activity_4_flowgorithm_functions():
    test.check_flowgorithm_functions("Assignment 9", "Activity 4", 1, 1, 1)


def test_assignment_9_activity_4_flowgorithm_has_matching_source_code_file():
    test.check_flowgorithm_has_matching_source_code_file(
        "Assignment 9", "Activity 4")


def test_assignment_9_activity_4_source_code_comments():
    test.check_source_code_comments("Assignment 9", "Activity 4", 1)


def test_assignment_9_activity_4_source_code_functions():
    test.check_source_code_functions("Assignment 9", "Activity 4", 1, 1, 1)


def test_assignment_9_activity_4_source_code_formatting():
    test.check_source_code_formatting("Assignment 9", "Activity 4")


def test_assignment_9_activity_4_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 9", "Activity 4")


def test_assignment_9_activity_4_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 9", "Activity 4")


def test_assignment_9_activity_4_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 9", "Activity 4")


def test_assignment_9_activity_4_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 9", "Activity 4")


def test_assignment_9_activity_4_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 9", "Activity 4")
