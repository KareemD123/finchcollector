from django.db import models

# Create your models here.
from django.db import models

from django.urls import reverse

# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


class Finch(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    description = models.CharField(max_length=240)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})


class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])

    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"

    # change the default sort
    class Meta:
        ordering = ['-date']
