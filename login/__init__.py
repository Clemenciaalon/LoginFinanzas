import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = '172.31.113.125\DGIPRESUPUESTO'
database = 'dbTransparencia'
user = 'usrpresupuestot'
pwd = 'Transpar3nc1@?20'
try:
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server+';DATABASE='+database+';UID='+user+';PWD='+pwd)
except Exception as e:
    print("Error Login (local): ", e)
    cnxn = False


def validation(user, pwd):
    try:
        if cnxn != False:
            with cnxn.cursor() as cursor:
                query = """
                    SELECT 
                        Id, 
                        Rol 
                    from 
                        dbo.Usuarios 
                    where 
                        usName = '%s' 
                        and 
                        pwd='%s'"""
                cursor.execute(query % (user, pwd))
                data = cursor.fetchall()
                misDatos = []
                contenido = {}
                for elemento in data:
                    contenido = {
                        'Id': elemento[0],
                        'Rol': elemento[1]
                    }
                    misDatos.append(contenido)
                    contenido = {}
            return misDatos
        else:
            return 'Error'
    except Exception as e:
        print('Error DB: ', e)
        return 'Error'
