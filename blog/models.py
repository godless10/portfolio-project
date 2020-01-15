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




