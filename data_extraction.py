# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    data_extraction.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abaiao-r <abaiao-r@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/27 19:51:08 by abaiao-r          #+#    #+#              #
#    Updated: 2024/05/27 20:33:43 by abaiao-r         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils import *
import csv

# extract_csv() function: extracts the data from a csv file
# file_name: string with the name of the file
# header: boolean parameter with True as default argument
# return: the data and the header or just the data if header is False as a list
def extract_csv(file_name, header=True):
    if file_name is None:
        print("Error : no file name provided for extract_csv function")
        return (None)
    try:
        csv_file = open(file_name, encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: {file_name} not found")
        return (None)
    except Exception as e:
        print(f"Error: {e}")
        return (None)

    csv_reader = csv.reader(csv_file)
    data = list(csv_reader)
    if header:
        data_header = data[0]
        data = data[1:]
        csv_file.close()
        return data, data_header
    else:
        csv_file.close()
        return data

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
