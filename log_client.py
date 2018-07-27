# Aaron Hawkey 
# log_client.py
# Log Analysis Project
# Udacity Full Stack Nanodegree
# 7/27/2018
#
# This is the client that executes the print commands from logdb.py. This is the
# executable of the program. log_client.py will retrieve the top 3 articles and
# authors, and days where failed traffic exceeded 2%. All data is printed to the
# terminal.

import logdb

print("\n")

logdb.print_top_3_articles()
logdb.print_top_3_authors()
logdb.print_failed_traffic()
