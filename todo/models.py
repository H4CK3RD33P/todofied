from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100) #this is the title of the todo object.
    memo = models.TextField(blank=True) #this field not necessary but on can fill additional information regarding the task.
    created = models.DateTimeField(auto_now_add=True) #auto_now_add=True means this field is uneditable and it simply add the time and date of creation.
    completed = models.DateTimeField(null=True,blank=True) #null=True means this will be filled later on when the user accomplishes the task; blank=True means it will make this optional when building a todo object from admin panel.
    important = models.BooleanField(default=False) #this is a simple checkbox which is not marked by default. The user will click this if the task is important.
    #we create a column named 'user' where we store the 'id' of the 'User' object which is the primary key of the User database.
    ##Thus, 'user' is a foreign key which references the particular 'User'.
    ##This basically creates one-to-one relationships, because, a user might have multiple todo tasks, but a todo task cannot have multiple users.
    ####on_delete specifies what to do in case the referenced object is deleted i.e the user is deleted from database.
    ####models.CASCADE means remove all the todo objects of a user, if the user itself is deleted at some point of time.
    user = models.ForeignKey(User,on_delete=models.CASCADE) 

    def __str__(self):
        return self.title #show the title of the object as the name of the object.
