import requests
from fastapi import FastAPI,Form
import uvicorn
app=FastAPI()
@app.post('/pass')#路由地址
#单独运行的时候不添加      def main(text):
#下面是调用的时候的写法
def main(text:str=Form(...)):
    pass
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=7001)



#函数调用
def pdfTOtext(text):
    # 先判断图片还是pdf，如果是pdf就会先转成图片，
    # 返回的是内容转成文本之后的文件名字
    url = "地址+路由"
    try:
        data = {'text': text}
        response = requests.post(url, data=data)
        if response.ok:
            return response.text
        else:
             return '请求失败'
    except Exception as e:
        return e


