from django.shortcuts import render, get_object_or_404, redirect
from .forms import StudentForm,StudentForm2
from .models import Student,Student2
import re
import openpyxl
from django.http import FileResponse
from openpyxl.styles import Font
from operator import itemgetter
import logging
import time
def Download2(request):
	wb = openpyxl.Workbook()
	sheet = wb.active
	sheet.title = '文都考研现场确认报名表'
	value = [['姓名','性别','手机','QQ','乘车日期','乘车班次','单双程','12月份是否需要其它服务','专业','报考学院','报考专业','提交时间']]
	raw_data = []
	a = Student2.objects.all()
	for item in a:
		if item.is_need == True:
			is_need = '是'
		else:
			is_need = '否'
		temp = [item.name,item.sex,item.phone,item.qq,item.is_enroll,item.ride_date,item.ride_time,item.is_return,is_need,item.major,item.obj_school,item.obj_major,str(item.modifed_date).split('.')[0]]
		raw_data.append(temp)
	
	for item in sorted(raw_data,key=itemgetter(1,4,5,6)):
		value.append(item)
	for i in range(len(value)):
		for j in range(len(value[i])):
			sheet.cell(row=i+1, column=j+1, value=str(value[i][j]))
	for i in ['A','B','C','D','E','F','G','H','I','J','K','L']:
		sheet.column_dimensions[i].width =24


	for column in sheet.columns:
		for cell in column:
			cell.font = Font(size=18)

	wb.save('./xianchang.xlsx')
	file=open('./xianchang.xlsx','rb')
	response =FileResponse(file)
	response['Content-Type']='application/octet-stream'
	response['Content-Disposition']='attachment;filename="xianchang.xlsx"'
	return response
def Download(request):
	wb = openpyxl.Workbook()
	sheet = wb.active
	sheet.title = '文都考研直通车报名表'
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

	wb.save('./zhitongche.xlsx')
	file=open('./zhitongche.xlsx','rb')
	response =FileResponse(file)
	response['Content-Type']='application/octet-stream'
	response['Content-Disposition']='attachment;filename="zhitongche.xlsx"'
	return response
	
def index(request):
	return render(request, 'enroll/index.html')
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



def Enroll2(request):
	if request.method == 'POST':
		form = StudentForm2(request.POST)
		if form.is_valid():
			context = {'form':form}
			u = request.POST.get('name')
			q = request.POST.get('qq')
			o = request.POST.get('obj_school')
			om = request.POST.get('obj_major')
			m = request.POST.get('major')
			p = request.POST.get('phone')
			rd = request.POST.get('ride_date')
			rt = request.POST.get('ride_time')
			is_re = request.POST.get('is_return')
			sex = request.POST.get('sex')
			is_ne = request.POST.get('is_need',False)
			if is_re == '0' or is_en == '0':
				context.update({'message':'请填写乘车,学员等相关信息'})
				return render(request, 'enroll/enroll2.html', context=context)
			temp = Student2.objects.filter(name=u,phone=p)
			if temp:
				rd = temp[0].ride_date
				rt =temp[0].ride_time
				ph = temp[0].phone
				name = temp[0].name
				context.update({'message':'您已成功提交信息,请勿重复提交','ph':ph,'rd':rd,'rt':rt,'name':name})
				return render(request, 'enroll/enroll2_ok.html', context=context)
			reg = re.compile(r'^1[0-9]{10}$')	
			if reg.match(p) == None:
				context.update({'message':'手机号请正确填写'})
				return render(request, 'enroll/enroll2.html', context=context)
			if is_ne !=False:
				is_ne = True
			data = {'u':u,'o':o,'q':q,'om':om,'rd':rd,'rt':rt,
					'm':m,'p':p,'is_en':is_en,'is_need':is_ne,
					'is_re':is_re,'sex':sex}
			Student2.objects.create(
			name = u,
			qq = q,
			obj_school = o,
			obj_major = om,
			ride_date = rd,
			ride_time = rt,
			major = m,
			phone = p,
			is_return = is_re,
			is_need = is_ne,
			sex= sex,
			)
			rd = rd
			rt = rt
			ph = p
			name = u
			return render(request, 'enroll/enroll2_ok.html', {'message':'%s,同学成功提交信息'%request.POST['name'],'ph':ph,'name':name,'rd':rd,'rt':rt})
	form = StudentForm2()
	return render(request, 'enroll/enroll2.html', {'form':form})
