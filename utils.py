# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abaiao-r <abaiao-r@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/27 20:28:04 by abaiao-r          #+#    #+#              #
#    Updated: 2024/05/28 12:41:43 by abaiao-r         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# print_separator() function: prints a separator
# return: nothing, just prints a separator
def print_separator():
    print("\n")
    print("----------------------------------------\n")
    print("\n")
    
# print_dataset_slice() function: allows us to explore the rows and columns of a 
# dataset
# dataset: list of lists
# start and end: integers that slice the dataset
# rows_and_columns: boolean parameter with False as default argument
# return: nothing, just prints the number of rows and columns and slices the 
# dataset
def print_dataset_slice(dataset, start, end, rows_and_columns = False):
    dataset_slice = dataset[start:end]
    for i in dataset_slice:
        print(i);
        print("\n");
        
    if rows_and_columns:
        print("Number of rows: ", len(dataset))
        print("Number of columns: ", len(dataset[0]))