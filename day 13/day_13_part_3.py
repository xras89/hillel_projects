def update_hero(**kwargs):
    file_name = "hero.ini"

    # Read data from a file
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Change field values according to the specified parameters
    for i in range(len(lines)):
        for key, value in kwargs.items():
            if key.lower() in lines[i].lower():
                lines[i] = f"{key}={value}\n"

    # Overwrite the file with new values
    with open(file_name, 'w') as file:
        file.writelines(lines)


# An example of a function call
update_hero(hero="Halk", power=450, Y=2.3)
