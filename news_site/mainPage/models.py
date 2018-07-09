from django.db import models

SHORT_TEXT_LEN = 200

class News(models.Model):
	title = models.CharField(max_length=500, verbose_name = 'Заголовок')
	descriptions = models.TextField(verbose_name = 'Информация')
	date = models.DateTimeField(auto_now = True, verbose_name = 'Дата')

	def __str__(self):
		return self.title

	def get_short_text(self):
		if len(self.descriptions) > SHORT_TEXT_LEN:
			return self.descriptions[:SHORT_TEXT_LEN]
		else:
			return self.descriptions

	class Meta:
		verbose_name = 'Новости'
		verbose_name_plural = 'Новости'

