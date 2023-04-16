# only used for alphabet
import string


def main(original, search):

    original = original.strip().lower()

    yaml_output = f"input: '{original}'\n"
    yaml_output += f"blank: ' '\n"
    yaml_output += f"start state: S0\n"
    yaml_output += f"table:\n"

    # our array of substring characters
    sub_str = search.strip()
    sub_str = [char for char in sub_str]

    # get letters of alpha
    alpha_as_string = string.ascii_lowercase

    # alpha will be our array of lowercase letters
    alpha = [alpha_as_string[i] for i in range(26)]

    # iterate through each
    for index, char in enumerate(sub_str):

        # generate list of values that return us to start
        alpha_copy = [letter for letter in alpha if letter != char]
        alpha_copy = ','.join(alpha_copy)

        yaml_output += f" S{index}:\n"

        yaml_output += f"  [{alpha_copy}] : " + "{R: S0}\n"
        if index != len(sub_str) - 1:
            yaml_output += f"  {char} : " + "{R: S"+str(index+1)+"}\n"

        else:
            yaml_output += f"  {char} : " + "{R: Done}\n"

    alpha = ",".join(alpha)
    yaml_output += f" Done:\n  [{alpha}] : " + "R\n"

    with open('turningmachine.io.yaml', 'w') as out:
        out.write(yaml_output)


if __name__ == '__main__':
    main('pythonisprettygreatngl', 'great')
