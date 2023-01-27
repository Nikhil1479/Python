def format_name(first_name, last_name):
    fname = first_name[0].upper() + first_name[1:].lower()
    lname = last_name[0].upper() + last_name[1:].lower()
    print(fname + " " + lname)

    ##################### OR #########################
    #! Use title() function
    fname = first_name.title()
    lname = last_name.title()

format_name("nIkHil","gupta")
