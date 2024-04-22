import requests
from bs4 import BeautifulSoup
import re
from langchain_openai import ChatOpenAI
import time
time1=time.time()

#爬取网页文本
url='https://www.thepaper.cn/newsDetail_forward_26719895'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 提取纯文本
text = soup.get_text()

#模型调用
llm = ChatOpenAI(openai_api_base='https://36t44u2324.vicp.fun/v1',model_name='城建模型0.2', openai_api_key='asd')

#摘要提示词
match = re.search(r'(.*)责任编辑', text).group(1)
prompt1='请对我文本中比较重要的内容，进行文本摘要，文章中有些内容不是与主题相关,请删除不必要的词语和短语,使句子更加清晰、要求摘要后的字数在200-300字'

#摘要的内容
text1=llm.invoke(prompt1+match)
text1=str(text1)

#模型判断
llm = ChatOpenAI(openai_api_base='https://36t44u2324.vicp.fun/v1',model_name='城建模型0.2', openai_api_key='asd')
prompt='请分析我这个新闻的内容是否会影响到国际物流这个行业的业务，你的回答只需要从Ture和Flese中选择一个答案并且返回我理由'
a1=llm.invoke(prompt+text1)
match = re.search(r"content='([^']*)'", str(a1)).group(1).strip()

#代码判断
if match=='Ture':
    print('符合')
elif match=='Flese':
    print('继续')




time2=time.time()
print('响应时间',time2-time1)
