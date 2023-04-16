# used to capture user input
import sys
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
        # check if char is the same as the first letter of the substring
        if char == sub_str[0]:
            same_as_char = True
            alpha_copy = [letter for letter in alpha if letter != char]

        else:
            same_as_char = False
            alpha_copy = [letter for letter in alpha if letter !=
                          char and letter != sub_str[0]]

        alpha_copy = ','.join(alpha_copy)

        yaml_output += f" S{index}:\n"

        yaml_output += f"  [{alpha_copy}] : " + "{R: S0}\n"

        if not same_as_char:
            if index == len(sub_str) - 1:
                yaml_output += f"  {char} : " + "{R: Done}\n"

            else:
                yaml_output += f"  {char} : " + "{R: S"+str(index+1)+"}\n"
            yaml_output += f"  {sub_str[0]} : " + "{R: S1}\n"

        else:
            yaml_output += f"  {char} : " + "{R: S"+str(index+1)+"}\n"

    alpha = ",".join(alpha)
    yaml_output += f" Done:\n  [{alpha}] : " + "R\n"

    with open('turningmachine.io.yaml', 'w') as out:
        out.write(yaml_output)


if __name__ == '__main__':

    # support user input
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        main('pythonisprettygreatngl', 'great')
