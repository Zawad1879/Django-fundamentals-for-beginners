from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic

@method_decorator(login_required, name='dispatch')
class HomeView(generic.TemplateView):
	template_name = "home.html"
