from django.shortcuts import render
# komentarze
def post_list(request):
    return render(request, 'blog/post_list.html',{})