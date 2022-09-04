import mysql.connector
from mysql.connector import Error

try:    
    conexion = mysql.connector.connect(
        host ='localhost',
        port = 3306,
        user = 'root',
        password = '20473781',
        db = 'guitars'
    )
    
    if conexion.is_connected():
        print('Conexión exitosa')
        cursor = conexion.cursor() 
        cursor.execute('use guitars;')
        cursor.execute('insert into electric_guitar (model, color, num_string, brand) values ("Super_strat", "Green", 6, "Kiesel")')
        conexion.commit()
        print("data inserted correctly" )
except Error as ex:
    print('Error durante la conexion:', ex)
finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexión ha finalizado")