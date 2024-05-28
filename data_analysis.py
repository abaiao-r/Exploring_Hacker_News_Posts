
from utils import *
from datetime import datetime as dt

# calculate_average_comments() function: calculates the average number of comments
# for a given list of posts
# posts: list of posts
# return: the average number of comments
def calculate_average_comments(posts):
    total_comments = 0
    for post in posts:
        total_comments += int(post[4])
    return total_comments / len(posts)

# parse_coments_by_hour() function: parses the date and time and calculates the
# number of posts and comments by hour
# results_list: list of lists with the created_at and num_comments columns
# return: dictionaries with the number of posts and comments by hour
def parse_coments_by_hour(results_list):
    counts_by_hour = {}
    comments_by_hour = {}
    
    for result in results_list:
        date_str = result[0]
        num_comments = result[1]
        date_dt = dt.strptime(date_str, "%m/%d/%Y %H:%M")
        hour = date_dt.strftime("%H")
        if hour not in counts_by_hour:
            counts_by_hour[hour] = 1
            comments_by_hour[hour] = num_comments
        else:
            counts_by_hour[hour] += 1
            comments_by_hour[hour] += num_comments
    
    return (counts_by_hour, comments_by_hour)
            
# average number of comments per post by hour function: calculates the average
# number of comments per post by hour
# counts_by_hour: dictionary with the number of posts by hour
# comments_by_hour: dictionary with the number of comments by hour
# return: a list of lists with the average number of comments per post by hour
def average_comments_per_post_by_hour(counts_by_hour, comments_by_hour):
    avg_by_hour = []
    
    for hour in counts_by_hour:
        avg_by_hour.append([hour, comments_by_hour[hour] / counts_by_hour[hour]])
    
    return (avg_by_hour)

