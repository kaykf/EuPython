from django.shortcuts import render # type: ignore
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect # type: ignore
from django.urls import reverse # type: ignore

def index(request):
    """Página Principal do Learning_Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Mostra os assuntos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Mostra um único assunto e todas as suas entradas."""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Adiciona um novo assunto"""
    if request.method != 'POST':
        #Nenhum dado submetido cria um formulario em branco
        form = TopicForm()
    else:
        #Dados de post submetidos processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            #return render para voltar para a mesma pag
            return HttpResponseRedirect(reverse('topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """Acrescenta uma nova entrada para um assunto em particular."""
    topic = Topic.objects.get(id= topic_id)

    if request.method != 'POST':
        #nenhum dado submetido cria um formulario em branco
        form = EntryForm()
    
    else: 
        #Dados de post submetidos: processa os dados
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    context = {'topic':topic, 'form':form}
    return render(request,'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    """Edita uma entrada existente"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        #Requisição inicial; preenche preveamente o formulario com a entrada atual
        form = EntryForm(instance = entry)

    else:
        #Dados de Post submetidos; processa os dados
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request,'learning_logs/edit_entry.html', context)