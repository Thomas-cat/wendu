from django.shortcuts import render, get_object_or_404, redirect
from .forms import StudentForm
from .models import Student
import re
def Enroll(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			context = {'form':form}
			u = request.POST.get('name')
			q = request.POST.get('qq',None)
			o = request.POST.get('obj_school',None)
			i = request.POST.get('institute',None)
			m = request.POST.get('major',None)
			p = request.POST.get('phone')
			is_en = request.POST.get('is_enroll',False)
			temp = Student.objects.filter(name=u,phone=p)
			if temp:
				context.update({'message':'您已报名,请勿重复提交'})
				return render(request, 'enroll/enroll.html', context=context)

			reg = re.compile(r'^1[0-9]{10}$')	
			if reg.match(p) == None:
				context.update({'message':'手机号请正确填写'})
				return render(request, 'enroll/enroll.html', context=context)

			if is_en !=False:
				is_en = True
			Student.objects.create(
			name = u,
			qq = q,
			obj_school = o,
			institute = i,
			major = m,
			phone = p,
			is_enroll = is_en
			)
			return render(request, 'enroll/enroll.html', {'message':'%s同学报名成功'%u})
	form = StudentForm()
	return render(request, 'enroll/enroll.html', {'form':form})
