from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from textsum_app.models import jsonContent
import re
import pandas as pd
import random, string
import json
from textrank4zh import TextRank4Keyword, TextRank4Sentence
import psycopg2


# ------------------- 要從前端取得的內容 -------------------
# sub代表li底下的解釋
level_num = {'h1':5, 'h2':4, 'h3':3, 'text':2, 'li':1, 'sub':0}
# do_textsum = True
# user選擇要不要顯示這個level
# select_level = {'h1':True, 'h2':True, 'h3':False, 'text':False, 'li':True, 'sub':True}

# ------------------- request -------------------
# 上傳檔案以進行轉換(input: 1 file、4 bool)
def convert(request):
    select_level = {'h1':True, 'h2':True, 'h3':False, 'text':False, 'li':True, 'sub':True}
    if request.user.is_authenticated:
        author = request.user.username

        try:
            select_level['h2'] = request.POST['H2']
            select_level['h3'] = request.POST['H3']
            select_level['text'] = request.POST['Paragraph']
            mdfile = request.POST['mdfile'] # 待確認
            do_textsum = request.POST['Summary']
        except:
            mdfile = NULL
            message = '請上傳檔案'

        # 有上傳檔案且檔案類型為.md
        # if 'mdfile' in request.POST:
        if mdfile.
            json_file = mm_execute(author, mdfile, select_level, do_textsum)
            return render_to_response('MMEdit.html',{'blog': blog})
        else: # 沒上傳檔案
            return render_to_response('convert.html',locals())
    else:
        return render_to_response('convert.html',locals())

# 顯示整個工作區
def shownotes(request):


# 從工作區開一個檔案
def open(request):
    if 'id' in request.GET: # id: 心智圖編號
        print(type(request.GET['id']))
        j = jsonContent.objects.get(id=request.GET['id'])
        return render_to_response('edit.html',locals())
    else:
        # 回到工作區頁面
        return HttpResponseRedirect("/mynotes/")

# ------------------- function ---------------------
# 取得
def get_key (dict_, value):
    return [k for k, v in dict_.items() if v == value]

# 抓到.md資料(progresql版本)
def download_mdfile():
    #db_name = "postgres"
    conn = psycopg2.connect(database="postgres", user="postgres", password="misG6_5PEN", host="127.0.0.1", port=5432)
    c = conn.cursor()
    print("Opened database successfully")
    cursor = c.execute("SELECT upload FROM jsonContent")
    upload_testmd = cursor.fetchone() # 從結果中取一條紀錄，並將游標指向下一條紀錄
    print("Operation done successfully")

    conn.close()
    return upload_testmd

#upload_testmd = download_mdfile()
#print(upload_testmd)

# 取得資料
def get_md():
    # 下面這行之後應該是從資料庫抓，要再改
    fileread =  open('./loginSystem/text_sum/text_data/經濟學 CH22 微觀經濟學.md','r', encoding="utf-8")
    lines = fileread.readlines() #逐行讀取
    lines_=[]
    for i in lines:
        i_ = pre_remove(i)
        if i_.strip()!='':
            lines_.append(i_.strip())
    return lines_

# 判斷一個句子的level
def get_level(sent):
    if(sent[0]=='#'):
        count = 0
        while sent[count]=='#':
            count+=1
            level = 'h'+str(count)
    elif re.match(r'(\d+)\.\s', sent):
        level = 'li'
    elif (sent[0]=='-' or sent[0]=='*') and sent[1]==' ':
        level = 'sub'
    else :
        level='text'
    return level

# 定義每句的level，傳回dataframe(目前header都可，其他level若需要可再加)
def define_level(md_list):
    df_level = pd.DataFrame(columns=['level', 'topic', 'father', 'is_sum'])
    if md_list!=[]:
        f_index = 0
        for sent in md_list:
            # 這句的level
            level = get_level(sent)
            # 這句的父節點
            flag = False
            if df_level.empty: # df為空，代表當下這筆為第一筆，也就是h1
                count=-1
                f_index=-1
            else: # 非空，從最後一筆資料開始
                count=len(df_level)-1

            while flag==False and count>=0:
                temp_l = df_level.loc[count][0]
                if temp_l==level: # 同level就同爸爸
                    f_index = df_level.loc[count][2]
                    flag = True
                elif level_num[temp_l]>level_num[level]: # 新的這筆level較小
                    f_index = count
                    flag = True
                # 剩下沒處理的情況是"新的比較大"，要繼續往上找level大於等於他的
                count-=1
            s = pd.Series({'level':level, 'topic':remove_title(sent), 'father':f_index, 'is_sum':False})
            df_level = df_level.append(s, ignore_index=True)
    return df_level

# 前處理-斜、粗體、冒號、>；移除特殊char
def pre_remove(s):
    # 刪除圖片url
    str_url = r'[a-z]*[:.]+\S+'
    s_ = re.sub(str_url, '', s)

    s_ = s_.replace(':::', '')
    s_ = s_.replace('>','')
    s_ = s_.replace('!','')
    s_ = s_.replace('[]','')

    pos = find_substr(s_, '~~')
    if pos:
        s_ = delete_subs(s_, pos[0], pos[1], len('~~'))

    return s_.strip()

# 找subs在s中的位置，return list
def find_substr(s, subs):
    num = s.count(subs)
    start = 0
    end = len(s)

    pos_list = []

    # print('num: ', num)
    while num>0:
        l_pos = s.find(subs, start, end)   # 從頭開始找在string中第1個出現子字串的位置，找不到會回傳-1
        r_pos = s.find(subs, l_pos+1, end)

        print('l_pos: ' + str(l_pos) + ', r_pos: ' + str(r_pos))
        num = num - 2

        if l_pos>0 and r_pos>0: # 有成對才會append
            pos_list.append(l_pos)
            pos_list.append(r_pos)

        start = r_pos+1

    return pos_list

# 前處理-刪除縣；以位置刪除子字串
def delete_subs(s, l_pos, r_pos, length=1):
    return s[:l_pos]+s[r_pos+length:]

# 把header和list的數字都移除，因為之後要放進json檔裡
def remove_title(s):
    s_ = s.replace('-','')
    s_ = s_.replace('*','')
    s_ = s_.replace('#','')

    rem_chars = r'(\d+)\.\s' # 移除'1. '、'2. '
    s_ = re.sub(rem_chars, '', s_)

    return s_.strip()

# 遞迴產生json檔案
def get_node(index, select_level):
    now_node={'id':''.join(random.choice(string.ascii_letters) for x in range(6)),
            'topic':df_level.loc[index][1]}
    child_list=[]

    if index==0:
        now_node['id']='root'

    # now_node['topic']=df_level.loc[index][1]
    for i in range(index, len(df_level)): # 只有後方的句子才可能為子節點，不用整個df都查
        # 如果該row的father欄位為自己的index，代表為自己小孩，加進children
        if df_level.loc[i][2]==index and select_level[df_level.loc[i][0]]:
            ch_node=get_node(i, select_level)
            child_list.append(ch_node)
    '''else: # 摘要的節點
        now_node['topic']='摘要'
        child_list.append()'''

    if len(child_list)>0:
        now_node['children']=child_list
    return now_node

# 取得摘要的節點
def get_sum_node():
    sum_node={'id':''.join(random.choice(string.ascii_letters) for x in range(6)),
            'topic':'摘要'}
    child_list=[]

    for i in sum: # 只有後方的句子才可能為子節點，不用整個df都查
        ch_node={'id':''.join(random.choice(string.ascii_letters) for x in range(6)),
            'topic':i}
        child_list.append(ch_node)

    sum_node['children']=child_list
    return sum_node

# 把df_level中level為text的內容抓來做文本摘要，會回傳摘要句子及其在df中的index
def catch_label():
    paragraph = df_level[df_level["level"] == "text"] # 把所有為text level的內容都整理成新的df
    par = ""
    summary = []
    summary_index = []
    sentence = paragraph["topic"].values # 擷取句子
    index = paragraph.index
    for i in range(len(sentence)):
        par += sentence[i] + "\n"
    # print(sentence)
    # print(index)

    # 文字摘要
    tr4s = TextRank4Sentence()
    tr4s.analyze(text = par, lower = True, source = 'all_filters')

    for i in tr4s.get_key_sentences(num = 6): # num = 6 代表輸出最好的6句
        summary.append(i.sentence)

        for j in range(len(sentence)):
            if i.sentence == sentence[j]:
                summary_index.append(index[j])
                break

    return summary, summary_index

# 把json_file上傳到資料庫(sqlite3版)
def upload_file(json_file):
    #db_name = "db.sqlite3"
    conn = psycopg2.connect(database="postgres", user="postgres", password="misG6_5PEN", host="127.0.0.1", port=5432) #定義資料存取位置
    c = conn.cursor()
    print("Opened database successfully")

    # 將json檔存放置資料庫
    c.execute("INSERT INTO jsonContent(content) VALUES(?)",[json_file]) #設為列表比較不會因為字數問題儲存錯誤
    conn.commit()
    print("Records created successfully")
    c.close()

# 執行
def mm_execute(author, mdfile, select_level, do_textsum):
    # 生成dataframe
    df_level = define_level(get_md())
    # print(df_level)
    # 取得欲建立json檔前的dict
    node_dict = get_node(0, select_level)

    # 得到摘要index
    if do_textsum:
        sum, sum_index = catch_label()
        node_dict['children'].append(get_sum_node())
        # print(sum_index)

    meta_dict = {"name":"jsMind remote", # file name要再改
                "author":author,
                "version":"0.2"}

    json_dict = {'meta':meta_dict,
                'format':"node_tree",
                'data':node_dict}

    # 產生json檔
    json_file = json.dumps(json_dict, ensure_ascii=False, separators=(',\n', ': ')) # 設定接收參數(dump轉換為str型態)
    upload_file(json_file)
    return json_file


# -----------------以下可刪
'''md_list = get_md()
print(md_list)

df_level = define_level(md_list) # 生成dataframe
print(df_level)

# # 可省
# for index in range(len(df_level)):
#     print('index:', index, 'text: ', df_level.loc[index][1][0:5] , 'father_index: ', df_level.loc[index][2])

# 取得欲建立json檔前的dict
node_dict = get_node(0)

# 得到摘要index
if do_textsum:
    sum, sum_index = catch_label()
    node_dict['children'].append(get_sum_node())
    # print(sum_index)

meta_dict = {"name":"jsMind remote",
            "author":"hizzgdev@163.com",
            "version":"0.2"}

json_dict = {'meta':meta_dict,
            'format':"node_tree",
            'data':node_dict}

# 產生json檔
json_file = json.dumps(json_dict, ensure_ascii=False, separators=(',\n', ': ')) # 設定接收參數(dump轉換為str型態)
upload_file(json_file)'''

# 把json_file上傳到資料庫(照理說是django連接前端和資料庫，但沒辦法做到平行把資料丟到後端吧???)
'''
class jsonContent(models.Model):
    f = SimpleUploadedFile('upload.json', b"json_file")
    print("成功讀取")

testfile = jsonContent.objects.create(file = f)
'''

