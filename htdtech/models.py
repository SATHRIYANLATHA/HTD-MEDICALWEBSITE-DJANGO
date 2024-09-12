from django.db import models

from django.core.exceptions import ValidationError
import re

import os


def validate_session(value):
    if not re.match(r'^\d{4} - \d{4}$', value):
        raise ValidationError('Session must be in the format YYYY - YYYY.')




    
class Session(models.Model):
    session_text = models.CharField(max_length=11, validators=[validate_session])

    def __str__(self) :
        return str(self.session_text)
    
class Course(models.Model):
    course_text = models.CharField( max_length=70)

    def __str__(self) :
        return str(self.course_text)
    
class Prevyearinfo(models.Model):
    
    Session = models.ForeignKey(Session, on_delete = models.CASCADE)
    Course = models.ForeignKey(Course, on_delete = models.CASCADE)
    Prospectus = models.FileField( upload_to='prospectus/',null=True,blank=True)
    Meritlist = models.FileField(upload_to='meritlist/',null=True,blank=True)
    Schedule = models.FileField( upload_to='schedule/',null=True,blank=True)
    Allottedlist = models.FileField(upload_to='Allottedlist/',null=True,blank=True)
    Amendments = models.FileField( upload_to='amendments/',null=True,blank=True)
    Cutoff = models.FileField(upload_to='cutoff/',null=True,blank=True)

    def __str__(self) :
        return f'{self.Session} - {self.Course}'
    































# # Custom validator for session format

# def validate_session(value):
#     if not re.match(r'^\d{4} - \d{4}$', value):
#         raise ValidationError('Session must be in the format YYYY - YYYY.')


# # MODELS :---->



# class prevyearinfo(models.Model):
#     sno = models.IntegerField()
#     session = models.CharField(max_length=11, validators=[validate_session])
#     course = models.CharField(max_length=50)
#     prospectus = models.FileField(upload_to='prospectus/', blank=True, null=True)
#     meritlist = models.FileField(upload_to='meritlist/', blank=True, null=True)
#     schedule = models.FileField(upload_to='schedule/', blank=True, null=True)
#     allottedlist = models.FileField(upload_to='allottedlist/', blank=True, null=True)
#     amendments = models.FileField(upload_to='amendments/', blank=True, null=True)
#     cutoff = models.FileField(upload_to ='cutoff/', blank=True, null=True)

#     def __str__(self) :
#         return f'{self.course} - {self.session}'




#         # DELETING FILES IF WE DELETE THE DETAILS IN ADMIN PANEL----->


#     def delete(self, *args, **kwargs):
       
#         if self.prospectus:
#             if os.path.isfile(self.prospectus.path):
#                 os.remove(self.prospectus.path)

#         if self.meritlist:
#             if os.path.isfile(self.meritlist.path):
#                 os.remove(self.meritlist.path)

#         if self.schedule:
#             if os.path.isfile(self.schedule.path):
#                 os.remove(self.schedule.path)

#         if self.allottedlist:
#             if os.path.isfile(self.allottedlist.path):
#                 os.remove(self.allottedlist.path)

#         if self.amendments:
#             if os.path.isfile(self.amendments.path):
#                 os.remove(self.amendments.path)

#         if self.cutoff:
#             if os.path.isfile(self.cutoff.path):
#                 os.remove(self.cutoff.path)
        
#         super(prevyearinfo, self).delete(*args, **kwargs)
