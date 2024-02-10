def GrabarFlujoYDistancia(flujo, distancia):
    import pymysql
    import datetime

    db = pymysql.connect(host='192.168.100.129', user='root', password='N0s3w3y', db='AlmacenDeTemperaturas', charset='utf8')
    ahorita = datetime.datetime.now()
    sql = f"INSERT INTO Datos (fecha, temperatura, humedad) VALUES ('{ahorita}', {flujo}, {distancia});"
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    db.close()