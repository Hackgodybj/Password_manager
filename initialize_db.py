import pymysql
import os.path

def init_db():
    check_file=os.path.join(os.path.abspath(os.path.dirname(__file__)),"mysqlcredentials.txt")
    f=open(check_file,"r")
    output=[i.strip("\n") for i in f.readlines()]
    con = pymysql.connect(host=output[0],port=int(output[1]), user=output[2], passwd=output[3])
    cursor = con.cursor()

    # create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS password_database")
    con.commit()

    # create user table
    query = """
    CREATE TABLE IF NOT EXISTS password_database.user
    (
        Username VARCHAR(30) NOT NULL,
        Password VARCHAR(64) NOT NULL,
        Country_of_origin VARCHAR(30) NOT NULL,
        id INT(10) PRIMARY KEY AUTO_INCREMENT,
        salt VARCHAR(100) NOT NULL,
        iv char(77) NOT NULL,
        key_salt VARCHAR(32) NOT NULL
    )
    """
    cursor.execute(query)
    con.commit()
    con.close()
