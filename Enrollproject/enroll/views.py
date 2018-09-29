from django.shortcuts import render, get_object_or_404, redirect
from .forms import StudentForm
from .models import Student
import re
import openpyxl
from django.http import FileResponse
from openpyxl.styles import Font
def Download(request):
	wb = openpyxl.Workbook()
	sheet = wb.active
	sheet.title = '2020文都考研报名表'
	value = [['姓名','手机','qq','是否学员','学院','专业','目标学校']]
	a = Student.objects.all()
	for item in a:
		if item.is_enroll == True:
			is_enroll = '是'
		else:
			is_enroll = '否'
		temp = [item.name,item.phone,item.qq,is_enroll,item.institute,item.major,item.obj_school]
		value.append(temp)
	for i in range(len(value)):
		for j in range(len(value[i])):
			sheet.cell(row=i+1, column=j+1, value=str(value[i][j]))
	for i in ['A','B','C','D','E','F','G']:
		sheet.column_dimensions[i].width = 30


	for column in sheet.columns:
		for cell in column:
			cell.font = Font(size=20)

	wb.save('./2020文都考研报名表.xlsx')
	file=open('./2020文都考研报名表.xlsx','rb')
	response =FileResponse(file)
	response['Content-Type']='application/octet-stream'
	response['Content-Disposition']='attachment;filename="wendu.xlsx"'
	return response
	
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
			return render(request, 'enroll/enroll_ok.html', {'message':'[%s]同学报名成功,点击返回'%request.POST['name']})
	form = StudentForm()
	return render(request, 'enroll/enroll.html', {'form':form})
