import re
import pandas as pd
from http import HTTPStatus
import dashscope
import time
import pdfplumber
from PIL import Image
import os
import mysql.connector
from datetime import datetime

# 数据库连接信息
# host = "sh-cdb-grf2ge8a.sql.tencentcdb.com"
# user = "root"
# password = "a18670990886A"
# port = 63527
# database = "langchain_fc"  # 数据库名
# table_name = "bs_qa"  # 表名


# 要插入的数据字典
import mysql.connector
from datetime import datetime


# def write_mysql(text,i):
#     data_dict = {
#         1: {
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
#                 insert_query = f"INSERT INTO {table_name} (question, answer, up_time, path_name) VALUES (%s, %s, %s, %s)"
#                 current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#                 cursor.execute(insert_query, (text, "Paris", current_time, i))
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
#

def page_to_image(page):
    # 将PDF页面转换为PIL图像
    image = page.to_image(resolution=250)  # 可以设置分辨率
    return image



def pdf_to_images(pdf_file, output_folder):
    # 创建输出文件夹
    import os
    os.makedirs(output_folder, exist_ok=True)

    # 打开PDF文件
    with pdfplumber.open(pdf_file) as pdf:
        # 逐页读取并保存为图片
        for i, page in enumerate(pdf.pages):
            image = page_to_image(page)
            image.save(os.path.join(output_folder, f"page_{i + 1}.jpg"))


def simple_multimodal_conversation_call(list_jpg):
    # 读取每一个图片
    for i in list_jpg:
        if i==1:
            pass
        else:

            messages = [
                {
                    "role": "user",
                    "content":
                        [
                            {"image":fr"C:\Users\cao\Desktop\tupian\{i}"},
                            {
                                "text": "你现在是一个专业人员,把图片中的所有信息进行理解，然后以问题和答案的形式返回图中的知识点，问题和答案要求图片中的所有知识点都能覆盖到，格式是例子 问题：xxxx，答案：xxxxx 请按照格式化输出,注意版权归属和版权声明的内容都不要出现"},
                        ]
                }]
            response = dashscope.MultiModalConversation.call(model='qwen-vl-plus',
                                                             messages=messages,
                                                             api_key='sk-7939f5b192404940843cfc80226b906c')

            if response.status_code == HTTPStatus.OK:

                qa=response["output"]["choices"][0]["message"]["content"][0]["text"]
                # write_mysql(text=qa,i=i)
                print(qa+'\n'+i)
                print('-----------------------------------------------------')

            else:
                print(response.code)  # The error code.
                print(response.message)  # The error message.


if __name__ == '__main__':
    time1 = time.time()
    # 输入PDF文件路径和输出文件夹路径
    # pdf_file = r"C:\Users\cao\Desktop\Bosch Rexroth 焊接培训.pdf"
    # output_folder = r"C:\Users\cao\Desktop\tupian"
    # # 获取所有的地址，
    list_jpg = os.listdir(r"C:\Users\cao\Desktop\tupian")
    # 定义一个函数，用来提取文件名中的数字部分
    def extract_number(filename):
        return int(filename.split('_')[1].split('.')[0])
    # 使用自定义的排序键对列表进行排序
    list_jpg.sort(key=extract_number)

    # 将PDF转换为图像
    # pdf_to_images(pdf_file, output_folder)

    #总结图片中的QA并且返回list_jpg
    simple_multimodal_conversation_call(list_jpg)


    time2=time.time()
    print(f'总耗时{time2-time1}')
