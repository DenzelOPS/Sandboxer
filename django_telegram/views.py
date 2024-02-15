from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import Log_in_form, ClientForm, ChildForm, ClientOrderForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.forms import formset_factory
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
# Create your views here.

@login_required()
def index(request):
    if request.method == 'POST':
        form = ClientForm(data=request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('add_child')
    else:
        form = ClientForm()
    return render(request, 'index.html', {'form': form})


def add_child(request):
    ChildFormSet = formset_factory(ChildForm, extra=10)

    if request.method == 'POST':
        formset = ChildFormSet(request.POST, prefix='child')
        print(11111111111)
        if formset.is_valid():
            print(0000000)
            # Iterate through the forms in the formset and save each instance
            for form in formset:
                print(123)
                print(form)
                print(456)
                if form.has_changed():
                    form.save()


            return redirect('add_product')
        else:
            print("Error")
            for form in formset:
                print(form.errors)
    else:
        formset = ChildFormSet(prefix='child')

    return render(request, 'add_child.html', {'formset': formset})
    
# def add_product(request):
    # ChildFormSet = formset_factory(ChildForm, extra=10)

    # if request.method == 'POST':
        # formset = ChildFormSet(request.POST, prefix='child')
        # if formset.is_valid():

            # for form in formset:
                # if form.has_changed():
                    # form.save()


            # return render(request, 'add_child.html', {'formset': formset})
        # else:
            # print("Error")
            # for form in formset:
                # print(form.errors)
    # else:
        # formset = ChildFormSet(prefix='child')
    # products = Product.objects.all()
    # print(Product.objects.all())
    # return render(request, 'add_product.html', {'products': products})

def add_product(request):
    client = ClientOrderForm()  # You need to implement how to get the current client
    products = Product.objects.all()
    order_items = 0
    if request.method == 'POST':
    
        order_items = OrderItem.objects.filter(client=client)

    context = {
        'products': products,
        'order_items': order_items,
        'client': client,
    }
    print(555, order_items)
    return render(request, 'add_product.html', context)

def get_order_items(request, client_id):
    # Получение всех OrderItem пользователя
    order_items = OrderItem.objects.filter(client__id=client_id)
    
    # Обработка и суммирование одинаковых OrderItem
    result = {}
    for order_item in order_items:
        product_name = order_item.product.product_name
        amount = order_item.amount
        if product_name in result:
            result[product_name] += amount
        else:
            result[product_name] = amount

    return JsonResponse(result)

def adjust_quantity(request, client_id):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        action = request.POST.get('action')

        client = get_object_or_404(Client, pk=client_id)
        product = get_object_or_404(Product, pk=product_id)

        order_item, created = OrderItem.objects.get_or_create(client=client, product=product)

        if action == 'increment':
            order_item.amount += 1
            order_item.save()
        elif action == 'decrement':
            order_item.amount -= 1
            if order_item.amount <= 0:
                order_item.delete()
            else:
                order_item.save()

        # Получение всех OrderItem пользователя
        order_items = OrderItem.objects.filter(client=client)
        
        # Обработка и суммирование одинаковых OrderItem
        result = {}
        for item in order_items:
            result[item.product.product_name] = item.amount

        return JsonResponse(result)
    else:
        return JsonResponse({'error': 'Invalid method'})

def login(request):
    if request.method == 'POST':
        form = Log_in_form(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else:
        form = Log_in_form()
    return render(request, 'login_page.html', {'form': form})

@csrf_exempt
def submit_order(request):
    if request.method == 'POST':
        # message1 = f"""Отчет о клиенте:
        # Номер телефона: {client.mobile_phone}
        # Имя ребенка: {client.name}
        # Имя ребенка: {client.name}
        # """
        data = json.loads(request.body.decode('utf-8'))
        # Process the data as needed, for example, save it to the database
        client = get_object_or_404(Client, pk=data['client_id'])
        products = Product.objects.all()
        today = datetime.today()
        children = ""
        tarifs = ""
        summary = 0
        for child in Child.objects.filter(client = client):
            print(child.name)
            age = today.year - child.date_of_birth.year   #- ((today.month, today.day) < (child.date_of_birth.month, child.date_of_birth.day))
            children += child.name + ", " + str(age) + " лет. "
            
            if child.visit.visit == "30 минут":
                #print(child.partner, child.partner.partner_name != "Choco")
                price = child.hall.price_thirty_minute
            elif child.visit.visit == "1 час":
                price = child.hall.price_one_hour
            elif child.visit.visit == "безлимит":
                price = child.hall.price_unlimited
                # Hall.objects.get(pk=child.Visit)
            tarifs += child.name + child.hall.hall_name + " + " + str((price if child.partner.partner_name != "Choco" else 0) if child.partner != None else price) + " х 1 = " + str((price if child.partner.partner_name != "Choco" else 0) if child.partner != None else price) + " тенге " + (("(Choco)" if child.partner.partner_name == "Choco" else "") if child.partner != None else "")+"\n" 
            summary += (price if child.partner.partner_name != "Choco" else 0) if child.partner != None else price
            print(tarifs)
            print(child.visit)
            #print(Hall.objects.get(pk=child.Visit) )
        print(children)
        #age = today.year - 1
        
        msg = ""
        # for k, v in data['products']:
            # product = Product.objects.all()
            # print("item ",item)
            # msg += item.product.product_name+": "+item.product.price+" x "+item.amount+" = "+ round(item.product.price*item.amount,1)
            # summary += round(item.product.price*item.amount,1)
        # msg += "/n"
        # msg += f"Общая сумма к оплате: *{summary} тенге*"
        # print(msg)
        for product_id in data['products']:
            #print(123,data['products'][product_id])
            if data['products'][product_id] != 0:
                product = Product.objects.get(pk=product_id)
                msg += product.product_name+": "+str(product.price)+" x "+str(data['products'][product_id])+" = "+ str(round(product.price*data['products'][product_id],1))+"\n"
                #print(product.price* data['products'][product_id]) 
                summary += round(product.price*data['products'][product_id],1)
        msg += f"\nОбщая сумма к оплате: *{summary} тенге*"
        print(msg)
        message = f"""
Отчет о заказе:*

Клиент: {client.name}, {client.mobile_phone}
Ребенок: {children}

*Услуги и товары:*
{tarifs}
{msg}
"""
        print(message)
        # for product in products:
            # print(product.product_name, product.price)
        context = {
            'message': message
        }
        return JsonResponse({'message': message})
    else:
        return JsonResponse({'error': 'Invalid request method'})