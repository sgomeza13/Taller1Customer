from django import forms

from .models import CustomerUser

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ['email', 'password', 'first_name','last_name', 'address']
    
    def clean_password(self):
        password = self.cleaned_data['password']
        if(len(password)<=6):
            raise forms.ValidationError("Contraseña: Contraseña muy corta, minimo 7 caracteres")
        elif(" " in password):
            raise forms.ValidationError("Contraseña: Espacios no permitidos")
        elif(password.lower()==password):
            raise forms.ValidationError("Contraseña: Minimo 1 caracter con mayusculas")
        elif(not(any(i.isdigit() for i in password))):
            raise forms.ValidationError("Contraseña: Minimo 1 digito")
        return password        

        

class CustomerChangeForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ('email','password','address')


