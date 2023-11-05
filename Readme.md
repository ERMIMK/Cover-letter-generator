# Cover Letter Generator

This project is a Python application that automatically generates a cover letter based on user input. The cover letter can be output as either a text file or a PDF document.

## Features

- Interactive prompts to collect cover letter details
- Generates a cover letter in text or PDF format
- Customizable for different job positions and companies

## Requirements

To run this program, you'll need:

- Python installed on your system.
- FPDF package for PDF generation (`pip install fpdf`).

## Usage

1. Clone the repository to your local machine.
2. Run the script using Python.

    ```bash
    python cover_letter_generator.py
    ```

3. Follow the on-screen prompts to enter the required details for your cover letter.
4. Choose the output format (TXT or PDF).
5. Find the generated cover letter in the specified output directory.

## Inputs

The script will ask for the following information:

- Date of the cover letter
- Position applying for
- Type of position (JOB/INTERNSHIP)
- Company name
- Address of the position
- Employer's name
- Where you found the position
- Skills and qualifications
- Optional additional skills
- Good attributes of the company

## Outputs

The script will generate a cover letter with the provided details and save it as:

- `generated.txt` for text output
- `generated.pdf` for PDF output

## Customization

The cover letter template within the script can be customized by editing the `generate_cl` function to suit individual needs or preferences.

## Contribution

Feel free to fork, suggest improvements, or submit pull requests.

## Contact

For any queries or feedback, please reach out to [your email].

## Disclaimer

This project is for educational purposes only and is not intended for commercial use.

