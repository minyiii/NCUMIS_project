#!pip install textrank4zh
import re

# 讀取並做前處理
fileread =  open('./misproject_demo/text_sum/text_data/經濟學 CH22 微觀經濟學.md','r' ,encoding='UTF-8')   
char = fileread.read() # 逐字讀取
lines = fileread.readlines() #逐行讀取
lines = [i.strip() for i in lines] #濾除換行字元

# 去掉不要的符號
def predo_content(lines):
  content = [] # 初始化內文
  flag = True
  while fileread != [] and flag == True:
    for i in range(len(lines)): # 逐句讀取字元，並將特定字元改成''
      # 刪除圖片url
      str_url = r'[a-z]*[:.]+\S+'
      lines[i] = re.sub(str_url, '', lines[i])
      lines[i] = lines[i].replace("**","") #把**刪掉
      lines[i] = lines[i].replace(">","") #把>刪掉
      lines[i] = lines[i].replace(":::","") #把>刪掉
      lines[i] = lines[i].replace("info","") #把>刪掉
      lines[i] = lines[i].replace("[]","") #把[]刪掉
      lines[i] = lines[i].replace("!","") #把!刪掉
      content.append(lines[i])
    flag = False
  return content
  #print(content)
content = predo_content(lines)
print(content)


# 判斷哪些是h1 h2 h3 或其他
# 判斷句首#數量來做分類
def catch_label(content):
  
  h1 = ['h1']
  h2 = ['h2']
  h3 = ['h3']
  p = ['p']

  for i in range(len(content)):
    num = lines[i].count("#") # 計算'#'數量
    
    # 判斷為哪類
    if num == 1:
      content[i]
      h1.append(content[i])
    elif num == 2:
      h2.append(content[i])
    elif num == 3:
      h3.append(content[i]) 
    else:
      p.append(content[i])
 
  return h1, h2, h3, p
h1, h2,h3,p = catch_label(content)

p = str(p) #將paragraph轉為字串

# 抓取文字摘要
def catch_summary(p):
  from textrank4zh import TextRank4Keyword, TextRank4Sentence 
  tr4s = TextRank4Sentence()
  tr4s.analyze(text = p, lower = True, source = 'all_filters')
  for item in tr4s.get_key_sentences(num=6): # num = 3 代表輸出最好的3句                   
    print(item.index, item.weight, item.sentence)

catch_summary(p)