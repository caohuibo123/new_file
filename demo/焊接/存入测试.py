import mysql.connector
import json

# 数据库连接信息
host = "sh-cdb-grf2ge8a.sql.tencentcdb.com"
user = "root"
password = "a18670990886A"
port = 63527
database = "langchain_fc"  # 数据库名
table_name = "bs_qa"  # 表名

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS my_table (
            id VARCHAR(255) PRIMARY KEY,
            data JSON
        )
    """)
    conn.commit()
    cursor.close()

def insert_data(conn, data_dict):
    cursor = conn.cursor()
    for id_, data in data_dict.items():
        # 将数据转换为 JSON 格式
        json_data = json.dumps(data)
        cursor.execute("INSERT INTO my_table (id, data) VALUES (%s, %s)", (id_, json_data))
    conn.commit()
    cursor.close()

try:
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        port=port,
        database=database,
        # table_name=table_name
    )
    if conn.is_connected():
        cursor = conn.cursor()

        print("连接到数据库")

        # 创建表
        # create_table(conn)

        # # 查询有哪个些表
        # cursor.execute("SHOW TABLES")
        # # 获取表名
        # tables = cursor.fetchall()
        # # 打印表名
        # print("数据库中的表：")
        # for table in tables:
        #     print(table[0])



        # 插入数据
        # insert_data(conn, data_dict)
        # print("数据存入成功")


        # 获取表的结构信息
        # cursor.execute(f"DESCRIBE {table_name}")
        # columns = cursor.fetchall()
        # # 打印表的结构信息
        # print(f"表 {table_name} 的结构：")
        # for column in columns:
        #     print(column)


        #
        # for i in range(1020,1022):
        #     # 根据 ID 删除数据
        #     cursor.execute("DELETE FROM bs_qa WHERE id = %s", (i,))
        #     conn.commit()
        #     print("数据删除成功")

        # 获取查询结果，  打印查询结果
        cursor.execute("SELECT * FROM bs_qa")
        rows = cursor.fetchall()
        print("ba_qa 表中的数据：")
        for row in rows:
            print(row)

        #关闭数据库
        # conn.close()
        print("MySQL执行完毕")
except mysql.connector.Error as e:
    print(f"连接到 MySQL 数据库失败：{e}")
