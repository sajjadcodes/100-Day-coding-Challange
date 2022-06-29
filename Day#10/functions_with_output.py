#function with output : return value

def format_name(f_name, l_name):
    formated_f_name = f_name.title();
    formated_l_name = l_name.title();
    
    return f"{formated_f_name} {formated_l_name}"



f_name = input("Enter your first name")

l_name = input("Enter your last name")

formated_name = format_name(f_name, l_name)

print(formated_name)