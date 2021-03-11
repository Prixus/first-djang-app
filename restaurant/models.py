from django.db import models

# Create your models here.

class MenuItem:
    id: int
    name: str
    img: str
    description: str
    price: int
