from django.shortcuts import render,redirect
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chat import lista
chatbot = ChatBot("Ron Obvious")
trainer = ListTrainer(chatbot)
trainer.train(lista.conversa)

mensagens =[[]]


def index(request):
    if request.method == 'GET':
        context={
            'mensagens':mensagens
            }
        return render(request,'index.html',context)

def chat_enviar(request):
    if request.method == 'POST':
        chat_mensagem = request.POST['chat_mensagem']

        

        response = chatbot.get_response(chat_mensagem)
        resposta = response
        mensagens.append([chat_mensagem,resposta])
       

        return redirect(index)

def ferramenta(request):
    if request.method == 'GET':
        context={
            'mensagens':mensagens
        }
        return render(request,'ferramenta.html',context)

def tdah(request):
    if request.method == 'GET':

        context={
            'mensagens':mensagens
            }
        return render(request,'tdah.html',context)

def ajuda(request):
    if request.method == 'GET':

        context={
            'mensagens':mensagens
            }
        return render(request,'ajuda.html',context)

def referencias(request):
    if request.method == 'GET':
        context={
            'mensagens':mensagens
            }
        return render(request,'referencias.html',context)