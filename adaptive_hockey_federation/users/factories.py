import factory  # type: ignore
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    """Фабрика создания тестовых юзеров"""
    class Meta:
        model = User

    first_name = factory.Faker('first_name', locale='ru_RU')
    last_name = factory.Faker('last_name', locale='ru_RU')
    patronymic = factory.Faker('first_name', locale='ru_RU')
    email = factory.Faker('email', locale='ru_RU')
    phone = factory.Faker('phone_number', locale='ru_RU')
    password = factory.PostGenerationMethodCall('set_password', 'pass1234')

    @factory.post_generation
    def admin_create(self, create, extracted, **kwargs):
        if create:
            if self.role in ['admin', 'moderator']:
                self.is_staff = True
                if self.role == 'admin':
                    self.is_superuser = True
