from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    description = models
    author_image = models.ImageField(upload_to='authors/', blank=True, null=True)
    job_title = models.CharField(max_length=50)
    view_count = models.IntegerField(default=0)
    product_designer = models.CharField(max_length=100)

    is_published = models.BooleanField(default=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    name = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    email = models.EmailField()
    message = models.TextField()

    is_published = models.BooleanField(default=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    is_solved = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
