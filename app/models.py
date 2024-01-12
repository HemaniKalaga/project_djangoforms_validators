from django.db import models

# Create your models here.
class Author(models.Model):
    author_id=models.IntegerField(primary_key=True)
    author_name=models.CharField(max_length=100)
    author_age=models.IntegerField()
    author_exp=models.IntegerField()

    def __str__(self):
        return self.author_name
    
class Book(models.Model):
    book_id=models.IntegerField()
    author_id=models.ForeignKey(Author,on_delete=models.CASCADE)
    book_name=models.CharField(max_length=100)
    book_price=models.IntegerField()

    def __str__(self):
        return self.book_name
    
class Student(models.Model):
    stu_name=models.CharField(max_length=100)
    stu_class=models.CharField(max_length=100)
    book_id=models.ForeignKey(Book,on_delete=models.CASCADE)
    date=models.DateField(auto_now=False,auto_now_add=False)
    stu_email=models.EmailField()
    stu_re_email=models.EmailField()

    def __str__(self):
        return self.stu_name