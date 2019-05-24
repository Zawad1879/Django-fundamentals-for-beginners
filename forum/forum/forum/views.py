from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.shortcuts import redirect
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

	def post(self, request, *args, **kwargs):
		print (request.POST.get('newcomment'))
		print(request.user.id)
		print(self.kwargs['pk'])
		Comment.objects.create(user_id=request.user.id, post_id=self.kwargs['pk'], comment_text=request.POST.get('newcomment'))
		return redirect('/')

