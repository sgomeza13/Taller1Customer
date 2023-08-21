from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, ListView, View
from django.views.generic.edit import CreateView
from .forms import CustomerForm
from .models import CustomerUser
# Create your views here.

#Vista de la pagina de inicio
class CustomerHomeView(TemplateView):
    template_name = "home.html"
    
class CreatedCustomer(TemplateView):
    template_name = 'customer/created.html'
    def get(self,request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] =kwargs
        return render(request,self.template_name,context)

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
        viewData["form"] = form.data
        print(form.data)
        if(form.is_valid()):
            form.save()
            return redirect(reverse('created',kwargs={"email":form.data['email']}))
        else:
            viewErrors = {
                'form':form
            }
            return render(request, self.template_name, viewErrors)
        
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
