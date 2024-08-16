from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name=models.CharField(max_length=40)
    category_description=models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='images/category/')


class Movie(models.Model):
    movie_name=models.CharField(max_length=80)
    movie_description=models.CharField(max_length=200)
    movie_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    movie_image=models.ImageField(upload_to='images/Movies/')
    movie_price=models.PositiveIntegerField()
    movie_date=models.DateTimeField(blank=False)
    movie_time=models.TimeField(blank=False)
    shows_list=[
        ('First_Show','first show'),
        ('Second_Show','Second show'),
        ('Evening_Show','Evening show'),
        ('Night_Show','Night show')
    ]
    shows=models.CharField(max_length=30,choices=shows_list,default='Night_Show')


class SeatOne(models.Model):
    show=models.ForeignKey(Movie,on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    status = models.BooleanField(default=False)

    class Meta:
        unique_together = ('show', 'seat_number')
        ordering = ['seat_number']


class SeatTwo(models.Model):
    show=models.ForeignKey(Movie,on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    status = models.BooleanField(default=False)

    class Meta:
        unique_together = ('show', 'seat_number')
        ordering = ['seat_number']


class SeatThree(models.Model):
    show=models.ForeignKey(Movie,on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    status = models.BooleanField(default=False)

    class Meta:
        unique_together = ('show', 'seat_number')
        ordering = ['seat_number']


class SeatFour(models.Model):
    show=models.ForeignKey(Movie,on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    status = models.BooleanField(default=False)

    class Meta:
        unique_together = ('show', 'seat_number')
        ordering = ['seat_number']

  
class Orders(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    seat=models.CharField(max_length=80)
    order_date=models.DateTimeField(auto_now_add=True)
    order_time=models.TimeField(auto_now_add=True)

