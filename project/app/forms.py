from django import forms
froms .models import Department, Course, subject, Exam, Student_Attendance,
from django.contrib.auth.models import User
from django.forms import CharField

# Add/ Edit Student create_profile

class UpdateStudentProfile(forms.modelForm):
    is_super = forms.BooleanField(required=False)
    class Meta:
        model = Student
        fields = ('user','first_name','last_name','email','department','course')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['user'].widget.attrs.update({'hidden':True})
        self.fields['first_name'].widget.attrs.update({'class':'form-control', 'placeholder':'First Name'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control', 'placeholder':'Last Name'})
        self.fields['email'].widget.attrs.update({'class':'form-control', 'placeholder':'Email'})
        self.fields['department'].widget.attrs.update({'class':'form-control', 'placeholder':'Department'})
        self.fields['course'].widget.attrs.update({'class':'form-control', 'placeholder':'Course'})

# signup forms
class SignUpForm(forms.Forms):
    username = forms.CharField()
    password1 = forms.CharField(widget = forms.Passwordinput())
    password2 = forms.CharField(widget = forms.Passwordinput())

    def clean_username(self):
        try:
            User.object.get(username__iexact=self.username)
            raise forms.ValidationError('User already exist')
        except User.DoesNotExist:
            return self.username

    def clean_password(self):
        pwd1 = self.cleaned_data.get('password1')
        pwd2 = self.cleaned_data.get('password2')

        if pwd1 and pwd2 and pwd1 == pwd2:
            return pwd1
        raise forms.ValidationError("Password dosent Match")

# student ATTENDANCE
class StudentAttendanceForm(forms.ModelForm):
    is_super = forms.BooleanField(required=True)

    class Meta:
        model = Student_Attendance
        fields = ('student','date','present')

    def __init__(self,*args,**kwargs):
        super(StudentAttendanceForm,self).__init__(*args,**kwargs)
        self.fields['student'].widget.attrs.update({'class':'form-control'})
        self.fields['date'].widget.attrs.update({'class':'form-control'})
        self.fields['present'].widget.attrs.update({'class':'form-control'})

class ExamForm(forms.ModelForm):
    is_super = forms.BooleanField(required=True)

    class Meta:
        model = Exam
        fields = ('course','student','subject','date','student_marks')

        def __init__(self,*args,**kwargs):
            super(ExamForm,self).__init__(*args,**kwargs)
            self.fields['course'].widget.attrs.update({'class':'form-control'})
            self.fields['student'].widget.attrs.update({'class':'form-control'})
            self.fields['subject'].widget.attrs.update({'class':'form-control'})
            self.fields['date'].widget.attrs.update({'class':'form-control'})
            self.fields['student_marks'].widget.attrs.update({'class':'form-control'})
