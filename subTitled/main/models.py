from django.db import models

# Create your models here.

# Store piece of YT media by id, keep subtitles stored
class YTMedia(models.Model):
    title = models.CharField(max_length=200)
    yturl = models.CharField(max_length=200, unique=True)
    subtitles = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    # to get the ytID
    def getID(self):
        return (youtube_url.split('v=')[-1]).split('&')[0]


# Store words that the model identifies incorrectly
class DifficultWord(models.Model):
    word = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.word

# One-to-Many relationship between a word that has been identified incorrectly, store which word it believed
class IncorrectWord(models.Model):
    incorrect_word = models.CharField(max_length=200)
    difficult_word = models.ForeignKey(DifficultWord, related_name='incorrect_words', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.incorrect_word