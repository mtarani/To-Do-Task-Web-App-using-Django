from django.db import models
from django.utils import timezone

class TodoList(models.Model): #Todolist able name that inherits models.Model
    title = models.CharField(max_length=250) # a varchar
    description = models.TextField(blank=True) # a text field
    last_modified = models.DateTimeField(auto_now=True)#(default=timezone.now().strftime("%m/%d/%Y %H:%M:%S")) # a date
    created_by = models.CharField(max_length=250)
    due_time = models.DateTimeField("%m/%d/%Y %H:%M:%S") # a date
    class Meta:
        ordering = ["due_time"] #ordering by the created field
    def __str__(self):
        return self.title #name to be shown when called
