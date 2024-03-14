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

        :returns: string representation of 'question_text' attribute.

        :rtype: str
        """
        return self.question_text


class Choice(models.Model):
    """This class defines a model for choices within the application.
    A choice is associated with a specific question (`question`) through a
    foreign key relationship. It has a `choice_text` field to store the text of 
    the choice (max length 200 characters) and a `vote` field (IntegerField) 
    to keep track of the number of votes received.

    :Attribute question (ForeignKey): A foreign key relationship to the Question model.
    :Attribute choice_text (CharField): The text of the choice (max length 200 characters).
    :Attribute vote (IntegerField): The number of votes received by this choice (default 0).
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        """This method is used by Django to represent the choice object as a string.

        :returns: string representation of 'choice_text' attribute.

        :rtype: str
        """
        return self.choice_text