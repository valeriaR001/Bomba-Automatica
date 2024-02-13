def GrabarFlujoYDistancia(flujo, distancia):
    import pymysql
    import datetime

    db = pymysql.connect(host='192.168.0.219', user='root', password='CPBraulio', db='ffgf', charset='utf8')
    ahorita = datetime.datetime.now()
    sql = f"INSERT INTO Datos (fecha, Flujo, Distancia) VALUES ('{ahorita}', {flujo}, {distancia});"
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    db.close()