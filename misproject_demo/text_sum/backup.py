# print(df_level.loc[0][1])
# list_=['h3']
# df_level_ = df_level[df_level['level'].isin(list_)]
### print(df_level_)
# ---------------------------------
# 從根結點開始
'''data_dict={'id': "root", 'topic': df_level.loc[0][1]}
next_level = levels[levels.index('h1')+1] # h1下個level
if select_level[next_level]==True:
    child_list=[]
    fliter = (df_level["level"] == select_level[next_level])
    print(df_level[fliter])
print(df_level.loc[0][1])'''

# 亂數產生json檔的id
'''temp_id = ''.join(random.choice(string.ascii_letters) for x in range(5))
print(temp_id)'''
# topic_ ="hiiiiiiiiiii"
# node_str = "{{\"id\":\"{}\",\"topic\":\"{}\"}}".format(temp_id, topic_)
# print(node_str)

'''# 得到節點的json內容
for index, row in df_level.iterrows(): # traverse所有row
    node_dict = {}
    node_dict['id'] = index
    node_dict['topic'] = row["topic"]
    j = json.dumps(node_dict, ensure_ascii=False)
    print(j)

    # print("index: " + str(index) + ", level: "+ row["level"]+ " , text: "+ row["topic"])
    node_str = "{{\"id\":\"{}\",\"topic\":\"{}\"}}".format(index, row["topic"])
    print(node_str)'''

# -----------------------------------------
# 找出要產生random id的level，為h1底下第一個存在(user設true)的level
# print("-------------------0804---------------------")
'''r_level=1
while select_level[levels[r_level]]==False and r_level<len(levels):
    r_level+=1

print("r_level: ", r_level, ", level name: ", levels[r_level])'''

# # (感覺可以不用判斷，先在前面擋下來內容空的情況)若存在比h1小的節點，才能產生心智圖
# if r_index>len(levels):

'''count=0
while(count<len(df_level)):
    current_row = df_level.iloc[count] # 當下那row
    node_dict={}
    child_list=[]

    # 若此節點level為user有選的
    if select_level[current_row['level']]==True:
        # # 若其level為要產生random id的level
        # if current_row['level']==levels[r_level]:
        r_id = ''.join(random.choice(string.ascii_letters) for x in range(8))
        node_dict['id'] = r_id
        node_dict['text'] = current_row['topic']

        ch_end = 1 # 此節點的最後一個子節點的後一個
        while df_level.iloc[count+ch_end]['level']!= current_row['level']:
            ch_end+=1

        j = json.dumps(node_dict, ensure_ascii=False)
        print(j)

    count+=1'''

# -----------------json範例-----------------
# 子節點1
'''node_2 = {}
node_2['id'] = "ch_index"
node_2['topic'] = "ch_topic"

# 子節點2
node_3 = {}
node_3['id'] = "ch2_index"
node_3['topic'] = "ch2_topic"

# 父節點
node_dict = {}
node_dict['id'] = "p_id"
node_dict['topic'] = "p_topic"

# 若有子節點，加去父節點
child_list=[] # 此list會暫存子節點的內容
child_list.append(node_2)
child_list.append(node_3)
if(child_list):
    node_dict['children'] = child_list

j = json.dumps(node_dict, ensure_ascii=False)
print(j)'''
