from django.db import models

class TodoItems(models.Model): # it represent each todo item in our sqlite db
	content = models.TextField()
	
