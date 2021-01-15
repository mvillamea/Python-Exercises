"""Create a function that receives a list of strings that are arithmetic problems
and returns the problems arranged vertically and side-by-side.
The function should optionally take a second argument.
When the second argument is set to True, the answers should be displayed."""

def split_list(list):
    """splits everything by the spaces
    Example:
        input= [12 13, 14]
        output= [12, 13, 14]"""
    new_list = []
    for i in range(len(list)):
        new_list_i = list[i].split(' ')
        new_list = new_list.__add__(new_list_i)
    return new_list


def get_first_numbers(list):
    """It will get the first
    numbers of the calc"""
    first_numbers = []
    for i in range(0, len(list), 3):
        first_numbers = first_numbers.__add__([list[i]])
    return first_numbers


def get_signs(list):
    """It will get the signs
        of the calc"""
    signs = []
    for i in range(1, len(list), 3):
        signs = signs.__add__([list[i]])
    return signs


def get_second_numbers(list):
    """It will get the second
        numbers of the calc"""
    second_numbers = []
    for i in range(2, len(list), 3):
        second_numbers = second_numbers.__add__([list[i]])
    return second_numbers


def check_all_numbers(list):
    """checks if all the elements
    of the list are numbers"""

    for i in range(len(list)):
        try:
            list[i] = int(list[i])
            return True
        except:
            return False


def check_length_numbers(list):
    """checks if all the elements of
    the list have length lower than 5"""
    condition = True
    for i in range(len(list)):
        if len(str(list[i]))>4:
            condition=False
    return condition


def get_solution(num_1, num_2, op):
    """gets the solution of the calc"""
    num_1 = int(num_1)
    num_2 = int(num_2)
    solution = 0
    if op == '+':
        solution=solution+num_1+num_2
    else:
        solution = solution + num_1 - num_2
    return solution


def arithmetic_arranger(problems, solution=False):

    aux_list = split_list(problems)
    first_numbers = get_first_numbers(aux_list) # gets the first numbers
    signs = get_signs(aux_list)  # gets the + or - signs
    second_numbers = get_second_numbers(aux_list) # gets the second numbers
    line_1 = ''
    line_2 = ''
    line_3 = ''
    line_4 = ''

    if len(problems)>5: # checks if there are more than 5 problems
        return 'Error: Too many problems.'

    elif ('*' in signs) or ('/' in signs): # checks that there are no * or / operators
        return "Error: Operator must be '+' or '-'."

    elif (not check_all_numbers(first_numbers)) or (not check_all_numbers(second_numbers)):
        # checks that the first and second numbers are digits
        return 'Error: Numbers must only contain digits.'

    elif (not check_length_numbers(first_numbers)) or (not check_length_numbers(second_numbers)):
        # checks that the first and second numbers are no longer than 4 digits
        return 'Error: Numbers cannot be more than four digits.'

    else:
        for i in range(len(problems)):
            if solution == False: # first case: we don't need the solution
                max_length = max(len(str(first_numbers[i])), len(str(second_numbers[i]))) # useful for the spaces and dashes
                line_1 += str(first_numbers[i]).rjust(max_length+2)  # first line: first number right
                line_2 += str(signs[i])+str(second_numbers[i]).rjust(max_length+1) #second line: operator and second number
                line_3 += ('-' * (max_length + 2)).rjust(max_length+2) #third line: dashes

                if i < len(problems) - 1:
                    line_1 += "    "
                    line_2 += "    "
                    line_3 += "    "

                arranged_problems = line_1+'\n'+line_2+'\n'+line_3 # joins everything

            else: #if we want the solution
                max_length = max(len(str(first_numbers[i])), len(str(second_numbers[i]))) # useful for the spaces and dashes
                line_1 += str(first_numbers[i]).rjust(max_length + 2)  # first line: first number right
                line_2 += str(signs[i]) + str(second_numbers[i]).rjust(max_length + 1)  #second line: operator and second number
                line_3 += ('-' * (max_length + 2)).rjust(max_length + 2) #third line: dashes
                line_4 += str(get_solution(first_numbers[i], second_numbers[i], signs[i])).rjust(max_length+2) # forth line: solutions

                if i < len(problems) - 1:
                    # adds the spaces between calcs
                    line_1 += "    "
                    line_2 += "    "
                    line_3 += "    "
                    line_4 += "    "

                arranged_problems = line_1 + '\n' + line_2 + '\n' + line_3 + '\n' + line_4 # joins everything


    return arranged_problems








