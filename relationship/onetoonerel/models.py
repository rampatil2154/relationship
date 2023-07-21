from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "AUTHOR_INFO"

class Book(models.Model):
    name = models.CharField(max_length=50)
    publication = models.CharField(max_length=30)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "BOOK_INFO"

class PersonalDetail(models.Model):
    address = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    salary = models.IntegerField()
    author = models.OneToOneField(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.address

    class Meta:
        db_table = "PERSONAL_INFO"

class Library(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=30)
    author = models.ManyToManyField(Author,related_name='library')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "LIBRARY_INFO"
 # Create your models here.
