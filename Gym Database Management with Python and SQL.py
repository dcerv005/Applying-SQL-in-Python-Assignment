from open_sql import connect_database
conn = connect_database()
#Question 1 TASK 1
def add_member(name, age, trainer_id):
  
    if conn is not None:
        
        try:
            #Query has the SQL logic to add values for a new member in the members table
            cursor=conn.cursor()
            query="INSERT INTO Members(name, age, trainer_id) VALUES(%s, %s, %s)"
            new_member = (name, age, trainer_id)
            cursor.execute(query, new_member)
            conn.commit()
            print('New Member Added.')
            
        except Exception as e:
            print(f'Error: {e}')

        finally:
            cursor.close()
            conn.close()



#Question 1 TASK 2
def add_workout_session(duration_minutes, calories_burn, date, member_id):
    if conn is not None:
        try:
            #Here we are adding a new workout session will all the parameters to fill in the table
            cursor=conn.cursor()
            new_workout_session = (duration_minutes, calories_burn, date, member_id)
            query = "INSERT INTO Workoutsessions (duration_minutes, calories_burn, date, member_id) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, new_workout_session)
            conn.commit()
            print('New workout Added')
        
        except Exception as e:
            print(f'Error: {e}')

        finally:
            cursor.close()
            conn.close()


#Question 1 Task 3
def updating_members(member_id, age):
    if conn is not None:
        try:
            cursor=conn.cursor()
            #This query is to update the age of a member. member id is required to know where exactly the change will be
            query = ' Update Members SET age= %s WHERE id = %s'
            cursor.execute(query, (age, member_id))
            conn.commit()
            print("Update age.")

        except Exception as e:
            print(f'Error: {e}')

        finally: 
            conn.close()
            cursor.close()


#Question 1 Task 4
def delete_workout_session(session_id):
    
    if conn is not None:
        try:
            #Here we are deleting a specific workout session so we need the id of the sessins that we are deleting so that we do not accidently delete other sessions.
            cursor=conn.cursor()
            query= 'DELETE FROM Workoutsessions WHERE id=%s'
            cursor.execute(query, (session_id, ))
            conn.commit()
            print("Session deleted")
        except Exception as e:
            print(f'Error: {e}')

        finally:
            conn.close()
            cursor.close()

#add_member('Ronald', 25, 2)
#add_workout_session(25, 75, '2024-04-18', 4)
#updating_members(8, 42)
#delete_workout_session(2)

