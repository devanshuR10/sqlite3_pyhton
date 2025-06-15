import sqlite3

conn=sqlite3.connect("hotel_data.db")
c=conn.cursor()
loc= input("\n\n\n\t\t\tENTER STATE  TO SEARCH HOTEL : ")
# sql = (f'''
#                  select * from hotel_info where hot_loc ='{loc}';
# ''')
# print(sql)
c.executescript(f"select * from hotel_info where hot_loc ='{loc}'")

result = c.fetchall()
print (result)

for i in range(0, len(result)):
    print(f'''


                            * HOTEL NUMBER  : {result[i][6]}
                            * HOTEL NAME    : {result[i][0]}
                            * HOTEL LOCATION: {result[i][1]}        
                            * ROOM TYPE     : {result[i][2]}
                            * BOOKING COST  : {result[i][3]}
                            * COST PER DAY  : {result[i][4]}
                            * HOTEL RATING  : {result[i][5]}



        ''')