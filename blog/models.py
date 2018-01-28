from django.db import models



class Post(models.Model):
	post_title = models.CharField(max_length=2000)
	post_main_image = models.CharField(max_length=3000)
	pub_date = models.DateTimeField('date published')
	votes = models.IntegerField(default=0)
	category = models.CharField(max_length=200, default='general')
	def __str__(self):
		return self.post_title

class Comment(models.Model):
	comment_author = models.CharField(max_length=200)
	comment_text = models.TextField()
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	def __str__(self):
		return self.comment_author

class SiteImage(models.Model):
	image = models.CharField(max_length=3000)
	alt = models.CharField(max_length=2000, default='image')
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	def __str__(self):
		return self.alt

class SiteLink(models.Model):
	link = models.CharField(max_length=3000)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	def __str__(self):
		return self.link

class Paragraph(models.Model):
	paragraph_title = models.CharField(max_length=2000)
	paragraph_text = models.TextField()
	paragraph_image = models.CharField(max_length=3000, blank=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	def __str__(self):
		return self.paragraph_title