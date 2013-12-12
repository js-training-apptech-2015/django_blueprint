from django.shortcuts import render

def frontpage(request):
	return render('index.html', {'key': 'value'})