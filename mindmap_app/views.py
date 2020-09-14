from django.shortcuts import render
from django.views.generic.base import View
from textsum_app.models import jsonContent
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# 取得此用戶的所有心智圖
def get_mindmap(request):
    if request.user.is_authenticated:
        name = request.user.get_username()
        try:
            jsons = jsonContent.objects.filter(author=request.user)
        except:
            # return render(request,"login.html")
            pass
    return render(request, 'mindmap.html',locals())

# 開啟某一心智圖
def edit_mindmap(request, id):
    if request.user.is_authenticated:
        try:
            # get條件多一個author是怕有人憑id取挖別人的檔案
            j = jsonContent.objects.get(id=id, author=request.user)
            return render(request, 'edit.html', locals())
        except:
            return HttpResponseRedirect('/mindmap/')
    return render(request,"login.html")

# 刪除某一心智圖
def del_mindmap(request, id):
    if request.user.is_authenticated:
        try:
            jsonContent.objects.get(id=id).delete()
            msg = '刪除成功'
            return HttpResponseRedirect('/mindmap/')

        except:
            msg = '刪除失敗'
            return HttpResponseRedirect('/mindmap/')
        # return render(request, 'mindmap.html',locals())
    return render(request,"login.html")

# 編輯某一心智圖的敘述
def edit_describe(request, id):
    if id and request.user.is_authenticated:
        # print(request)
        try:
            # describe = request.POST['describe']
            title = request.POST['title']
            # jsonContent.objects.filter(id=id).update(describe=describe)
            jsonContent.objects.filter(id=id).update(title=title)
            msg = '修改成功'
            return HttpResponseRedirect('/mindmap/')

        except:
            msg = '修改失敗'
            return HttpResponseRedirect('/mindmap/')
    return render(request,"login.html")

# 儲存檔案(更新json檔)
def save_json(request, id):
    if request.user.is_authenticated:
        author = request.user
        if request.method == "POST":
            try:
                id = request.POST['id']
                jfile = request.FILES['jfile']

                print('id: {id}, jfile: {j} '.format(id, jfile))

                j = jsonContent.objects.get(id=id)
                j.content = jfile
                j.save()

                return render(request, 'edit.html', {'id': id, 'j':j})
            except:
                pass
        return render(request, 'edit.html', {'id': id})
    return redirect ("/account/login")