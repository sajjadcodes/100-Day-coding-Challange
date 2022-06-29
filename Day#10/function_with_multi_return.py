#function with output : return value

def format_name(f_name, l_name):
    if f_name =="" or l_name == '':
        return print("You did not provide valid input")
    
    formated_f_name = f_name.title();
    formated_l_name = l_name.title();
    return f"{formated_f_name} {formated_l_name}"



f_name = input("Enter your first name")

l_name = input("Enter your last name")

print(format_name(f_name, l_name))
