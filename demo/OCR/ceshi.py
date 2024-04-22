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
                        "text": "把图片中的所有信息提取出来"},
                ]
        }]
    response = dashscope.MultiModalConversation.call(model='qwen-vl-max',
                                                     messages=messages,
                                                     api_key='sk-7939f5b192404940843cfc80226b906c')




    if response.status_code == HTTPStatus.OK:

        a1 = response["output"]["choices"][0]["message"]["content"][0]["text"]

        print(a1)

    else:
        print(response.code)  # The error code.
        print(response.message)  # The error message.


if __name__ == '__main__':
    simple_multimodal_conversation_call(aaa='img.jpg')


