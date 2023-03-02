import mysql.connector  #this is needed to talk to sql, you might need to add from mysql setup

mydb = mysql.connector.connect(     #just for less typing
  host="localhost",       #connects you to the mysqlinstance i think
  user="root",
  password="root"
)

mycursor = mydb.cursor()   #just for less typing


mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase2")
mycursor.execute("CREATE DATABASE IF NOT EXISTS Shop")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

mycursor.execute("USE Shop")  #which database to use
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("CREATE TABLE IF NOT EXISTS product (productname VARCHAR(255), address VARCHAR(255))")

mycursor.execute("USE Electronics")  #needed if swapping bewteen databases as well
mycursor.execute("CREATE TABLE IF NOT EXISTS product (productname VARCHAR(255), address VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS name(productname VARCHAR(255), address VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS name2(productname VARCHAR(255) PRIMARY KEY, address VARCHAR(255))")
mycursor.execute('CREATE TABLE IF NOT EXISTS TEST(productname INT PRIMARY KEY AUTO_INCREMENT, address VARCHAR(255))')



sql = "INSERT INTO test (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute('INSERT INTO test (name, address) VALUES (\'Michelle\', \'Blue Village\')')
#mycursor.execute('INSERT INTO product (productname, address) VALUES (\'toaster2\', \'Canyon 123\')')
mycursor.execute("UPDATE product SET address = 'swaped' WHERE address = 'Canyon 123'")

mycursor.execute("DELETE FROM product WHERE NOT address = 'swaped'")

mydb.commit()  #this is needed to actually add the items to the table not used in sql direct but needed for the python connector
              # not sure if you need to do this individually for each write yet


              #doodling
#mycursor.execute('CREATE TABLE new_table AS SELECT * FROM   old_table');
#CREATE VIEW view_name AS SELECT address, name FROM test WHERE productname>10;
#Select * from view_name