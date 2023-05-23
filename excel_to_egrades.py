import pandas as pd
import os
import argparse
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def acquire_file():
    """
    This function opens a file dialog for the user to choose a file.
    It returns the path of the chosen file.
    """
    Tk().withdraw()
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = askopenfilename(initialdir=script_dir, title="Please select the moodle excel document containing the student grades.")
    return file_path

def parse_data_frame(file_path):
    """
    This function reads the file at the given path into a DataFrame.
    It capitalizes the 'a' in the student ID and prepends "txt" to it.
    It returns the parsed DataFrame.
    """
    df = pd.read_excel(file_path)
    id_column = df.columns[2]
    grade_column = df.columns[7]
    df = df[[id_column, grade_column]]
    df[id_column] = df[id_column].str.upper()
    df[id_column] = "txt" + df[id_column]
    return df

def get_scaling_factor():
    """
    This function gets the scaling factor from the command line arguments.
    If the user provides a number, the function returns this number.
    If the user does not provide a number or does not provide anything, the function returns 1.
    """
    parser = argparse.ArgumentParser(description="Enter a scaling factor for the grades.")
    parser.add_argument('--scale', default=1, type=float, help='The scaling factor for the grades.')
    args = parser.parse_args()

    if args.scale:
        scaling_factor = args.scale
    else:
        print("No scaling factor provided. Using scaling factor of 1.")
        scaling_factor = 1.0

    return scaling_factor

def create_js_code(df, input_file_path, scaling_factor=1):
    """
    This function generates JavaScript code from the DataFrame to fill in the grades.
    It writes this code to a .js file.
    The .js file is named 'inject_grades_<input_file_name>.js' and is located in the same directory as the input file.
    
    :param df: DataFrame containing student ID and grades
    :param input_file_path: String path of the input excel file
    :param scaling_factor: The factor by which to scale the grades
    """

    js_code = ""
    for index, row in df.iterrows():
        user_id = row[df.columns[0]]
        raw_grade = row[df.columns[1]]
        grade = 0 if raw_grade == "-" else raw_grade/scaling_factor
        grade = format(grade, '.2f').rstrip('0').rstrip('.') if isinstance(grade, float) else grade
        js_code += f'document.getElementById("{user_id}").value = "{grade}";\n'

    # Extract the base name of the input file (without extension)
    input_file_name = os.path.splitext(os.path.basename(input_file_path))[0]

    # Construct the output file path
    output_file_path = os.path.join(os.path.dirname(input_file_path), f'inject_grades_{input_file_name}.js')

    with open(output_file_path, 'w') as file:
        file.write(js_code)


file_path = acquire_file()
df = parse_data_frame(file_path)
create_js_code(df, file_path, get_scaling_factor())
