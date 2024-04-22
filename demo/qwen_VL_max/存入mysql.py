# import mysql.connector
# from datetime import datetime
#
# # 数据库连接信息
# host = "sh-cdb-grf2ge8a.sql.tencentcdb.com"
# user = "root"
# password = "a18670990886A"
# port = 63527
# database = "langchain_fc"  # 数据库名
# table_name = "bs_qa"  # 表名
#
#
# # 要插入的数据字典
# def write_mysql(text,i):
#     c=0
#     data_dict = {
#         "2": {
#             "question": text,
#             "answer": "Paris",
#             "up_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
#             "path_name": i
#         },
#     }
#
#     try:
#         conn = mysql.connector.connect(
#             host=host,
#             user=user,
#             password=password,
#             port=port,
#             database=database
#         )
#         if conn.is_connected():
#             print("成功连接到 MySQL 数据库")
#
#             # 创建游标对象
#             cursor = conn.cursor()
#
#             # 插入数据
#             for id_, record in data_dict.items():
#                 question = record.get("question", "")
#                 answer = record.get("answer", "")
#                 up_time = record.get("up_time", "")
#                 path_name = record.get("path_name", "")
#                 cursor.execute(f"INSERT INTO {table_name} (id, question, answer, up_time, path_name) VALUES (%s, %s, %s, %s, %s)",
#                                (id_, question, answer, up_time, path_name))
#
#             conn.commit()
#             print("数据插入成功")
#
#             cursor.close()
#             conn.close()
#             print("MySQL 连接已关闭")
#     except mysql.connector.Error as e:
#         print(f"连接到 MySQL 数据库失败：{e}")
#
# if __name__ == '__main__':
#     write_mysql(text='asvfasfasfasfasfsafsafsafsaf',i='asdas\dasdasf\asfsa\fsafsa')