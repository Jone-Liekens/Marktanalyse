import psycopg2
 
# Connection parameters
host = "localhost"  # or the IP address of your database server
port = 5432         # default PostgreSQL port
database = "databasename"
user = "postgres"
password = "postgres"
 

def execute_sql(command, print_output = False):
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password,
            options="-c client_encoding=UTF8"
        )

        cur = conn.cursor()
        cur.execute(command)

        try:
            print("\n".join([x.name for x in cur.description]))


            rows = cur.fetchall()
            if print_output:
                for row in rows:
                    print(row)
        except:
            rows = []

        

        


        conn.commit()
        cur.close()
        conn.close()

        return rows
    
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)




def modify_database(sql_command): # sql_command is something like creating a new table, column, something like that
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password,
        )

        cur = conn.cursor()
        cur.execute(sql_command)
        conn.commit()
        cur.close()
        conn.close()

        return 0
    
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
