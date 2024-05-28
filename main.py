# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abaiao-r <abaiao-r@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/27 19:14:44 by abaiao-r          #+#    #+#              #
#    Updated: 2024/05/28 13:00:11 by abaiao-r         ###   ########.fr        #
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
from data_cleaning import *
from data_analysis import *
from utils import *
from datetime import datetime as dt

# File path for the dataset
hacker_news_csv = "hacker_news.csv"

# Extracting the dataset and its header
hn, headers = extract_csv(hacker_news_csv, True)


# print the header and the first 5 rows of the dataset to check if the 
#extraction was successful
print (headers, "\n")
print_dataset_slice(hn, 0, 5, True)
print_separator()


# ## Extracting Ask HN and Show HN Posts

# We will now extract the "Ask HN" and "Show HN" posts from the dataset to
# analyze them separately. We will also identify the number of posts in each
# category.

# Lists to store the "Ask HN" and "Show HN" posts and other posts
ask_posts, show_posts, other_posts = extract_post_types(hn)

# Check the number of "Ask HN" and "Show HN" posts and other posts
print("Number of Ask HN posts:", len(ask_posts))
print("Number of Show HN posts:", len(show_posts))
print("Number of other posts:", len(other_posts))
print_separator()

# ## Calculating the Average Number of Comments for Ask HN and Show HN Posts

# We will now calculate the average number of comments for "Ask HN" and "Show HN"
# posts to determine which type of post receives more comments on average.

# Calculate the average number of comments for "Ask HN" and "Show HN" posts
avg_ask_comments = calculate_average_comments(ask_posts)
print("Average number of comments for Ask HN posts:", avg_ask_comments)

avg_show_comments = calculate_average_comments(show_posts)
print("Average number of comments for Show HN posts:", avg_show_comments)
print_separator()

# (1) Do show posts or ask posts receive more comments on average?
# The average number of comments for "Ask HN" posts is approximately 14.04, while
# the average number of comments for "Show HN" posts is approximately 10.32.
# Therefore, "Ask HN" posts receive more comments on average compared to "Show HN"
# posts.

# ## Analyzing the Number of Comments by Hour

# Next, we will analyze the number of comments for "Ask HN" posts by hour to
# determine if posts created at a certain time receive more comments on average.
# We will follow these steps:

# 1. Calculate the number of "Ask HN" posts created in each hour of the day, along
# with the number of comments received.
# 2. Calculate the average number of comments "Ask HN" posts receive by hour created.


# List to store the created_at and num_comments columns from the "Ask HN" posts
results_list = extract_results_list(ask_posts)


# Creating dictionaries to store the number of posts and comments by hour
counts_by_hour, comments_by_hour= parse_coments_by_hour(results_list)

# Calculating the average number of comments per post by hour
avg_by_hour = average_comments_per_post_by_hour(counts_by_hour, comments_by_hour)

print("Average number of comments per post by hour:\n")
print_dataset_slice(avg_by_hour, 0, len(avg_by_hour), False)
print_separator()


# Swap the columns in the avg_by_hour list of lists
swap_avg_by_hour = swap_columns(avg_by_hour)

print("Swapped columns in the avg_by_hour list of lists:\n")
print_dataset_slice(swap_avg_by_hour, 0, len(swap_avg_by_hour), False)
print_separator()

# Sort the swap_avg_by_hour list of lists in descending order
sorted_swap = sorted(swap_avg_by_hour, reverse=True)
print("Top 5 Hours for Ask Posts Comments:\n")
for avg, hour in sorted_swap[:5]:
    print(
        "{}: {:.2f} average comments per post".format(
            dt.strptime(hour, "%H").strftime("%H:%M"), avg
        )
    )
print_separator()

# ## Conclusion

# In this project, we analyzed a dataset of Hacker News posts to determine which
# type of post and time receive more comments on average. We found that "Ask HN"
# posts receive more comments on average compared to "Show HN" posts. Additionally,
# we discovered that posts created between 15:00 and 16:00 (3:00 pm - 4:00 pm EST)
# receive the most comments on average.
