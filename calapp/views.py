from django.shortcuts import render
import math
# Create your views here.
def cal(request):
	if request.method == 'POST':
		answer  = request.POST['answer']
		try:
			result = eval(answer)
		except Exception as e:
			e.m = 'Something Wrong! Try Again'
			return render(request,'cal.html',{'m': e.m})
		#print(result)
		return render(request,'cal.html',{'re': result})
	return render(request,'cal.html',)