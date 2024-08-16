
from django.shortcuts import render,redirect
from .forms import MovieForm,CategoryForm
from .models import Orders,Movie,Category,SeatOne,SeatTwo,SeatThree,SeatFour
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def mainview(request):
    return render(request,'index.html')

@login_required(login_url='/credentials/login/')
def addCategory(request):
    if request.method == "POST":
        form = CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            print(form.errors)
    else:
        form=CategoryForm
    return render(request,"add_category.html",{'form':form})

def success(request):
    return HttpResponse('Success! Your category has been added.')

@login_required(login_url='/credentials/login/')
def addMovie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            print(form.errors)
    else:
        form=MovieForm
    return render(request,"add_movie.html",{'form':form})

@login_required(login_url='/credentials/login/')
def selectshow(request):
    return render(request,'select_show.html')


@login_required(login_url='/credentials/login/')
def selectseat(request,idd):
   
        # print("True")
    request.session['idd'] = idd
    if idd==14:
        all_seats = SeatOne.objects.filter(show_id=idd).values('seat_number','status')    
        items_per_row = 20
        seats_per_row = [all_seats[i:i + items_per_row] for i in range(0, len(all_seats), items_per_row)]
        return render(request,'select_seat.html',{'st':seats_per_row})
    if idd==15:
        all_seats = SeatTwo.objects.filter(show_id=idd).values('seat_number','status')    
        items_per_row = 20
        seats_per_row = [all_seats[i:i + items_per_row] for i in range(0, len(all_seats), items_per_row)]
        return render(request,'select_seat.html',{'st':seats_per_row})
    if idd==16:
        all_seats = SeatThree.objects.filter(show_id=idd).values('seat_number','status')    
        items_per_row = 20
        seats_per_row = [all_seats[i:i + items_per_row] for i in range(0, len(all_seats), items_per_row)]
        return render(request,'select_seat.html',{'st':seats_per_row})
    if idd==17:
        all_seats = SeatFour.objects.filter(show_id=idd).values('seat_number','status')    
        items_per_row = 20
        seats_per_row = [all_seats[i:i + items_per_row] for i in range(0, len(all_seats), items_per_row)]
        return render(request,'select_seat.html',{'st':seats_per_row})

   
    
    

@login_required(login_url='/credentials/login/')
def changeSeatStatus(request):
    idd = request.session.get('idd')
    if request.method == 'GET':
        seat_no = request.GET.get('seatnos')
        if seat_no:
            seat_no_list = seat_no.split(',')
            for i in seat_no_list:
                i = i.strip()
                if i.isdigit() and 1 <= len(i) <= 3:
                    j = int(i)
                if idd==14:
                    stk = SeatOne.objects.get(show_id=idd, seat_number=j)
                    stk.status=True
                    stk.save()
                elif idd==15:
                    stk = SeatTwo.objects.get(show_id=idd, seat_number=j)
                    stk.status=True
                    stk.save()
                elif idd==16:
                    stk = SeatThree.objects.get(show_id=idd, seat_number=j)
                    stk.status=True
                    stk.save()
                elif idd==17:
                    stk = SeatFour.objects.get(show_id=idd, seat_number=j)
                    stk.status=True
                    stk.save()
                usr=request.user
                
                ordk=Orders.objects.create(movie=stk.show,user=usr,seat=stk.seat_number)
                ordk.save()

                if idd==14:
                    all_seats = SeatOne.objects.filter(show_id=idd).values('seat_number','status')    
                    items_per_row = 20
                    seats_per_row = [all_seats[i:i + items_per_row] for i in range(0, len(all_seats), items_per_row)]
                    return render(request,'select_seat.html',{'st':seats_per_row})
                if idd==15:
                    all_seats = SeatTwo.objects.filter(show_id=idd).values('seat_number','status')    
                    items_per_row = 20
                    seats_per_row = [all_seats[i:i + items_per_row] for i in range(0, len(all_seats), items_per_row)]
                    return render(request,'select_seat.html',{'st':seats_per_row})
                if idd==16:
                    all_seats = SeatThree.objects.filter(show_id=idd).values('seat_number','status')    
                    items_per_row = 20
                    seats_per_row = [all_seats[i:i + items_per_row] for i in range(0, len(all_seats), items_per_row)]
                    return render(request,'select_seat.html',{'st':seats_per_row})
                if idd==17:
                    all_seats = SeatFour.objects.filter(show_id=idd).values('seat_number','status')    
                    items_per_row = 20
                    seats_per_row = [all_seats[i:i + items_per_row] for i in range(0, len(all_seats), items_per_row)]
                    return render(request,'select_seat.html',{'st':seats_per_row})
                
        return render(request,'select_seat.html',{'st':seats_per_row,'seatnos':seat_no})
        
        
        
        

@login_required(login_url='/credentials/login/')
def view_orders(request):
    # SeatOne.objects.all().delete()
    # SeatTwo.objects.all().delete()
    # SeatThree.objects.all().delete()
    # SeatFour.objects.all().delete()
    # Movie.objects.all().delete()
    # Orders.objects.all().delete()
    # Category.objects.all().delete()

    # reset show 1, SeatOne
    # sho=Movie.objects.get(id=14)
    # SeatOne.objects.all().delete()
    # for seat_number in range(1, 101):
    #     SeatOne.objects.create(show=sho, seat_number=seat_number)

    # reset show 2, SeatTwo
    # sho=Movie.objects.get(id=15)
    # SeatTwo.objects.all().delete()
    # for seat_number in range(1, 101):
    #     SeatTwo.objects.create(show=sho, seat_number=seat_number)

    # reset show 3, SeatThree
    # sho=Movie.objects.get(id=16)
    # SeatThree.objects.all().delete()
    # for seat_number in range(1, 101):
    #     SeatThree.objects.create(show=sho, seat_number=seat_number)

    # reset show 2, SeatFour
    # sho=Movie.objects.get(id=17)
    # SeatFour.objects.all().delete()
    # for seat_number in range(1, 101):
    #     SeatFour.objects.create(show=sho, seat_number=seat_number)


    usr=request.user  
    vieword=Orders.objects.filter(user_id=usr.id)
    return render(request,'view_orders.html',{'vieword':vieword})


