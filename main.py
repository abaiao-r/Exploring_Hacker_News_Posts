# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abaiao-r <abaiao-r@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/27 19:14:44 by abaiao-r          #+#    #+#              #
#    Updated: 2024/05/27 20:36:18 by abaiao-r         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# # Analysis of Ask HN and Show HN Posts on Hacker News

# ## Introduction

# Hacker News is a popular platform within the technology and startup 
# communities where users submit posts to share news, ask questions, or showcase 
# projects. This project involves analyzing a dataset of Hacker News posts to 
# answer two primary questions:

# 1. Do "Ask HN" or "Show HN" posts receive more comments on average?
# 2. Do posts created at a certain time receive more comments on average?

# The dataset provided has been filtered to include only posts that received 
# comments, reducing the original dataset from nearly 300,000 rows to 
# approximately 20,000 rows. The columns in the dataset include:

# - `id`: The unique identifier for each post.
# - `title`: The title of the post.
# - `url`: The URL the post links to, if applicable.
# - `num_points`: The number of points the post acquired, calculated as upvotes 
# minus downvotes.
# - `num_comments`: The number of comments on the post.
# - `author`: The username of the person who submitted the post.
# - `created_at`: The date and time of the post's submission.

# We will use Python to analyze this data, focusing on string manipulation, 
# object-oriented programming, and date and time operations to gain insights 
# into user engagement on Hacker News.

# ## Importing Libraries and Reading the Dataset

# Let's start by importing the necessary libraries and reading the dataset into 
# a list of lists.

from data_extraction import *

# File path for the dataset
hacker_news_csv = "hacker_news.csv"

# Extracting the dataset and its header
hn, headers = extract_csv(hacker_news_csv, True)


# print the header and the first 5 rows of the dataset to check if the 
#extraction was successful
print (headers, "\n")
print_dataset_slice(hn, 0, 5, True)
print_separator()




