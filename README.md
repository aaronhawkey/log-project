# Log Analysis project

## About
This project was created as an assignment in the Full Stack Nanodegree program at Udacity.

This repository uses Python 2.7.12 to query data from a PSQL database. Psycopg2 is used to connect to the database and retrieve data. Results are displayed in a terminal window.

## Set Up
The linux based virtual machine used in this application was provided by Udcacity.

1. Download and install [Vagrant](https://www.vagrantup.com/)
2. Download and install Oracle's [Virtual Box](https://www.virtualbox.org/)
3. Download this git repository.
4. Download the database dump from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
5. In a terminal, navigate to the repository's directory.
6. Execute `$ vagrant up`
  * The default Udacity configuration file is provided.
7. Execute `$ vagrant ssh` to connect to the VM
8. Navigate to the `/vagrant` directory.
9. Load the data into the database by executing the following command: `psql -d news -f newsdata.sql`

## Execution
To compile the code and query the data, complete the following steps in the VM ssh.

1. `cd` into the project repository.
2. Execute: `$ python log_client.py`


## Views Used
In order for the code to function properly, you must create the view "daily_report". Use the query provided to create a view on your PSQL instance.

#### Daily Report View
```sql
CREATE VIEW daily_report AS

SELECT time::DATE AS date,
SUM (
    CASE WHEN status = '200 OK'
    THEN 1
    ELSE 0
    END) AS success,

SUM (
    CASE WHEN status  !=  '200 OK'
    THEN 1
    ELSE 0
    END) AS error
FROM log GROUP BY time::DATE;```

# Authors
Copyright 2018 -  Aaron J. Hawkey

Full Stack Nanodegree, Udcaity
