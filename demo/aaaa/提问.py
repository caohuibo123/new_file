import re
import pandas as pd
from http import HTTPStatus
import dashscope
import time
import pdfplumber
from PIL import Image
import os

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

        messages = [
            {
                "role": "user",
                "content":
                    [
                        {"image":fr"C:\Users\cao\Desktop\tupian\{i}"},
                        {
                            "text": "你现在是一个软件人员,把图片中的所有信息进行理解，给出详细的使用教程"},
                    ]
            }]
        response = dashscope.MultiModalConversation.call(model='qwen-vl-max',
                                                         messages=messages,
                                                         api_key='sk-7939f5b192404940843cfc80226b906c')

        if response.status_code == HTTPStatus.OK:

            qa=response["output"]["choices"][0]["message"]["content"][0]["text"]
            print(qa+i)

        else:
            print(response.code)  # The error code.
            print(response.message)  # The error message.



if __name__ == '__main__':
    time1 = time.time()
    # 输入PDF文件路径和输出文件夹路径
    pdf_file = r"C:\Users\cao\Desktop\Bosch Rexroth 焊接培训.pdf"
    output_folder = r"C:\Users\cao\Desktop\tupian"

    # 获取所有的地址，
    list_jpg = os.listdir(r"C:\Users\cao\Desktop\tupian")


    # 将PDF转换为图像
    # pdf_to_images(pdf_file, output_folder)

    #总结图片中的QA并且返回
    simple_multimodal_conversation_call(list_jpg)





    time2=time.time()
    print(f'总耗时{time2-time1}')
