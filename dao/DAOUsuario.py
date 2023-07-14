import pymysql

class DAOUsuario:
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="",db="smartnest" )

#    def read(self, id):
#        con = DAOUsuario.connect(self)
#        cursor = con.cursor()

#        try:
#            if id == None:
#                cursor.execute("SELECT * FROM curso order by nombre asc")
#            else:
#                cursor.execute("SELECT * FROM curso where id = %s order by nombre asc", (id,))
#            return cursor.fetchall()
#        except:
#            return ()
#        finally:
#            con.close()

    def insert(self,data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO usuario(name,email,username,password) VALUES(%s, %s, %s, %s)", (data['name'],data['email'],data['username'],data['password'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

#    def update(self, id, data):
#        con = DAOCurso.connect(self)
#        cursor = con.cursor()

#        try:
#            cursor.execute("UPDATE curso set nombre = %s, telefono = %s, email = %s where id = %s", (data['nombre'],data['telefono'],data['email'],id,))
#            con.commit()
#            return True
#        except:
#            con.rollback()
#            return False
#        finally:
#            con.close()

#    def delete(self, id):
#        con = DAOCurso.connect(self)
#        cursor = con.cursor()

#        try:
#            cursor.execute("DELETE FROM curso where id = %s", (id,))
#            con.commit()
#            return True
#        except:
#            con.rollback()
#            return False
#        finally:
#            con.close()
