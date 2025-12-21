from django.shortcuts import render
from .models import Todo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from .form import TodoForm
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# def todo_list(request):
#     # nome = "Victor"
#     # nomes = ["Davi", "Saleh", "Victor", "Luanderson"]
#     todos = Todo.objects.all()

#     return render(request, "todos/todo_list.html", {"todos": todos})


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo

    def get_queryset(self):
        # Retorna apenas as tarefas que pertencem ao utilizador logado
        return Todo.objects.filter(user=self.request.user)


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        # Antes de gravar no banco de dados, atribuímos o utilizador logado à tarefa
        form.instance.user = self.request.user
        return super().form_valid(form)


class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo_list")


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()

        if request.headers.get("HX-Request"):
            return HttpResponse("")

        return redirect(self.get_success_url())


class TodoCompleteView(View):
    def post(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_has_complete()

        # Verifica se é uma requisição do HTMX
        if request.headers.get("HX-Request"):
            # Retorna APENAS o pedaço da linha atualizada
            return render(request, "todos/todo_row.html", {"todo": todo})

        # Se não for HTMX (fallback), redireciona normalmente
        return redirect("todo_list")
