from django.shortcuts import render

def index(request, pageindex=None):  #首頁
    

	return render(request, "index.html", locals())