import json
import time

from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')


def msg_data(request):
    data = json.loads(request.body)
    new_data = str(data['message'])
    print(new_data)
    with open("chat.txt", "w") as file:
        # 写入文本内容
        file.write(new_data)
    print("文本已成功保存到文件。")
    time.sleep(1.5)
    with open("D:/chatBot/RealBot/botAnswer.txt", "r") as file:
        # 写入文本内容
        answer = file.read()
        response_data = {'answer': answer}
    print(answer)
    return JsonResponse(response_data)
