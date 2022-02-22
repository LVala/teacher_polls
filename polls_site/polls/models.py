from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=200)
    plot_image = models.ImageField

    def __str__(self):
        return self.name

class Choice(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
    total_voters_number = models.IntegerField(default=0)
    total_quality = models.IntegerField(default=0)
    total_friendliness = models.IntegerField(default=0)
    total_motivation = models.IntegerField(default=0)
    total_ease = models.IntegerField(default=0)

    class Meta:
        unique_together = ('teacher', 'subject')

    def get_score(self, attr: str):
        if attr == 'total_general':
            return (self.get_score('total_quality') + self.get_score('total_friendliness') + self.get_score('total_motivation') +self.get_score('total_ease'))/4
        else:
            if self.total_voters_number > 0:
                return self.__getattribute__(attr)/self.total_voters_number
            else:
                return 0

    def __str__(self):
        return f"T: {str(self.teacher)}, S: {str(self.subject)}"
            