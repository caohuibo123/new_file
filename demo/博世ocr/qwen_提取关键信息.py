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


def simple_multimodal_conversation_call():
    # 读取每一个图片  list_jpg
    # for i in list_jpg:
    messages = [
        {
            "role": "user",
            "content":
                [
                    {"image":r"C:\Users\cao\Desktop\CO23120141\page_4.jpg"},
                    {
                        "text": "你现在是一个专业人员,对图片中所有信息进行理解，然后标准的格式返回我，如果图片中没有的话就不要返回了.只需要返回以下的信息，发票号码(装箱单号):****,文件号（提单号）:****，总货物包数(件):****，毛重:****，净重:****，发票号码:****，跟踪ID:****，开票日期:****，供应商代码:****"},
                ]
        }]
    response = dashscope.MultiModalConversation.call(model='qwen-vl-max',
                                                     messages=messages,
                                                     api_key='sk-7939f5b192404940843cfc80226b906c')

    if response.status_code == HTTPStatus.OK:

        qa=response["output"]["choices"][0]["message"]["content"][0]["text"]
        print(qa)
        # with open(r"C:\Users\cao\Desktop\CO23120141所有关键信息.docx", 'a', encoding='utf-8') as f:
        #     f.write(qa + '\n' + i +'\n'+'\n'+ '----------------------------------------'+'\n'+'\n')
        #     print(f'{i}提取完毕已存入')

    else:
        print(response.code)  # The error code.
        print(response.message)  # The error message.


if __name__ == '__main__':
    time1 = time.time()
    # 输入PDF文件路径和输出文件夹路径
    # pdf_file = r"C:\Users\cao\Desktop\样本\CO23120141.pdf"
    # output_folder = r"C:\Users\cao\Desktop\CO23120141"

    # # 获取所有的地址，
    # list_jpg = os.listdir(r"C:\Users\cao\Desktop\CO23120141")
    # 定义一个函数，用来提取文件名中的数字部分
    # def extract_number(filename):
    #     return int(filename.split('_')[1].split('.')[0])
    # 使用自定义的排序键对列表进行排序
    # list_jpg.sort(key=extract_number)



    # 将PDF转换为图像
    # pdf_to_images(pdf_file, output_folder)

    #总结图片中的QA并且返回list_jpg,list_jpg
    simple_multimodal_conversation_call()

    time2=time.time()
    print(f'总耗时{time2-time1}')