from django.db import models


class Survey(models.Model):
    name = models.CharField(max_length=100, blank=False)
    date_start = models.DateField(null=False)
    date_finish = models.DateField(null=False)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Question(models.Model):
    class TypeChoices(models.IntegerChoices):
        ONE = 1
        SEVERAL = 2
        TEXT = 3
    text = models.TextField(max_length=1000)
    type = models.IntegerField(choices=TypeChoices.choices, default=TypeChoices.ONE)
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE,
        related_name="questions",
        null=False,
    )

    def __str__(self):
        return f"{self.text} {self.type}"

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):


class DefaultAnswer(models.Model):
    text = models.CharField(max_length=100, blank=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="default_answers")

    def __str__(self):
        return self.text


class SurveyReport(models.Model):
    user = models.BigIntegerField(verbose_name="id пользователя", blank=False)
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE,
        related_name="reports",
        null=False,
    )


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="user_answers")
    user_answer = models.TextField(verbose_name="ответ пользователя", null=True)
    chosen_answer = models.ForeignKey(DefaultAnswer, on_delete=models.CASCADE, related_name="+", null=True)
    report = models.ForeignKey(SurveyReport, on_delete=models.CASCADE, related_name="answers")

