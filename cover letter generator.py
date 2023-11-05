# Importing the FPDF class from the fpdf package for PDF generation
from fpdf import FPDF

# Function to get inputs from the user for the cover letter
def get_input():
    # Prompting user for various details to include in the cover letter
    cl_date = input("Input the date of the cover letter: ")
    cl_position = input("Input the position: ")
    cl_type = input("Input the type of the position, JOB/INTERNSHIP: ")
    cl_company_name = input("Input the company Name: ")
    cl_address = input("Where is the address of the position: ")
    cl_noe = input("Input name of employer: ")
    cl_posted = input("Where did you find the position?: ")
    cl_skill01 = input("What skill blend with the position (can put more than two using a comma): ")
    cl_skill02 = input("What is the required skill: ")
    cl_optional_skill = input("Any skill you want to include (OPTIONAL, press enter if none): ")
    Cl_additional = input("Any additional things to include: ")
    cl_good = input("Any good thing about the company: ")

    # Compiling all inputs into a list
    input_lst = [cl_date, cl_position, cl_company_name, cl_type, cl_address, cl_noe, 
                 cl_skill01, cl_skill02, cl_optional_skill, cl_posted, Cl_additional, cl_good]
    return input_lst

# Function to generate the cover letter text from the input list
def generate_cl(lst):
    # Unpacking the list into individual variables for use in the cover letter
    (cl_date, cl_position, cl_company_name, cl_type, cl_address, cl_noe, cl_skill01, 
     cl_skill02, cl_optional_skill, cl_posted, Cl_additional, cl_good_things) = lst
    
    # Template text for the cover letter, inserting the user's inputs
    TEXT = ('''
    ...
    '''.format(cl_date, cl_position, cl_company_name, cl_address, cl_noe, cl_position, 
               cl_company_name, cl_posted, cl_company_name, cl_skill01, cl_skill02, 
               cl_optional_skill, cl_skill02, cl_skill01, cl_company_name, cl_company_name, 
               cl_position, Cl_additional, cl_type, cl_position, cl_good_things, 
               cl_company_name))
    return TEXT

# Function to write the cover letter to a text file
def txt(filename, MENU):
    # Opening the file with written permission
    with open("/Users/.../Desktop/"+filename, "w") as fp:        # modify this
        # Writing the generated cover letter to the file
        fp.write(MENU)

# Function to write the cover letter to a PDF file
def pdf(TEXT, filename):
    # Creating a PDF object
    pdf = FPDF()
    # Adding a page to the PDF
    pdf.add_page()
    # Setting the font for the PDF
    pdf.set_font("Arial", size = 15)
    # Adding the cover letter text to the PDF
    pdf.cell(200, 10, txt = TEXT, align = 'L')
    # Outputting the PDF to the specified file
    pdf.output("/Users/...Desktop/"+filename) #modify this

# Main function to run the cover letter generator
def main():
    while True:
        # User interface for the script
        print("-"*60)
        print("          WELCOME TO COVER LETTER GENERATOR     ")
        print("_"*60)
        print("\n")

        # Getting user input
        user_in = get_input()

        # Generating the cover letter text
        text = generate_cl(user_in)
    
        # Asking the user for the desired output format
        type_choice = input("What kind of output do you want? TXT or PDF: ").lower()
        if type_choice == "txt":
            # Generate a TXT file if the user chooses text format
            txt("generated.txt", text)
            print("Generating TXT Successfully completed!!!")
        elif type_choice == "pdf":
            # Generate a PDF file if the user chooses PDF format
            pdf(text, "generated.pdf")
            print("Generating PDF Successfully completed!!!")
        else:
            # Informs the user of an incorrect input
            print("Incorrect input")

        # Asking the user if they want to create another cover letter
        qui = input("DO YOU WANT TO CONTINUE (y/n): ").lower()
        print("-"*40)
        # If the user confirms, continue; otherwise, break the loop and end the program
        if qui in ('yes', 'y'):
            continue
        else:
            break
        
# Ensures the main function is only executed when the script is run directly
if __name__ == '__main__':
    main()
