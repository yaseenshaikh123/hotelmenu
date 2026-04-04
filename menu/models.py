from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='dishes/')


class Order(models.Model):
    items = models.TextField()
    total = models.IntegerField()

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        import json
        items_dict = json.loads(self.items)

        text = ""
        for item, data in items_dict.items():
            text += f"{item} ({data['qty']}), "

        return f"{self.name} - {text} - ₹{self.total}"