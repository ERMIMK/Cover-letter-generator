from fpdf import FPDF
def get_input():

    cl_date = input("Input the date of the cover letter :  ")
    cl_position = input("Input the position : ")
    cl_type = input("Input the type of the position, JOB/INTERNSHIP : ")
    cl_company_name = input("Input the company Name : ")
    cl_address = input("Where is the address of the position : ")
    cl_noe = input("input name of employer: ")
    cl_posted = input("Where did you find the position? : ")

    cl_skill01 = input("What skill blend with the postion can put more than two using comma : ")
    cl_skill02 = input("What is the required skill : ")
    cl_optional_skill  = input("Any skill want to include (OPTIONAL, Press enter if don't have) : ")
    Cl_additional = input("additional things to include : ")
    cl_good = input("Any good thing about the company : ")
    input_lst = [cl_date, cl_position, cl_company_name, cl_type, cl_address, cl_noe, cl_skill01, cl_skill02, cl_optional_skill,cl_posted,Cl_additional,cl_good]
    return input_lst


def generate_cl(lst):
    cl_date, cl_position, cl_company_name, cl_type, cl_address, cl_noe, cl_skill01, cl_skill02, cl_optional_skill,cl_posted,Cl_additional,cl_good_things = lst[0], lst[1], lst[2], lst[3],lst[4],lst[5],lst[6],lst[7],lst[8],lst[9],lst[10],lst[11]
    
    TEXT = ('''

Date: {}
    
{}
{}
{}
 
Dear {}:
    
    I am writing to express my interest in the {} position with {}. I am currently working on
getting my bachelor's degree at Michigan State University with a major in Computer Science. I discovered
the job position on {}. After reading the description regarding the job and the astonishing
background of the company, I am eager to add value to {}, and I am confident with my {}
and the other experiences that I acquired through years blended with {}
align well with the published role. {}.
    
    My experience that developed from an early age in high school in python programming, {}
and {} helped prepare me further from other applicants with my level of
education for the position at {}. Furthermore, my experiences with leadership and
communication match one of the skills that are mentioned in the description on the job posting. 
    
    In addition to this, my dedication and passion for grasping new skills as I have done in the past,
taking more than nine online courses, and acquiring considerable skills working with the harsh
circumstances and limited internet accessibility while living in Ethiopia demonstrates my commitment
to learning and attaining new skills. I will devote my summer to making an impact at {} in the
{} to add value to the company while getting {} experience at the same time. 
    
    I offer excellent programming, problem-solving, and communication skill enhanced from my 
previously held positions. I am curious, dedicated, passionate, and above all else, I am customer
centered. I am ready to use these attributes at {}, a company that {}. 
I welcome any opportunity for an interview for this role and others with {} and invite 
you to contact me at (517)-512-3734 or ermiyas.net. I look forward to hearing from you soon.
    
    
Sincerely,
Ermiyas Kifle (Ermi)
mesfiner@msu.edu'''
    .format(cl_date,cl_position, cl_company_name,cl_address,cl_noe, cl_position, cl_company_name, cl_posted,cl_company_name, cl_skill01, cl_skill02, cl_optional_skill,cl_skill02, cl_skill01, cl_company_name, cl_company_name, cl_position, Cl_additional, cl_type, cl_position,cl_good_things,cl_company_name ))
    return TEXT


def txt(filename, MENU):
    fp = open("/Users/ermiyasmesfin/Desktop/"+filename, "w")
    fp.write(MENU)
    fp.close()

def pdf(TEXT, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)

    pdf.cell(200, 10, txt = TEXT, align = 'L')
    pdf.output("/Users/ermiyasmesfin/Desktop/"+filename)


def main():
    while True:
        print("-"*60)
        print("          WELCOME TO COVER LETTER GENERATOR     ")
        print("_"*60)
        print("\n")

        user_in = get_input()

        text = generate_cl(user_in)
    
        type_choice = str(input(" What kind of output do you want? TXT or PDF : ")).lower()
        if type_choice == "txt":
            txt("generated.txt", text)
            print("Generating TXT Successfully completed!!!")

        elif type_choice == "pdf":
            pdf(text, "generated.pdf")
            print("Generating PDF Successfully completed!!!")

        else:
            print("incorrect input")

        qui = input("DO YOU WANT TO CONTINUE y/n : ").lower()
        print("-"*40)
        if qui == "yes" or qui == 'y':
            continue
        elif qui == 'no' or qui == 'n':
            break
        else:
            break

        
if __name__ == '__main__':
    main()




