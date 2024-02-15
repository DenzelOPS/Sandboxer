from django.db import models

class Visit(models.Model):
    
    VISIT_CHOICES = [
        ('безлимит', 'безлимит'),
        ('1 час', '1 час'),
        ('30 минут', '30 минут'),
    ]

    visit = models.CharField(max_length=20, choices=VISIT_CHOICES)
    
    
    def __str__(self):
        return str(self.visit)
    
class Hall(models.Model):
    hall_name = models.CharField(max_length=200)
    price_thirty_minute = models.IntegerField()
    price_one_hour = models.IntegerField()
    price_unlimited = models.IntegerField()
    def __str__(self):
        return str(self.hall_name)
    
class Partner(models.Model):
    partner_name = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.partner_name)

class Payment(models.Model):
    # PAYMENT_CHOICES = [
        # ('QR', 'QR'),
        # ('реклама', 'реклама'),
        # ('наличные', 'наличные'),
    # ]
    payment = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.payment)

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=200)
    mobile_phone = models.CharField(max_length=200)
    large_families = models.BooleanField()
    payment_client = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name = "client_payment")
    
    def __str__(self):
        return str(self.name)

class Discount(models.Model):
    discount_name = models.CharField(max_length=200)
    discount_percent = models.IntegerField()
    
    
    def __str__(self):
        return "Скидка "+ str(self.discount_name) + " - " + str(self.discount_percent) + "%"

class Child(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский')
    ]
    HALL_CHOICES = [
        ('Форум', 'Форум'),
        ('Гранд парк', 'Гранд парк')
    ]
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    status = models.BooleanField()
    hall = models.ForeignKey(Hall, on_delete=models.DO_NOTHING, related_name = "child_hall")
    visit = models.ForeignKey(Visit, on_delete=models.DO_NOTHING, related_name = "child_visit")
    partner = models.ForeignKey(Partner, on_delete=models.DO_NOTHING, related_name = "child_partner", null = True, blank = True)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, related_name = "client_child")
    discount = models.ForeignKey(Discount, on_delete=models.DO_NOTHING, related_name = "child_discount", null = True, blank = True)
    #PARTNER_CHOICES = [
    #    ('YaYaPass', 'YaYaPass'),
    #    ('Choco', 'Choco')
    #]
    def __str__(self):
        return "Ребенок - "+str(self.name)+", его родитель -" + str(self.client)

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.IntegerField()
    
    def __str__(self):
        return str(self.product_name)

class OrderItem(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name = "client_product")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = "client_product")
    amount = models.IntegerField()
    #product_name = models.CharField(max_length=200)
    
    def __str__(self):
        return "Клиент "+ str(self.client) + "заказал " + str(self.product)

class Order(models.Model):
# =============================================================================
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product, through='OrderItem')
#     order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     order_date = models.DateTimeField(auto_now_add=True)
#     ordered = models.BooleanField(default=False)
#     shipping_address = models.TextField()
# =============================================================================
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name = "client_order")
    order_items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)

