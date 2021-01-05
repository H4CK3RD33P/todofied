from django.forms import ModelForm #This class lets create a form class based on a model class.
from .models import Todo #Import the todo model

class TodoForm(ModelForm): #We must inherit the ModelForm class to create a form based on the model
    '''
        We need this class to display the form for Todo model in create/ where a particular user logs in
        This is not for admin panel.
    '''
    class Meta: #Here we pass the model information that is, metadata (data about the model)
        model = Todo #this is the model for which we want to create a form
        fields = ['title','memo','important'] #these are the fields we want to displayed in the form