from django.db import models
from django.core.exceptions import ValidationError

#Home
class Home(models.Model):
    name = models.CharField(max_length= 20)
    greetings_1 = models.CharField(max_length=5)
    greetings_2 = models.CharField(max_length=5)
    picture = models.ImageField(upload_to='picture/')
    #save time when changed
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
#ABOUT

class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='picture/')
    
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.career
    
class Profile(models.Model):
    about = models.ForeignKey(About,
                              on_delete = models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length = 200)
    
#Skills 

class Category(models.Model):
    name = models.CharField(max_length=20)
    
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        
    def __str__(self):
        return self.name
    
    
class Skills(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete= models.CASCADE)
    skill_name = models.CharField(max_length = 20)
    

#Experience

class Experience(models.Model):
    company = models.CharField(max_length = 65)
    position = models.CharField(max_length=200)
    years_from = models.IntegerField()
    years_to = models.IntegerField()
    description = models.TextField(blank = False, default= '')
    company_img = models.ImageField(upload_to='picture/', default='')
    
    def clean(self):
        # Check if the years are within a valid range
        if self.years_from < 1900 or self.years_from > 9999:
            raise ValidationError('Years from must be between 1900 and 9999.')
        if self.years_to < 1900 or self.years_to > 9999:
            raise ValidationError('Years to must be between 1900 and 9999.')

        # Check if years_to is greater than or equal to years_from
        if self.years_from > self.years_to:
            raise ValidationError('Years to must be greater than or equal to years from.')
        
    def __str__(self):
        return self.company
        
        
    

#Portfolio

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link =  models.URLField(max_length = 200)
    skills_used = models.CharField(max_length = 400,default='')
    description = models.TextField(blank=False,default='')
    
    def __str__(self):
        return f'Portfolio {self.id}'
    