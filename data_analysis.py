
from utils import *

# calculate_average_comments() function: calculates the average number of comments
# for a given list of posts
# posts: list of posts
# return: the average number of comments
def calculate_average_comments(posts):
    total_comments = 0
    for post in posts:
        total_comments += int(post[4])
    return total_comments / len(posts)

