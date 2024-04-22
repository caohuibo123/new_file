import re
import pandas as pd
from http import HTTPStatus
import dashscope


def simple_multimodal_conversation_call(aaa):

    messages = [
        {
            "role": "user",
            "content":
                [
                    {"image":fr"C:\Users\cao\Desktop\{aaa}"},
                    {
                        "text": "把图片中的所有信息提取出来，并且以json的格式返回,只需返回跟我以下字段一致的就行,其他任何信息不都返回,'Pre-entry No','Customs Serial No','Consignee & Consignor','Export Part','Transport Means','B/L No','Declarant','Country of Trade','Port of Destination','Contract Agreement No','Quantity','Packing Type','Gross Weight','Net Weight'，只需要提取以字段所属的信息就可以了"},
                ]
        }]
    response = dashscope.MultiModalConversation.call(model='qwen-vl-max',
                                                     messages=messages,
                                                     api_key='sk-7939f5b192404940843cfc80226b906c')

    if response.status_code == HTTPStatus.OK:

        a1 = response["output"]["choices"][0]["message"]["content"][0]["text"]

        matches = re.findall(r'\{([^{}]+)\}', a1)
        # 构建输出格式
        output = "{" + matches[0] + "}"
        a2 = eval(output)
        print(a2)
        df = pd.DataFrame(a2, index=['Pre-entry No'])

        # 将数据写入 Excel 文件
        excel_file = 'output.xlsx'
        df.to_excel(excel_file)

        print("Excel 文件已生成:", excel_file)

    else:
        print(response.code)  # The error code.
        print(response.message)  # The error message.


if __name__ == '__main__':
    simple_multimodal_conversation_call(aaa='img.jpg')


