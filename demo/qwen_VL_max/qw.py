from fastapi import FastAPI
import uvicorn
import re
import pandas as pd
from http import HTTPStatus
import dashscope

app = FastAPI()

# ... 其他代码不变

@app.post('/qwenjpg')  # 路由地址
def main(img):
    messages = [
        {
            "role": "user",
            "content":
                [
                    {"image": fr'{img}'},
                    {
                        "text": "把图片中的所有信息提取出来，并且以json的格式返回,只需返回跟我以下字段一致的就行,每一次都是固定的这几个，无需返回其他的字段信息,其他任何信息不都返回,'Pre-entry No','Customs Serial No','Consignee & Consignor','Export Part','Transport Means','B/L No','Declarant','Country of Trade','Port of Destination','Contract Agreement No','Quantity','Packing Type','Gross Weight','Net Weight'"},
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

        # 读取现有的 Excel 文件到 DataFrame
        try:
            df = pd.read_excel('output.xlsx', index_col='Pre-entry No')
        except FileNotFoundError:
            # 如果文件不存在，创建一个空的 DataFrame
            df = pd.DataFrame()

        # 将新的数据添加到 DataFrame 中
        new_data = pd.DataFrame([a2])  # 将单个字典作为列表中的元素，以便传递索引

        # 使用 _append 方法追加数据，并忽略索引以保持一致
        df = df._append(new_data, ignore_index=True, sort=False)

        # 将数据写回到 Excel 文件
        excel_file = 'output.xlsx'
        df.to_excel(excel_file, index=False)  # 不保存索引列

        return "OK: " + excel_file

    else:
        return (response.code)  # The error code.
        return (response.message)  # The error message.

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=7001)
