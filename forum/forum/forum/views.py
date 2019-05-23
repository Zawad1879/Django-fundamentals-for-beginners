from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from .models import Post, Comment

@method_decorator(login_required, name='dispatch')
class HomeView(generic.ListView):
	template_name = "home.html"
	model = Post

@method_decorator(login_required, name='dispatch')
class DetailView(generic.DetailView):
	template_name = "detail.html"
	model = Post
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		
		context['comment_list'] = Comment.objects.filter(id=self.kwargs['pk'])
		return context