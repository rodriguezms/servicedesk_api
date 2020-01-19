from django.db import models

class WordCounter(models.Model):
    word = models.CharField(max_length=32, primary_key=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return "{}({})".format(self.word, self.count)

    class Meta:
        verbose_name = "Palabra"
        verbose_name_plural = "Palabras"

