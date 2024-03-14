from django.db import models

# Create your models here.
class Question(models.Model):
    """This class defines a model for questions within the application.
    A question is characterized by its question text (`question_text`)
    and the date and time it was published (`pub_date`).

    :attribute question_text (CharField): The text of the question (max length 200 characters).
    :attribute pub_date (DateTimeField): The date and time the question was published.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """This method returns a string representation of the question object.

        :returns: string representation of 'question_text' attribute

        :rtype: str
        """
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text