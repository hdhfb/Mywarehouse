#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def count(request):
    text=request.GET['text']
    count={}
    for word in text:
    	if word not in count:
    		count[word] = 1
    	else:
    		count[word] += 1
    sorted_dict=sorted(count.items(), key=lambda w:w[1], reverse=True)
    return render(request, 'count.html', 
    	{'text':text,'sorted_dict':sorted_dict})