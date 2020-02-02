from django.db import models

# Create your models here.

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class University(models.Model):
    """Model representing the university we're attending."""
    name = models.CharField(max_length=200, help_text='Enter a University (e.g. University of Waterloo)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Building(models.Model):
    """Model representing a building."""
    name = models.CharField(max_length=200, help_text='Enter a Building (e.g. DC)')

    # Foreign Key used because building can only have one university, but university can have multiple buildings
  
    University = models.ForeignKey(University, on_delete=models.SET_NULL, null=True, help_text='Select a university for this building')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name


from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Desk(models.Model):
    """Model representing a desk (but not a specific copy of a desk)."""
    Number = models.CharField(max_length=200)
   
        
    # ManyToManyField used because building can contain many desk numbers. Desk numbers can appear in many buildings.
    # Genre class has already been defined so we can specify the object above.
    building = models.ManyToManyField(Building, help_text='Select a building for this desk')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.Number
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this desk."""
        return reverse('desk-detail', args=[str(self.id)])


import uuid # Required for unique desk instances

class DeskInstance(models.Model):
    """Model representing a specific copy of a desk (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular desk across whole database')
    desk = models.ForeignKey('Desk', on_delete=models.SET_NULL, null=True) 
    due_back = models.TimeField(null=True, blank=True)

    # ManyToManyField used because building can contain many desk numbers. Desk numbers can appear in many buildings.
    # Genre class has already been defined so we can specify the object above.
    building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True, help_text='Select a building for this desk instance')

    AVAILABILITY_STATUS = (
        ('m', 'Away'),
        ('o', 'Occupied'),
        ('a', 'Available'),
    )

    status = models.CharField(
        max_length=1,
        choices=AVAILABILITY_STATUS,
        blank=True,
        default='a',
        help_text='Desk availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.desk.Number})'
    


    
