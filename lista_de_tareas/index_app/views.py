from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class IndexView(View):
    def get(self, request):
        return render(request, "index.html", {})

@method_decorator(login_required, name ='dispatch')
class IndexUserView(View):
    def get(self, request):
        return render(request, "index_user.html")