import mysql.connector
from sshtunnel import SSHTunnelForwarder
import datetime
import keyboard


def get_now_time():
    now = datetime.datetime.now()
    time_str = now.strftime("%Y-%m-%d %H:%M:%S")

    return time_str

def create_values(table_name, values, *cols):

    for col in cols:
        split_col = col.split(",")
        num_split_col = len(split_col)
        str_d = ""

        for i in range(1, num_split_col+1):
            if i <num_split_col:
                str_d += "%s,"
            else:
                str_d += "%s"

        sql = f"INSERT INTO {table_name}  ({col}) VALUES ({str_d})"

        value_list = values.split(",")
        sql_values = []

        for value in value_list:
            sql_values.append(value)
            sql_values_tuple = tuple(sql_values)

    cursor.execute(sql, sql_values)
    cnx.commit()

def delete_values(table_name,condition):
    table_name = table_name
    condition = condition
    sql = f"DELETE FROM {table_name} WHERE {condition}"

    cursor.execute(sql)
    cnx.commit()


now = datetime.datetime.now()
time_str = now.strftime("%Y-%m-%d %H:%M:%S")
print("現在時間：")
print(time_str)
# 建立資料庫連線
cnx = mysql.connector.connect(host="10.51.204.48", user="root", password="", database="mercury")


# 建立游標
cursor = cnx.cursor()
driving_num = ["GHI123"]
rTime = ["2015-02-11 16:28:02"]
yawn_vio = "打哈欠"
# 執行SQL語句
# sql = "INSERT INTO table_name (column1, column2, ...) VALUES (%s, %s, ...)"
# values = ("value1", "value2", ...)
# cursor.execute(sql, values)
#
# sql = "DELETE FROM users WHERE userid=3"
# cursor.execute(sql)

#-------create values----------
# now_time = get_now_time()
create_values("violation",f"{time_str},{rTime[0]},{driving_num[0]},{yawn_vio}", "vTime ,rTime, Number, Event")
#-------delete values----------
# delete_values("violation", "Number=111111")


cursor.execute("SELECT * FROM record WHERE Number = 'GHI123'")
#
#
results = cursor.fetchall()
print(results)
for row in results:
    print(row)


