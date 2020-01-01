from django.shortcuts import render
from django.shortcuts import redirect
from . import models

# Create your views here.
def login(request):
    if request.session.get('is_login', None):  # 不允許重複登入
        return redirect('/index/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username.strip() and password:  # 確保帳號密碼都有填寫
            try:
                user = models.User.objects.get(name=username)
            except:
                message = '帳號不存在，請重新輸入！'
                return render(request, 'login/login.html', {'message': message})
            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                message = '密碼不正確！'
                return render(request, 'login/login.html', {'message': message})

        else:
            return render(request, 'login/login.html', {'message': message})
    return render(request, 'login/login.html')

def logout(request):
    if not request.session.get('is_login', None):
        # 沒有登入 就沒有登出
        return redirect("/login/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")
