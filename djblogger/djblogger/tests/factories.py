import factory
from django.contrib.auth.models import User

from djblogger.blog.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.Faker("password")
    is_staff = True
    is_superuser = True

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence")
    subtitle = factory.Faker("sentence")
    slug = factory.Faker("slug")
    author = factory.SubFactory(UserFactory)
    content = factory.Faker("paragraph")
