from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
    target = models.TextField(default=None, null=True)
    block_1_text = models.TextField(default=None, null=True)
    block_1_image = models.FilePathField(path="/img", default=None, null=True)
    block_2_text = models.TextField(default=None , null=True)
    block_2_image = models.FilePathField(path="/img" , default=None , null=True)
    block_3_text = models.TextField(default=None , null=True)
    block_3_image = models.FilePathField(path="/img" , default=None , null=True)

    paragraph_txt_1 = models.TextField(default=None, null=True)
    paragraph_img_1 = models.FilePathField(path="/img" , default=None , null=True)

    paragraph_txt_2 = models.TextField(default=None , null=True)
    paragraph_img_2 = models.FilePathField(path="/img" , default=None , null=True)

    paragraph_txt_3 = models.TextField(default=None , null=True)
    paragraph_img_3 = models.FilePathField(path="/img" , default=None , null=True)

    paragraph_txt_4 = models.TextField(default=None , null=True)
    paragraph_img_4 = models.FilePathField(path="/img" , default=None , null=True)

    paragraph_txt_5 = models.TextField(default=None , null=True)
    paragraph_img_5 = models.FilePathField(path="/img" , default=None , null=True)

    paragraph_txt_6 = models.TextField(default=None , null=True)
    paragraph_img_6 = models.FilePathField(path="/img" , default=None , null=True)

    paragraph_txt_7 = models.TextField(default=None , null=True)
    paragraph_img_7 = models.FilePathField(path="/img" , default=None , null=True)

    paragraph_txt_8 = models.TextField(default=None , null=True)
    paragraph_img_8 = models.FilePathField(path="/img" , default=None , null=True)

    paragraph_txt_9 = models.TextField(default=None , null=True)
    paragraph_img_9 = models.FilePathField(path="/img" , default=None , null=True)

    paragraph_txt_10 = models.TextField(default=None , null=True)
    paragraph_img_10 = models.FilePathField(path="/img" , default=None , null=True)

    # сылку на гитхаб надо еще