# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    data_extraction.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abaiao-r <abaiao-r@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/27 19:51:08 by abaiao-r          #+#    #+#              #
#    Updated: 2024/05/28 12:50:48 by abaiao-r         ###   ########.fr        #
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
    
# extract_post_types() function: splits the dataset into "Ask HN" posts, 
# "Show HN" posts, and other posts
# hn: list of lists with the dataset
# return: the "Ask HN" posts, "Show HN" posts, and other posts as lists of lists
def extract_post_types(hn):
    ask_posts = []
    show_posts = []
    other_posts = []

    for post in hn:
        title = post[1].lower()
        if title.startswith("ask hn"):
            ask_posts.append(post)
        elif title.startswith("show hn"):
            show_posts.append(post)
        else:
            other_posts.append(post)

    return ask_posts, show_posts, other_posts

# extract_results_list(posts) function: extracts the created_at and num_comments
# columns from the "Ask HN" posts
# posts: list of lists with the "Ask HN" posts
# return: a list of lists with the created_at and num_comments columns
def extract_results_list(posts):
    results_list = []
    
    for post in posts:
        created_at = post[6]
        num_comments = int(post[4])
        results_list.append([created_at, num_comments])
    return (results_list)
