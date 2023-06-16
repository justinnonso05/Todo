from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import RegisterForm, AddTodoForm, DeleteTaskForm
from .models import Todo, User
from django.urls import reverse_lazy


def home(request):
	return render(request, 'tasks/home.html')


class CreateTodoView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = Todo
	fields = ['label', 'tasks']
	template_name = 'tasks/add.html'
	context_object_name = 'todo'
	success_url = '/tasks'
	success_message = 'Task Added Successfully'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)
		messages.success(self.request, self.success_message)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = '| Add task'
		return context

class UpdateTodoView(UserPassesTestMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Todo
	fields = ['label', 'tasks']
	template_name = 'tasks/edit.html'
	context_object_name = 'todo'
	success_url = '/tasks'
	success_message = 'Task Update successful'

	def test_func(self):
		task = self.get_object()
		if self.request.user == task.user:
			return True
		else:
			return False
		return self.request.user.is_authenticated

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)
		messages.success(self.request, self.success_message)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = '| Edit task'
		return context


class DeleteTodoView(UserPassesTestMixin, LoginRequiredMixin, SuccessMessageMixin, DeleteView):
	model = Todo
	template_name = 'tasks/delete.html'
	context_object_name = 'todo'
	success_url = '/tasks'
	success_message = 'Task Deleted'

	def test_func(self):
		task = self.get_object()
		if self.request.user == task.user:
			return True
		else:
			return False
		return self.request.user.is_authenticated

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = '| Delete task'
		return context


# def add(request):
# 	if request.method == "POST":
# 		add_form = AddTodoForm(request.POST)
# 		if add_form.is_valid():
# 			instance = add_form.save(commit = False)
# 			instance.user = request.user
# 			instance.save()
# 			messages.success(request, f'Task added successfuly!')
# 			return redirect('tasks')
# 	else:
# 		add_form = AddTodoForm()
# 	return render(request, 'tasks/add.html', {'add_form': add_form})


class TodoListView(UserPassesTestMixin, LoginRequiredMixin, ListView):
	model = Todo
	template_name = 'tasks/tasks.html'
	context_object_name = 'todo'
	ordering = ['-date_created']

	def test_func(self):
		return self.request.user.is_authenticated

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(user = self.request.user)

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = '| Tasks'
		return context

# def tasks(request):
# 	logged_user = Todo.objects.filter(user = request.user)
# 	return render(request, 'tasks/tasks.html', {'todo': logged_user})

def signup(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created successfuly!')
			return redirect('login')
	else:
		form = RegisterForm()
	return render(request, 'tasks/signup.html', {'form': form, 'title': 'Register'})

@login_required
def profile(request):
	...

class UpdateProfileView(UserPassesTestMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = User
	fields = ['username', 'email']
	template_name = 'tasks/profile.html'
	success_url = reverse_lazy('tasks')
	success_message = 'Profile Update successful'

	def test_func(self):
		user = self.request.user
		user_object = self.get_object()
		return user == user_object

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)
		messages.success(self.request, self.success_message)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = '| Update Profile'
		return context

class SearchResultView(UserPassesTestMixin, LoginRequiredMixin, ListView):
	model = Todo
	template_name = 'tasks/search.html'
	context_object_name = 'todo'
	ordering = ['-date_created']

	def test_func(self):
		return self.request.user.is_authenticated

	def get_queryset(self):
		queryset = super().get_queryset()
		search_query = self.request.GET.get('key')
		object_list = queryset.filter(Q(user = self.request.user) & (Q(tasks__icontains = search_query.lower()) | Q(label__icontains = search_query.upper())))
		return object_list
		return object_list

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = '| Tasks'
		return context