import Adafruit_DHT as dht
import datetime
import time
import urllib.request
import pymysql

sensor = dht.DHT11
pin = 21
print('Reading Temperature&Humidity')
conn = pymysql.connect(host='210.119.12.52',user='test_usr',password='mysql_p@ssw0rd',\
                        db='shopdb',charset='utf8')
try:
    while True:
        wtime = datetime.datetime.now()
        humid,temp = dht.read_retry(sensor,pin) 
        if humid is not None and temp is not None:
            print(wtime,"Temp={0:0.1f}C Humidity = {1:0.1f}%".format(temp,humid)) 
            curs = conn.cursor()
            query = """INSERT INTO shopdb.iotmachine (currents_time,machine_id,temperature,humidity) 
                    VALUES(%s, %s, %s, %s) """
            data = (wtime.strftime("%Y-%m-%d %H:%M:%S"),'YYJ',temp,humid)
            curs.execute(query,data)
            conn.commit()

            time.sleep(10)
        else:
            print("Failed to get readming. Try again")

        time.sleep(1)

#except KeyboardInterrupt:
#    print("Terminated by Keyboard")

finally:
    #print("End of program")
    curs.close()
    conn.close()