from django.db import models

# Create a Blog model
# title
# pub_date
# body
# image

# create blog app to settings
# create a migration
# migrate the things
# add to admin


class Blog (models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=700)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        retstr = str(self.pk) + ". " + self.title + " - " +self.pub_date.strftime('%b %e %Y')
        return retstr

    def summary_body(self):
        return self.body[0:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    
    def returnId(self):
        return self.pk



