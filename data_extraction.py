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

def extract_csv(file_name, header=True):
    if (file_name == None):
        print("Error : no file name provided for extract_csv function")
        return(None)
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
    if (header == True):
        data_header = data[0]
        data = data[1:]
    csv_file.close()
    return(data, data_header)

# explore_data() function: allows us to explore the rows and columns of a 
# dataset
# dataset: list of lists
# start and end: integers that slice the dataset
# rows_and_columns: boolean parameter with False as default argument
# return: nothing, just prints the number of rows and columns and slices the 
# dataset
def explore_data(dataset, start, end, rows_and_columns = False):
    dataset_slice = dataset[start:end]
    for i in dataset_slice:
        print(i);
        print("\n");
        
    if rows_and_columns:
        print("Number of rows: ", len(dataset))
        print("Number of columns: ", len(dataset[0]))
        
# print the headers and datasets() function: prints the headers and datasets
# header: list of strings
# dataset: list of lists
# dataset_name: string that represents the name of the dataset (optional)
# return: nothing, just prints the headers and datasets
def print_headers_and_datasets(header, dataset, dataset_name = None):
    if (dataset_name != None):
        print(dataset_name + ": \n");
    
    if (header):
        print(header)
        print("\n")
        
    if (dataset):
        explore_data(dataset, 0, 5, True)
        print_separator()