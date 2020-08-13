# !pip install textrank4zh

# 讀取並做前處理
fileread =  open('./misproject_demo/text_sum/text_data/經濟學 CH22 微觀經濟學.md','r')
#char = fileread.read() # 逐字讀取
lines = fileread.readlines() #逐行讀取
lines = [i.strip() for i in lines] #濾除換行字元

# 去掉不要的符號
def predo_content(lines):
  content = [] # 初始化內文
  flag = True
  while fileread != [] and flag == True:
    for i in range(len(lines)): # 逐句讀取字元，並將特定字源改成''
      if i == "*":
      #if i in "* ~":
        lines[i].replace("")
        #print(lines[i])
      content.append([lines[i]])
    flag = False
  return content
  #print(content)
content = predo_content(lines)
print(content)

