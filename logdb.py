# Aaron Hawkey
# logdb.py
# Log Analysis Project
# Udacity Full Stack Nanodegree
# 7/27/2018
#
# This module querys log data from the "news" database. It also prints logged
# data utilizing the query functions defined in this module. psycopg2 is
# utilized to query on the PSQL database. The constant "DBNAME" is defined in
# begining of the module. If there is a different database name it needs to
# connect to, redefine the "DBNAME" constant.


import psycopg2


DBNAME = "news"


# Queries top 3 articles. Returns a list.
def get_top_3_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""SELECT articles.title, count(*) AS visits
        FROM articles JOIN log ON log.path
        LIKE CONCAT('%', articles.slug, '%')
        WHERE log.status LIKE '%200%' GROUP BY
        articles.title, log.path ORDER BY visits DESC LIMIT 3""")
    top_3_articles = c.fetchall()
    db.close()
    return top_3_articles


# Queries top 3 authors. Returns a list.
def get_top_3_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""SELECT name, author, COUNT(path) AS visits
        FROM articles, log, authors
        WHERE log.path = CONCAT('/article/', articles.slug)
        AND articles.author = authors.id
        GROUP BY name, author
        ORDER BY visits DESC LIMIT 3""")
    top_3_authors = c.fetchall()
    db.close()
    return top_3_authors


# Queries failed traffice >2%. Returns a list.
def get_failed_traffic():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""SELECT agg.*
    FROM(
            SELECT date, ((CAST(error AS float) /
            CAST(success + error AS float)) *100)
            AS error_percentage FROM daily_report
            ORDER BY error_percentage DESC
        ) agg
        WHERE error_percentage > 1""")
    failed_traffic = c.fetchall()
    db.close()
    return failed_traffic


# Executes query for top 3 articles and prints results to terminal.
def print_top_3_articles():
    top_3_articles = get_top_3_articles()

    print("Top 3 Articles:")

    print("1. " + top_3_articles[0][0] + " - " + str(top_3_articles[0][1]) +
          " Total Views")

    print("2. " + top_3_articles[1][0] + " - " + str(top_3_articles[1][1]) +
          " Total Views")

    print("3. " + top_3_articles[2][0] + " - " + str(top_3_articles[2][1]) +
          " Total Views")

    print("\n")


# Executes query for top 3 authors and prints results to terminal.
def print_top_3_authors():
    top_3_authors = get_top_3_authors()
    print("Top 3 Authors:")

    print("1. " + top_3_authors[0][0] + " - " + str(top_3_authors[0][2]) +
          " Total Views")

    print("2. " + top_3_authors[1][0] + " - " + str(top_3_authors[1][2]) +
          " Total Views")

    print("3. " + top_3_authors[2][0] + " - " + str(top_3_authors[2][2]) +
          " Total Views")

    print("\n")


# Executes query for failed traffic and prints results to terminal.
def print_failed_traffic():
    failed_traffic = get_failed_traffic()
    print("Percent of traffic failed:")
    for x in failed_traffic:
        print(str(failed_traffic.index(x) + 1) + ". " + str(x[0]) + " - " +
              str(round(x[1], 3)) + "% Error")

    print("\n")
