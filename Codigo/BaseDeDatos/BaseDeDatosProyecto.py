def GrabarFlujoYDistancia(flujo, distancia):
    import pymysql
    import datetime

#En el host es la ip de tu raspberry y la contraseña tambien

    db = pymysql.connect(host='192.168.0.219', user='root', password='CPBraulio', db='AlmacenDeTemperaturas', charset='utf8')
    ahorita = datetime.datetime.now()
    sql = f"INSERT INTO Datos (fecha, temperatura, humedad) VALUES ('{ahorita}', {flujo}, {distancia});"
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    db.close()