# Excel-to-eGrades

This tool is designed to help automate the process of transferring grades from Moodle to eGrades. It does so by taking an Excel file export of grades from Moodle, parsing it to extract relevant information, and generating a JavaScript file that can be run in your web browser to automatically fill in grades on the eGrades page.

## Prerequisites

Before running the script, make sure that you have the following software installed on your machine:

- Python 3.x
- Required Python libraries: pandas, tkinter

## How to Use

### Step 1: Export Grades from Moodle

The first step is to export the grades from Moodle as an excel file. To do this, follow the instructions provided in the [Moodle documentation](https://docs.moodle.org/402/en/Grade_export).

### Step 2: Run the Script

In the directory where the script is located, run the script using Python:

```bash
python grades_converter.py --scale_factor 10
```

The `scale_factor` argument is optional and defaults to 1. This argument allows you to scale the grades if necessary. For example, if the total possible grade in Moodle is 100 but in eGrades it's 10, you would use a scale factor of 10.

A file dialog will appear. Select the Excel file that you exported from Moodle.

### Step 3: Inject the JavaScript Code into eGrades

The script will generate a JavaScript file named 'inject_grades_[input_file_name].js' in the same directory as the input Excel file.

To use this JavaScript file:

1. Navigate to the eGrades page for the corresponding grades.
2. Open your browser's JavaScript console. In Chrome and Edge, you can do this by right-clicking on the page, selecting 'Inspect', and then navigating to the 'Console' tab.
3. Copy the contents of the generated JavaScript file and paste them into the console, then press Enter.

The JavaScript code will automatically fill in the grades in the eGrades page.

Please note: The tool is intended to help automate the grade transfer process, but it is still important to verify that the grades have been transferred correctly.
