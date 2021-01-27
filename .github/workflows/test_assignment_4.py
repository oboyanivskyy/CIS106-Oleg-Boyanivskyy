# Test Assignment 4.

import test


def test_assignment_4_folder_structure():
    test.check_assignment_folder_structure(
        "Assignment 4",
        r"activity( *|_)#?\d\.(fprg|cs|java|js|lua|py)|"
        "package-lock.json|test.csproj")


def test_assignment_4_required_source_code_files():
    test.check_required_files("Assignment 4", "(cs|java|js|lua|py)", 2)


def test_assignment_4_activity_1_source_code_comments():
    test.check_source_code_comments("Assignment 4", "Activity 1", 1)


def test_assignment_4_activity_1_source_code_inputs():
    test.check_source_code_inputs("Assignment 4", "Activity 1", 2)


def test_assignment_4_activity_1_source_code_processing():
    test.check_source_code_processing("Assignment 4", "Activity 1", 5)


def test_assignment_4_activity_1_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 4", "Activity 1")


def test_assignment_4_activity_1_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 4", "Activity 1")


def test_assignment_4_activity_1_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 4", "Activity 1")


def test_assignment_4_activity_1_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 4", "Activity 1")


def test_assignment_4_activity_1_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 4", "Activity 1")


def test_assignment_4_activity_1_source_code_line_spacing():
    test.check_source_code_line_spacing("Assignment 4", "Activity 1")


def test_assignment_4_activity_1_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 1",
        "",
        "10\n15\n",
        "hours.*?\n?.*?rate",
        "Input label(s) missing or incorrect. "
            "Expecting hours and rate.")


def test_assignment_4_activity_1_weekly_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 1",
        "",
        "10\n15\n",
        "150",
        "weekly calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 1",
        "",
        "10.5\n15.5\n",
        "162.75",
        "weekly calculation output is incorrect.")


def test_assignment_4_activity_1_monthly_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 1",
        "",
        "10\n15\n",
        "600|650",
        "monthly calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 1",
        "",
        "10.5\n15.5\n",
        "651.0|705.25",
        "monthly calculation output is incorrect.")


def test_assignment_4_activity_1_yearly_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 1",
        "",
        "10\n15\n",
        "7800",
        "yearly calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 1",
        "",
        "10.5\n15.5\n",
        "8463.0",
        "yearly calculation output is incorrect.")


def test_assignment_4_activity_1_weekly_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 1",
        "",
        "10\n15\n",
        r"week.+?150|150.+?week",
        "weekly output label is missing or incorrect.")


def test_assignment_4_activity_1_monthly_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 1",
        "",
        "10\n15\n",
        r"month.+?6|6.+?month",
        "monthly output label is missing or incorrect.")


def test_assignment_4_activity_1_yearly_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 1",
        "",
        "10\n15\n",
        r"year.+?7800|7800.+?year|annual.+?7800|7800.+?annual",
        "yearly output label is missing or incorrect.")


def test_assignment_4_activity_2_source_code_comments():
    test.check_source_code_comments("Assignment 4", "Activity 2", 1)


def test_assignment_4_activity_2_source_code_inputs():
    test.check_source_code_inputs("Assignment 4", "Activity 2", 1)


def test_assignment_4_activity_2_source_code_processing():
    test.check_source_code_processing("Assignment 4", "Activity 2", 5)


def test_assignment_4_activity_2_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 4", "Activity 2")


def test_assignment_4_activity_2_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 4", "Activity 2")


def test_assignment_4_activity_2_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 4", "Activity 2")


def test_assignment_4_activity_2_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 4", "Activity 2")


def test_assignment_4_activity_2_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 4", "Activity 2")


def test_assignment_4_activity_2_source_code_line_spacing():
    test.check_source_code_line_spacing("Assignment 4", "Activity 2")


def test_assignment_4_activity_2_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 2",
        "",
        "1\n",
        "age|years",
        "Input label(s) missing or incorrect. Expecting years.")


def test_assignment_4_activity_2_months_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 2",
        "",
        "1\n",
        "12",
        "months calculation output is incorrect.")


def test_assignment_4_activity_2_days_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 2",
        "",
        "1\n",
        "365",
        "days calculation output is incorrect.")


def test_assignment_4_activity_2_hours_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 2",
        "",
        "1\n",
        "8760",
        "hours calculation output is incorrect.")


def test_assignment_4_activity_2_seconds_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 2",
        "",
        "1\n",
        "31536000",
        "seconds calculation output is incorrect.")


def test_assignment_4_activity_2_months_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 2",
        "",
        "1\n",
        "month.+?12|12.+?month",
        "months calculation or output label is missing or incorrect.")


def test_assignment_4_activity_2_days_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 2",
        "",
        "1\n",
        "day.+?365|365.+?day",
        "days calculation or output label is missing or incorrect.")


def test_assignment_4_activity_2_hours_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 2",
        "",
        "1\n",
        "hour.+?8760|8760.+?hour",
        "hours calculation or output label is missing or incorrect.")


def test_assignment_4_activity_2_seconds_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 2",
        "",
        "1\n",
        "seconds.+?31536000|31536000.+?seconds",
        "seconds calculation or output label is missing or incorrect.")


def test_assignment_4_activity_2_minutes_calculation():
    test.check_file_does_not_contain(
        "Assignment 4",
        "Activity 2",
        r"(cs|java|js|lua|py)",
        "minute",
        "processing error. Processing should not include minutes.")


def test_assignment_4_activity_3_source_code_comments():
    test.check_source_code_comments("Assignment 4", "Activity 3", 1)


def test_assignment_4_activity_3_source_code_inputs():
    test.check_source_code_inputs("Assignment 4", "Activity 3", 1)


def test_assignment_4_activity_3_source_code_processing():
    test.check_source_code_processing("Assignment 4", "Activity 3", 4)


def test_assignment_4_activity_3_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 4", "Activity 3")


def test_assignment_4_activity_3_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 4", "Activity 3")


def test_assignment_4_activity_3_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 4", "Activity 3")


def test_assignment_4_activity_3_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 4", "Activity 3")


def test_assignment_4_activity_3_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 4", "Activity 3")


def test_assignment_4_activity_3_source_code_line_spacing():
    test.check_source_code_line_spacing("Assignment 4", "Activity 3")


def test_assignment_4_activity_3_source_code_file_contains():
    test.check_file_contains(
        "Assignment 4",
        "Activity 3",
        r"(cs|java|js|lua|py)",
        "feet|meter",
        "must include output labels with either feet or meters.")


def test_assignment_4_activity_3_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "",
        "1\n",
        "mile",
        "input label(s) missing or incorrect. Expecting miles.")


def test_assignment_4_activity_3_yards_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "feet",
        "1\n",
        "1760",
        "yards calculation output is incorrect.")


def test_assignment_4_activity_3_feet_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "feet",
        "1\n",
        "5280",
        "feet calculation output is incorrect.")


def test_assignment_4_activity_3_inches_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "feet",
        "1\n",
        r"63360",
        "inches calculation output is incorrect.")


def test_assignment_4_activity_3_yards_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "feet",
        "1\n",
        r"yard.+?1760|1760.+?yard",
        "yards calculation or output label is missing or incorrect.")


def test_assignment_4_activity_3_feet_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "feet",
        "1\n",
        r"feet.+?5280|5280.+?feet",
        "feet calculation or output label is missing or incorrect.")


def test_assignment_4_activity_3_inches_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "feet",
        "1\n",
        r"inches.+?63360|63360.+?inches",
        "inches calculation or output label is missing or incorrect.")


def test_assignment_4_activity_3_kilometers_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "meter",
        "1\n",
        "1.6",
        "kilometers calculation output is incorrect.")


def test_assignment_4_activity_3_meters_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "meter",
        "1\n",
        r"16\d{2}",
        "meters calculation output is incorrect.")


def test_assignment_4_activity_3_centimeters_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "meter",
        "1\n",
        r"16\d{4}",
        "centimeters calculation output is incorrect.")


def test_assignment_4_activity_3_kilometers_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "meter",
        "1\n",
        r"kilometer.+?1\.6|1\.6.+?kilometer",
        "kilometers calculation or output label is missing or incorrect.")


def test_assignment_4_activity_3_meters_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "meter",
        "1\n",
        r"meter.+?16\d{2}|16\d{2}.+?meter",
        "mneters calculation or output label is missing or incorrect.")


def test_assignment_4_activity_3_centimeters_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 3",
        "meter",
        "1\n",
        r"centimeter.+?16\d{4}|16\d{4}.+?centimeter",
        "centimeters calculation or output label is missing or incorrect.")


def test_assignment_4_activity_4_source_code_comments():
    test.check_source_code_comments("Assignment 4", "Activity 4", 1)


def test_assignment_4_activity_4_source_code_inputs():
    test.check_source_code_inputs("Assignment 4", "Activity 4", 2)


def test_assignment_4_activity_4_source_code_processing():
    test.check_source_code_processing("Assignment 4", "Activity 4", 4)


def test_assignment_4_activity_4_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 4", "Activity 4")


def test_assignment_4_activity_4_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 4", "Activity 4")


def test_assignment_4_activity_4_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 4", "Activity 4")


def test_assignment_4_activity_4_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 4", "Activity 4")


def test_assignment_4_activity_4_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 4", "Activity 4")


def test_assignment_4_activity_4_source_code_line_spacing():
    test.check_source_code_line_spacing("Assignment 4", "Activity 4")


def test_assignment_4_activity_4_source_code_file_contains():
    test.check_file_contains(
        "Assignment 4",
        "Activity 4",
        r"(cs|java|js|lua|py)",
        "triangle|rectangle|trapezoid|ellipse|"
            "square|parallelogram|circle|sector",
        "must indicate shape type.")


def test_assignment_4_activity_4_triangle_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "triangle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        r"base.*?\n?.*?height",
        "input label(s) missing or incorrect. "
            "Expecting base and height.")


def test_assignment_4_activity_4_triangle_area_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "rectangle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "0.5",
        "triangle area calculation output is incorrect. "
            "Expected 0.5")


def test_assignment_4_activity_4_triangle_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "triangle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "triangle.+?area.+?0.5|area.+?triangle.+?0.5|"
            "0.5.+?triangle.+?0.5.+?area|area.+?triangle",
        "triangle calculation or output label is missing or incorrect.")


def test_assignment_4_activity_4_rectangle_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "rectangle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        r"width.*?\n?.*?height|length.*?\n?.*?width",
        "input label(s) missing or incorrect. "
            "Expecting width and height.")


def test_assignment_4_activity_4_rectangle_area_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "rectangle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "1.0",
        "rectangle area calculation output is incorrect. "
            "Expected 1.0")


def test_assignment_4_activity_4_rectangle_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "rectangle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "rectangle.+?area.+?1.0|area.+?rectangle.+?1.0|"
            "1.0.+?rectangle.+?1.0.+?area|area.+?rectangle",
        "rectangle calculation or output label is missing or incorrect.")


def test_assignment_4_activity_4_trapezoid_area_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "trapezoid",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "1.0",
        "trapezoid area calculation output is incorrect. "
            "Expected 1.0")


def test_assignment_4_activity_4_trapezoid_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "trapezoid",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "trapezoid.+?area.+?1.0|area.+?trapezoid.+?1.0|"
            "1.0.+?trapezoid.+?1.0.+?area|area.+?trapezoid",
        "trapezoid calculation or output label is missing or incorrect.")


def test_assignment_4_activity_4_ellipse_area_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "ellipse",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "3.14",
        "ellipse area calculation output is incorrect. "
            "Expected 3.14")


def test_assignment_4_activity_4_ellipse_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "ellipse",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "ellipse.+?area.+?3.14|area.+?ellipse.+?3.14|"
            "3.14.+?ellipse.+?3.14.+?area|area.+?ellipse",
        "ellipse calculation or output label is missing or incorrect.")


def test_assignment_4_activity_4_square_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "square",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "side|base|height|length|width",
        "input label(s) missing or incorrect. "
            "Expecting side.")


def test_assignment_4_activity_4_square_area_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "square",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "1.0",
        "square area calculation output is incorrect. "
            "Expected 1.0")


def test_assignment_4_activity_4_square_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "square",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "square.+?area.+?1.0|area.+?square.+?1.0|"
            "1.0.+?square.+?1.0.+?area|area.+?square",
        "square calculation or output label is missing or incorrect.")


def test_assignment_4_activity_4_parallelogram_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "parallelogram",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        r"base.*?\n?.*?height",
        "input label(s) missing or incorrect. "
            "Expecting base and height.")


def test_assignment_4_activity_4_parallelogram_area_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "parallelogram",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "1.0",
        "parallelogram area calculation output is incorrect. "
            "Expected 1.0")


def test_assignment_4_activity_4_parallelogram_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "parallelogram",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "parallelogram.+?area.+?1.0|area.+?parallelogram.+?1.0|"
            "1.0.+?parallelogram.+?1.0.+?area|area.+?parallelogram",
        "parallelogram calculation or output label is missing or incorrect.")


def test_assignment_4_activity_4_circle_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "circle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "radius",
        "input label(s) missing or incorrect. "
            "Expecting radius.")


def test_assignment_4_activity_4_circle_area_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "circle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "3.14",
        "circle area calculation output is incorrect. "
            "Expected 3.14")


def test_assignment_4_activity_4_circle_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "circle",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "circle.+?area.+?3.14|area.+?circle.+?3.14|"
            "3.14.+?circle.+?3.14.+?area|area.+?circle",
        "circle calculation or output label is missing or incorrect.")


def test_assignment_4_activity_4_sector_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "sector",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "radius",
        "input label(s) missing or incorrect. "
            "Expecting radius.")


def test_assignment_4_activity_4_sector_area_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "sector",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "0.5",
        "sector area calculation output is incorrect. "
            "Expected 0.5")


def test_assignment_4_activity_4_sector_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 4",
        "sector",
        "1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n",
        "sector.+?area.+?0.5|area.+?sector.+?0.5|"
            "0.5.+?sector.+?0.5.+?area|area.+?sector",
        "sector calculation or output label is missing or incorrect.")


def test_assignment_4_activity_5_source_code_comments():
    test.check_source_code_comments("Assignment 4", "Activity 5", 1)


def test_assignment_4_activity_5_source_code_inputs():
    test.check_source_code_inputs("Assignment 4", "Activity 5", 2)


def test_assignment_4_activity_5_source_code_processing():
    test.check_source_code_processing("Assignment 4", "Activity 5", 3)


def test_assignment_4_activity_5_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 4", "Activity 5")


def test_assignment_4_activity_5_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 4", "Activity 5")


def test_assignment_4_activity_5_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 4", "Activity 5")


def test_assignment_4_activity_5_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 4", "Activity 5")


def test_assignment_4_activity_5_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 4", "Activity 5")


def test_assignment_4_activity_5_source_code_line_spacing():
    test.check_source_code_line_spacing("Assignment 4", "Activity 5")


def test_assignment_4_activity_5_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 5",
        "",
        "10\n10\n",
        "length.*?\n?.*?width",
        "input label(s) missing or incorrect. "
            "Expecting length and width.")


def test_assignment_4_activity_5_area_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 5",
        "",
        "10\n10\n",
        r"11\.11",
        "area calculation output is incorrect.")

    test.check_source_code_output(
        "Assignment 4",
        "Activity 5",
        "",
        "10.5\n10.5\n",
        "12.25",
        "area calculation output is incorrect.")


def test_assignment_4_activity_5_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 5",
        "",
        "10\n10\n",
        r"yards.+?11\.11|11\.11.+?yards",
        "area output label is missing or incorrect. "
            "Expecting yards.")


def test_assignment_4_activity_6_source_code_comments():
    test.check_source_code_comments("Assignment 4", "Activity 6", 1)


def test_assignment_4_activity_6_source_code_inputs():
    test.check_source_code_inputs("Assignment 4", "Activity 6", 5)


def test_assignment_4_activity_6_source_code_processing():
    test.check_source_code_processing("Assignment 4", "Activity 6", 8)


def test_assignment_4_activity_6_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 4", "Activity 6")


def test_assignment_4_activity_6_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 4", "Activity 6")


def test_assignment_4_activity_6_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 4", "Activity 6")


def test_assignment_4_activity_6_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 4", "Activity 6")


def test_assignment_4_activity_6_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 4", "Activity 6")


def test_assignment_4_activity_6_source_code_line_spacing():
    test.check_source_code_line_spacing("Assignment 4", "Activity 6")


def test_assignment_4_activity_6_gallons_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 6",
        "",
        "10\n10\n8\n300\n30\n",
        "2",
        "gallons calculation output is incorrect.")


def test_assignment_4_activity_6_cost_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 6",
        "",
        "10\n10\n8\n300\n30\n",
        "60.0",
        "cost calculation output is incorrect.")


def test_assignment_4_activity_6_gallons_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 6",
        "",
        "10\n10\n8\n300\n30\n",
        "gallon.+?2|2.+?gallon",
        "gallons calculation or output label is missing or incorrect.")


def test_assignment_4_activity_6_cost_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 6",
        "",
        "10\n10\n8\n300\n30\n",
        r"cost.+?60\.0|price.+?60\.0|60\.0.+?price|60\.0.+?cost",
        "cost calculation or output label is missing or incorrect.")


def test_assignment_4_activity_7_source_code_comments():
    test.check_source_code_comments("Assignment 4", "Activity 7", 1)


def test_assignment_4_activity_7_source_code_inputs():
    test.check_source_code_inputs("Assignment 4", "Activity 7", 2)


def test_assignment_4_activity_7_source_code_processing():
    test.check_source_code_processing("Assignment 4", "Activity 7", 3)


def test_assignment_4_activity_7_source_code_comment_formatting():
    test.check_source_code_comment_formatting("Assignment 4", "Activity 7")


def test_assignment_4_activity_7_source_code_identifier_formatting():
    test.check_source_code_identifier_formatting("Assignment 4", "Activity 7")


def test_assignment_4_activity_7_source_code_identifier_length():
    test.check_source_code_identifier_length("Assignment 4", "Activity 7")


def test_assignment_4_activity_7_source_code_operator_formatting():
    test.check_source_code_operator_formatting("Assignment 4", "Activity 7")


def test_assignment_4_activity_7_source_code_comma_formatting():
    test.check_source_code_comma_formatting("Assignment 4", "Activity 7")


def test_assignment_4_activity_7_source_code_line_spacing():
    test.check_source_code_line_spacing("Assignment 4", "Activity 7")


def test_assignment_4_activity_7_input_labels():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 7",
        "",
        "Rover\n2\n",
        "name.*?\n?.*?age|name.*?\n?.*?old",
        "input label(s) missing or incorrect. "
            "Expecting name and age.")


def test_assignment_4_activity_7_age_calculation():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 7",
        "",
        "Rover\n2\n",
        "14",
        "age calculation output is incorrect.")


def test_assignment_4_activity_7_name_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 7",
        "",
        "Rover\n2\n",
        "Rover.+?14|14.+?Rover",
        "name label or age calculation output is missing or incorrect.")


def test_assignment_4_activity_7_cost_output_label():
    test.check_source_code_output(
        "Assignment 4",
        "Activity 7",
        "",
        "Rover\n2\n",
        "year.+?14|14.+?year",
        "age output label is missing or incorrect. "
            "Expected years.")
