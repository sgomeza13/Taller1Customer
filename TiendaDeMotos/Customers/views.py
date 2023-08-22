from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, ListView, View
from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout, authenticate
from .forms import CustomerForm, LoginForm
from .models import CustomerUser
# Create your views here.

#Vista de la pagina de inicio
class CustomerHomeView(TemplateView):
    template_name = "home.html"
    
class error(TemplateView):
    template_name = "error.html"
    
class RegisterView(CreateView):
    template_name = 'customer/register.html'

    def get(self, request):
        form = CustomerForm()
        viewData = {}
        viewData['form'] = form
        return render(request,self.template_name, viewData)
    def post(self, request):
        form = CustomerForm(request.POST)
        viewData = {}
        viewData['form'] = form.data
        print(viewData['form'])
        if(form.is_valid()):
            form.save(commit=True)
            return redirect(reverse('created',kwargs={"email":form.data['email']}))
        else:
            viewErrors = {
                'form':form
            }
            return render(request, self.template_name, viewErrors)
        
class LoginView(View):
    template_name = 'customer/login.html'
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        #form = LoginView(request.POST)
        #viewData = {'form':form.data}
        user = authenticate(request,username=request.POST['email'],password=request.POST['password'])
        print(user)
        if(user != None):
            login(request, user)
            return redirect('home')
        else:  
            return render(request,self.template_name)#,viewData)
        
        
class CustomerListView(ListView):
    model = CustomerUser
    template_name = 'customer/customers.html'
    context_object_name = 'users'

class CustomerView(View):
    template_name = 'customer/customer.html'
    def get(self, request, id):
        viewData = {}
        try:
            customer_id = int(id)
            if customer_id < 1:
                raise ValueError("Product id must be 1 or greater")
            customer = get_object_or_404(CustomerUser, pk=customer_id)
        except:
            return redirect('home')

        viewData["customer"] = customer
        
        return render(request, self.template_name, viewData)
    def post(self, request, id):
        customer = get_object_or_404(CustomerUser, pk=id)
        customer.delete()
        return redirect('list')

class CreatedCustomerView(View):
    template_name = 'customer/created.html'
    def get(self,request, email):
        viewData = {}
        try:
            print(email)
            user = get_object_or_404(CustomerUser, email=email)
            viewData['data'] = user
            print(viewData)
            return render(request,self.template_name,viewData)
        except:
            return redirect('error')
    def post(self,request,email):
        print(email)
        if('repeat_form' in request.POST):
            try:
                user = get_object_or_404(CustomerUser, email=email)
                user.delete()
                return redirect('register')
            except:
                return redirect('error')
        else:
            return redirect('list')
        
        