def bubble_sort(list_of_numbers) -> list:

    def validate_data_list(data_list) -> list:
        new_data_list = []
        if type(data_list) is not list:  # Check if the numbers are within a list.
            print('Only list! Try again!')
            exit()
        if data_list is []:  # Check if the list is not empty.
            print('Empty list! Try again!')
            exit()
        for data in data_list:
            data = str(data)
            if not data.lstrip('-').isnumeric():  # Check if the data of list is a number(ignores the symbol "-").
                print(f'The data "{data}" is not a number. Add only numbers! Try again!')
                exit()
            else:
                new_data_list.append(int(data))
        return new_data_list

    def bubble_sort_resolver() -> list:

        list_of_numbers_valided = validate_data_list(list_of_numbers)  # Validates input data

        revolved = False
        while not revolved:  # As long as it does not resolve, the classification continues.

            revolved = True
            list_of_numbers_size = len(list_of_numbers_valided)

            for list_index in range(list_of_numbers_size - 1):
                first_number = list_of_numbers_valided[list_index]  # take the first pair number
                second_number = list_of_numbers_valided[list_index + 1]  # take the second pair number

                if first_number > second_number:  # Check if the first_number is highlest than second_number.
                    # If so, change the position of the first_number to the second_number and...
                    list_of_numbers_valided[list_index] = second_number
                    # change the position of the first_number to the second_number.
                    list_of_numbers_valided[list_index + 1] = first_number

                    revolved = False

        return list_of_numbers_valided  # If resolved is True, returns the sort result

    list_of_numbers_resolved = bubble_sort_resolver()

    return list_of_numbers_resolved


if __name__ == '__main__':
    my_list = [-1, 7, 9, 0, 13, -11, 0, '3', '13', 8, -5]
    print(bubble_sort(my_list))
