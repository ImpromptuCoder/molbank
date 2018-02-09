from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import molbank
from .forms import addForm,contactForm,loginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,get_user_model,login,logout
# Create your views here.

def index(request):
	molecule_list = molbank.objects.raw('select * from molbank_molbank')
	context = {
	'molecule_list':molecule_list
	}
	return render(request,'molbank/index.html',context)

def loginHTML(request):
	if request.method == 'POST':
		form1 = loginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			print("user success")
			return redirect("home")
		else:
			print("user unsuccessful")
			return redirect("login")
	return render(request,"molbank/login.html")



# def index(request):
#     html = '<h1> ID             SMILES                              SAMPLE_CODE  <h1>'
#     molecule_list = molbank.objects.all()
#     for molecule in molecule_list:
#     	html += "<h3>" +molecule.ID+"  |||  "+molecule.SMILES +"  |||  "+molecule.SAMPLE_CODE+"</h3> <br>"
#     return HttpResponse(html)

def home(request):
	return render(request, 'molbank/home.html')

# def detail(request, mol_id):
# 	molecule_list = molbank.objects.raw('select * from molbank_molbank')
# 	molecule_with_ID = molbank.objects.raw("select ID from molbank_molbank where ID="+mol_id)
# 	return render(request,'')

def search_mol(request):
	return render(request,'molbank/search.html')

def contact(request):
    if request.method == 'POST':
    	form1 = contactForm(request.POST)
    # print (var)
    if form1.is_valid():
    	var=str(form1.cleaned_data['text_smiles'])
    	molecule_list = molbank.objects.raw("select * from molbank_molbank where \"SMILES\" operator(public.@) ('"+var+"','')::bingo.sub")
    	return render(request,'molbank/search_results.html',{'form': form1,'molecule_list': molecule_list})
    return render(request,'molbank/search_results.html')

def add_mols(request):
	form=addForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request,"Successfully Uploaded the molecule")
	context = {'form':form}
	return render(request,'molbank/add_mols.html',{'form':form})

def add(request):
	return render(request,"molbank/add_mols.html")



	# if request.method=='POST':
	# 	form2 = addForm(request.POST)
	# if form2.is_valid():
	# 	res = molbank.objects.raw("insert into molbank_molbank values('"+str(form2.cleaned_data['text_id'])+"','"+str(form2.cleaned_data['text_smiles'])+"','"+str(form2.cleaned_data['text_sample_code'])+"')")
	# 	print(res);
	# 	return render(request,'molbank/add.html',{'form': form2,'molecule_list': res})	