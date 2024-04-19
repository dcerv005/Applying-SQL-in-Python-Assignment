from open_sql import connect_database
conn = connect_database()
#Question 2
#Task 1
def list_distinct_trainers():
    if conn is not None:
        try:
            cursor=conn.cursor()
            #We are using 'DISTINCT' to find the unique trainers that are in the Members table
            query = "SELECT DISTINCT trainer_id FROM Members"
            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)
        except Exception as e:
            print(f'Error: {e}')

        finally:
            conn.close()
            cursor.close()

#Task 2
def count_members_per_trainer():
    if conn is not None:
        try:
            cursor=conn.cursor()
            #Here we are grouping by trainers the amount of members each trainer has.
            query= 'SELECT COUNT(id), trainer_id FROM Members GROUP BY trainer_id'
            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)
        except Exception as e:
            print(f'Error: {e}')
        finally:
            conn.close()
            cursor.close()

#Task 3
def get_members_in_age_range(start_age, end_age):
    if conn is not None:
        try:
            cursor=conn.cursor()
            #We are displaying the members from the table that are between certain ages.
            query = 'SELECT * FROM Members WHERE age BETWEEN %s AND %s'
            cursor.execute(query, (start_age, end_age))
            for row in cursor.fetchall():
                print(row)
        except Exception as e:
            print(f'Error: {e}')
        finally:
            conn.close()
            cursor.close()
#list_distinct_trainers()
#count_members_per_trainer()
get_members_in_age_range(20, 42)