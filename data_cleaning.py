# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    data_cleaning.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abaiao-r <abaiao-r@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 12:43:54 by abaiao-r          #+#    #+#              #
#    Updated: 2024/05/28 12:59:57 by abaiao-r         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils import *

# swap_columns() function: swaps the columns in a list of lists
# data: list of lists
# return: a new list of lists with the columns swapped
def swap_columns(data):
    swapped_data = []
    for row in data:
        swapped_data.append([row[1], row[0]])
    return swapped_data
