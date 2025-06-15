import sqlite3

conn=sqlite3.connect("hotel_data.db")
c=conn.cursor()


def view_avalable_hotel():
    sql = '''
        SELECT * FROM hotel_info
        '''
    c.execute(sql)

    result = c.fetchall()

    if len(result)>0:
        for i in range(0,len(result)):
         print(f'''
              
              
              * HOTEL NUMBER  : {result[i][6]}
              * HOTEL NAME    : {result[i][0]}
              * HOTEL LOCATION: {result[i][1]}        
              * ROOM TYPE     : {result[i][2]}
              * BOOKING COST  : {result[i][3]}
              * COST PER DAY  : {result[i][4]}
              * HOTEL RATING  : {result[i][5]}
              
        
        
        ''')
    else:
        print("\n\n\n\t\t\tNO HOTEL TO SHOW .........")

def search_hotel():


    print('''

             1.to search by hotel number

             2.to search  by hotel location

             3.to search by price

             4.to search by rating 


    ''')
    choice=int(input("\n\n\n\t\t\tENTER YOUR CHOICE : "))
    if choice==1:
        number=input("\n\n\n\t\t\tENTER HOTEL NUMBER TO SEARCH : ")

        sql=f'''
          select * from hotel_info where hotel_no ={number} 
        
        
        '''
        c.execute(sql)

        result = c.fetchall()


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


    elif choice==2:
        loc= input("\n\n\n\t\t\tENTER STATE  TO SEARCH HOTEL : ")

        sql = (f'''
                 select * from hotel_info where hot_loc ='{loc}';


               ''')

        c.execute(sql)

        result = c.fetchall()


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
    elif choice==3:
        price = input("\n\n\n\t\t\tENTER COST TO SEARCH HOTEL : ")

        sql = f'''
                         select * from hotel_info where cost_perday ={price} 


                       '''
        c.execute(sql)

        result = c.fetchall()


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
    elif choice==4:
        rating= input("\n\n\n\t\t\tENTER   RATING  TO SEARCH HOTEL (OUT OF 10) : ")

        sql = f'''
                         select * from hotel_info where hotel_rating ={rating} 


                       '''
        c.execute(sql)

        result = c.fetchall()


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
    else:
        print("\n\n\n\t\t\t\tINVALID INPUT.......")
#by name by location by price by hotel rating
def add_hotel():
    name=input("\n\n\n\t\t\tENTER NAME OF HOTEL :")
    loc=input("\n\n\n\t\t\tENTER THE LOCATION OF HOTEL:")
    room_type=input("\n\n\n\t\t\tENTER THE ROOM TYPE:")
    booking_cost=int(input("\n\n\n\t\t\tENTER THE BOOKING COST:"))
    daycost=int(input("\n\n\n\t\t\tENTER THE  PER/DAY COST :"))
    hotel_rating=int(input("\n\n\n\t\t\tENTER HOTEL RATING OUT OF 10:"))

    sql=f'''
       insert into hotel_info ('hot_name','hot_loc','room_type','booking_cost','cost_perday','hotel_rating') values
       ('{name}','{loc}','{room_type}','{booking_cost}','{daycost}','{hotel_rating}')
    
    
    '''
    c.executescript(sql)
    conn.commit()
    print("\n\n\t\t\n\t\tHOTEL ADDED........")


def remove_hotel():
    view_avalable_hotel()
    hotel_number=int(input("\n\n\n\t\t\tENTER HOTEL NUMBER TO REMOVE:"))

    sql=f'''
       DELETE FROM hotel_info WHERE hotel_no ={hotel_number}
    
    '''

    c.executescript(sql)
    conn.commit()
    print(f"\n\n\n\t\t\t HOTEL NUMBER {hotel_number} REMOVED")
def book_hotel():
    sql = '''
           SELECT * FROM hotel_info
           '''
    c.execute(sql)

    result = c.fetchall()
    print(len(result))

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

    pname=input("\n\n\n\t\t\tENTER YOUR NAME:")
    pphone=int(input("\n\n\n\t\t\tENTER YOUR PHONE NUMBER:"))
    id=input("\n\n\n\t\t\tENTER YOUR AADHAR CARD NO:")
    hotel_no=input("\n\n\n\t\t\tENTER HOTEL NUMBER YOU WANT TO BOOK:")
    no_of_days=int(input("\n\n\n\t\t\tENTER NUMBER OF DAYS YOU WANT TO STAY:"))
    #fetch cost from hotel_info using hotel_number and print net cost

    sql = f'''
        select * from hotel_info where hotel_no ={hotel_no}
        '''
    c.execute(sql)

    result=c.fetchall()

    cost=result[0][4]
    booking_cost=result[0][3]
    total=booking_cost+(cost*no_of_days) #final charges
    name_hotel=result[0][0]

    print(f"\n\n\n\n\t\t\tHOTEL COST={cost}")
    print(f"\n\n\n\t\t\tHOTEL BOOKING COST={booking_cost}")
    print(f"\n\n\n\t\t\tTOTAL COST FOR {no_of_days} DAYS ={total}")

    sql=f'''
        insert into book_hotel('Pname','phone_no','id_proof','hotel_name','nodays','amount_paid','hotel_no') values
        ('{pname}','{pphone}','{id}','{name_hotel}','{no_of_days}','{total}','{hotel_no}')
    
     '''
    c.executescript(sql)
    conn.commit()

    print("\n\n\n\t\t\tHOTEL BOOKED...........")
while(True):
    print('''
            ___________HOTEL MANAGEMENT SYSTEM_______
            *                                       *
            *          1. VIEW AVAILABLE HOTEL      *
            *                                       *
            *          2. SEARCH HOTEL              *
            *                                       *
            *          3. ADD HOTEL                 *
            *                                       *
            *          4. REMOVE HOTEL              *
            *                                       *
            *          5. BOOK HOTEL                *
            * * * * * * * * * * * * * * * * * * * * *             
    
    
    ''')
    choice=int(input("\n\n\n\t\t\t\tENTER YOUR CHOICE :"))

    if choice==1:
        view_avalable_hotel()
    elif choice==2:
        search_hotel()
    elif choice==3:
        add_hotel()
    elif choice==4:
        remove_hotel()
    elif choice==5:
        book_hotel()
    else:
        print("\n\n\n\t\t\t\tINVALID INPUT PLEASE TRY AGAIN.............")
