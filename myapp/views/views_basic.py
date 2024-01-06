from django.shortcuts import render

def index(request):  #首頁
    

	return render(request, "index.html", locals())