import mysql.connector
from config import USER, PASSWORD, HOST


class dbConnectError(Exception):
    pass


def connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


def get_all_people():
    people = []
    db_name = 'PQ'
    db_connection = connect_to_db(db_name)
    cur = db_connection.cursor()
    print("Connected to DB: %s" % db_name)

    query = """
        SELECT ID, Forename, Surname, Age, Profession FROM people
        """
    cur.execute(query)
    for (ID, Forename, Surname, Age, Profession) in cur:
        people.append(
            {'ID': ID,
             'Forename': Forename,
             'Surname': Surname,
             'Age': Age,
             'Profession': Profession
            }
        )

    return people


def search_person(id):
    db_name = 'PQ'
    db_connection = connect_to_db(db_name)
    cur = db_connection.cursor()
    query = """
    SELECT ID, Forename, Surname, Age, Profession FROM people
    WHERE ID = {}
    """.format(id)
    cur.execute(query)
    for (ID, Forename, Surname, Age, Profession) in cur:
        person = {'ID': ID,
             'Forename': Forename,
             'Surname': Surname,
             'Age': Age,
             'Profession': Profession
             }

    return person


def add_person(newperson):
    db_name = 'PQ'
    db_connection = connect_to_db(db_name)
    cur = db_connection.cursor()
    query = """INSERT INTO people (Forename, Surname, Age, Profession) VALUES ('{}', '{}', '{}', '{}')""".format(
        newperson['Forename'],
        newperson['Surname'],
        newperson['Age'],
        newperson['Profession'],
    )
    print(query)
    cur.execute(query)
    db_connection.commit()
    return cur.lastrowid
    cur.close()
    
    
def delete_person(id):
    db_name = 'PQ'
    db_connection = connect_to_db(db_name)
    cur = db_connection.cursor()
    query = """DELETE FROM people WHERE ID = {}""".format(id)
    cur.execute(query)
    db_connection.commit()
    print(cur.rowcount, "record(s) deleted")
