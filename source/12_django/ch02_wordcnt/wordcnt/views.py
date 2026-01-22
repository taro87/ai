from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wordinput(request):
    return render(request,
                  "wordcnt/wordinput.html")

def about(request):
    return render(request,
                  "wordcnt/about.html")

def result(request):
    #print(request.GET)
    # fulltext = request.GET.get('fulltext', '')
    fulltext = request.POST.get('fulltext', '')
    strlength = len(fulltext)
    words = fulltext.split() # space로 구분
    word_dic = dict()
    for word in words:
        if word in word_dic.keys():
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    context = {
        'fulltext': fulltext,
        'strlength': strlength,
        'wordcnt': len(words),
        'dict': word_dic.items(),}
    return render(request=request,
                    template_name="wordcnt/result.html",
                    context=context)