# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Movie, SeatOne, SeatTwo, SeatThree, SeatFour

# @receiver(post_save, sender=Movie)
# def create_seats(sender, instance, created, **kwargs):
    
#     SeatOne.objects.filter(show=instance).delete()

#     for seat_number in range(1, 101):
#         SeatOne.objects.create(show=instance, seat_number=seat_number)

