from django.shortcuts import render
from django.http import HttpResponse
from .utils import count_total_words, generate_method_section, generate_score, generate_original_score

# Create your views here.
def process_input(request):
    if request.method == 'POST':
        if 'input1' in request.POST:
            original_method = request.POST.get('input1')
            request.session['original_method'] = original_method  # 将值存储在会话中
            
            # 在第一个输入按钮旁边显示 "done"
            return render(request, 'input.html', {'done': True})
        
        if 'input2' in request.POST:
            original_method = str(request.session.get('original_method'))  # 获取第一个输入的值
            result = request.POST.get('input2')
            original_total = original_method + result
            generated_method = generate_method_section(original_total)
            generated_total = generated_method + result
            original_score = generate_original_score(original_total)
            # score, explanation = original_score.split(' ', 0)  # 通过空格分隔分数和解释
            # original_score = f"{score}<br>{explanation}"  # 添加换行
            generated_score = generate_score(generated_total)
            
            # 执行与 input2 相关的操作
            return render(request, 'result.html', {'method': generated_method, 'original_score': original_score, 'generated_score': generated_score})
        elif 'goback' in request.POST:
            return render(request, 'input.html')
    else:
        return render(request, 'input.html')

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)


