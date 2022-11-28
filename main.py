import psycopg2
from config import host, user, password, db_name, port, cur, conn
#host = 'localhost'
#user = 'postgres'
#password = 'aboba1488'
#db_name = 'test2'
#port = 5432
#conn = None
#cur = None

try:
    conn = psycopg2.connect(
        host=host,
        dbname=db_name,
        user=user,
        password=password,
        port=port
    )
    cur = conn.cursor()

    #create_script = ''' CREATE TABLE IF NOT EXISTS employee (
        #id int PRIMARY KEY,
        #name varchar(40) NOT NULL,
        #salary int,
        #dept_id varchar(30)
    #)'''
    #cur.execute(create_script)

    #insert_script = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
    #insert_value = [(1, 'James', 12000, 'D1'), (2, 'Karl', 88000, 'D1')]
    #for record in insert_value:
        #cur.execute(insert_script, record)

    cur.execute('SELECT * FROM cars')
    for record in cur.fetchall():
        print(record)

    #cur.execute('SELECT * FROM employee')
    #for record in cur.fetchall():
        #print(record[1])

    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()