from django.shortcuts import render

def home_view(request):
   # print(request)
   # print(request.user)

   
   return render(request, 'home.html')