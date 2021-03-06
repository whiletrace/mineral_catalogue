from django.db import models


# Create your models here.

class Mineral(models.Model):
    """
        Mineral model controls the instantiation of models.mineral objects

        as well as creation of tables within db to store data that is
        queried.  methods def__iter__:
    """
    name = models.CharField(max_length=500, blank=True, default='')
    image_filename = models.CharField(max_length=500, blank=True, default='')
    image_caption = models.CharField(max_length=500, blank=True, default='')
    category = models.CharField(max_length=500, blank=True, default='')
    formula = models.CharField(max_length=500, blank=True, default='')
    strunz_classification = models.CharField(max_length=500, blank=True, default='')
    color = models.CharField(max_length=500, blank=True, default='')
    crystal_system = models.CharField(max_length=500, blank=True, default='')
    unit_cell = models.CharField(max_length=500, blank=True, default='')
    crystal_symmetry = models.CharField(max_length=500, blank=True, default='')
    cleavage = models.CharField(max_length=500, blank=True, default='')
    mohs_scale_hardness = models.CharField(max_length=500, blank=True, default='')
    luster = models.CharField(max_length=500, blank=True, default='')
    streak = models.CharField(max_length=500, blank=True, default='')
    diaphaneity = models.CharField(max_length=500, blank=True, default='')
    optical_properties = models.CharField(max_length=500, blank=True, default='')
    refractive_index = models.CharField(max_length=500, blank=True, default='')
    crystal_habit = models.CharField(max_length=500, blank=True, default='')
    specific_gravity = models.CharField(max_length=500, blank=True, default='')
    group = models.CharField(max_length=500, blank=True, default='')
# not all data will have all attr so as available blank=True or default=""
# this will very based on data type of deserialization

    def __iter__(self):
        """
            method for  iteration over the fields and values of obj
        """
        for field in self._meta.fields:
            yield (field.verbose_name, field.value_to_string(self))
