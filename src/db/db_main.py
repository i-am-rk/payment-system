import sqlite3

con = sqlite3.connect('pa_db.db')

c = con.cursor()
########################################
#region SCHEMAS
# c.execute('''CREATE TABLE Client(
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     first_name text not null,
#     last_name text not null,
#     gender TEXT NOT NULL,
#     dob TEXT NOT NULL,
#     email TEXT NOT NULL UNIQUE,
#     mobile_num TEXT NOT NULL UNIQUE,
#     balance INTEGER NOT NULL DEFAULT 0,
#     check(gender in ('M', 'F', 'NA')),
#     check(GLOB('[0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', mobile_num))
#     check(GLOB('[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]', dob))
# )''')

# c.execute('''
# create table Vehicle(
#     id integer not null primary key autoincrement unique,
#     type text not null,
#     number_plate text not null,
#     owner_id integer not null,
#     foreign key(owner_id) references Client(id)
# )
# ''')
# c.execute('''
# create table Parking_lots(
#     id integer not null primary key autoincrement unique,
#     type text not null,
#     in_use integer not null default 0,
#     session integer,
#     foreign key(session) references Session(id) on delete set null
# )
# ''')
# c.execute('''
# create table Session(
#     id integer not null primary key autoincrement unique,
#     vehicle_id integer not null,
#     parking_lot integer not null,
#     owner_id integer not null,
#     start_date text not null,
#     start_time text not null,
#     foreign key(vehicle_id) references Vehicle(id) on delete cascade,
#     foreign key(parking_lot) references Parking_lots(id) on delete cascade,
#     foreign key(owner_id) references Client(id) on delete cascade
# )
# ''')
#endregion SCHEMAS
#################################################

#####################################################################
#region INSERT Clients
# c.execute('''insert into Client(first_name, last_name, gender, dob, email, mobile_num, balance)
#     values
#     ('Mario', 'speedwagon', 'M', '1999-02-03', 'mariospeed@gmail.com', '10-7020301020', 100),
#     ('Petey', 'Cruiser', 'F', '1999-02-03', 'peteycruiser@gmail.com', '11-7020301020', 200),
#     ('Anna', 'sthesia', 'F', '1999-02-03', 'annasthensia@gmail.com', '13-7020301020', 150),
#     ('Paul', 'molive', 'M', '1999-02-03', 'paulmolive@gmail.com', '14-7020301020', 400),
#     ('Anna', 'mull', 'F', '1999-02-03', 'annamull@gmail.com', '15-7020301020', 300),
#     ('Gail', 'forewind', 'M', '1999-02-03', 'gailforewind@gmail.com', '16-7020301020', 500),
#     ('Paige', 'turner', 'F', '1999-02-03', 'paigeturner@gmail.com', '17-7020301020', 600)
# ''')
#endregion INSERT Clients
#################################################################

# for row in c.execute('''select * FROM Client c where id = (select c2.id from Client c2 where c2.id = c.id)'''):
#     print(row)
for row in c.execute('''select * from Client'''):
    print(row)
# c.execute('''drop table Client''')
print("test")
con.commit()
con.close()