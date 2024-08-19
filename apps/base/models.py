from django.db.models import * 

# Create your models here.
class Index(Model):
    title = CharField(
        max_length=255,
        verbose_name='Заголовок сайта (на главной странице)'
    )
    description = TextField(
        verbose_name="Описание сайта ()"
    )
    logo = ImageField(
        upload_to='image/',
        verbose_name='Логотип'
    )
    banner = ImageField(
        upload_to='image/'
    )
    twitter = URLField(
        verbose_name='Укжите ссылку на twitter'
    )
    facebook = URLField(
        verbose_name='Укжите ссылку на facebook'
    )
    github = URLField(
        verbose_name='Укжите ссылку на github'
    )
    gmail = URLField(
        verbose_name='Укжите ссылку на почту'
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки главной страницы'


class About(Model):
    title = CharField(
    max_length = 255,
    verbose_name = "Название информации"
                )
    description = TextField(
    verbose_name="Описание информации"
                )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

class Action(Model):
    title = CharField(
    max_length = 255,
    verbose_name = "Название действия"
                )
    description = TextField(
    verbose_name="Описание действия"
                )
    image = ImageField(
        upload_to = "action_image",
        verbose_name="фото"

    )
    desc_image = CharField(
    max_length = 255,
    verbose_name = "Описание фото"
                )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'действие'
        verbose_name_plural = 'действии'


class Image(Model):
    photo = ImageField(
         upload_to = "actional_image",
        verbose_name="фотки"

    )
    photo2 = ImageField(
         upload_to = "actional_image",
        verbose_name="фотки"

    )

    class Meta:
        verbose_name = 'фотографии'
        verbose_name_plural = 'фотографии'

class Team(Model):
    title = CharField(
    max_length = 255,
    verbose_name = "Название тайтла"
                )
    description = TextField(
    verbose_name="Описание тайтла"
    )

    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = 'название'
        verbose_name_plural = 'названии'
class Jobs(Model):
    title = CharField(
    max_length = 255,
    verbose_name = "Фио"
                )
    description = TextField(
    verbose_name="Деятельность"
    )
    image = ImageField(
        upload_to='jobs',
        verbose_name='Фото'
    )

    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'неймес'
class Create(Model):
    title = CharField(
    max_length = 255,
    verbose_name = "опять название"
                )
    description = TextField(
    verbose_name="опять описание"
    )
    image = ImageField(
        upload_to='jobs',
        verbose_name='Фото'
    )


    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'криэйшны '
class Titled(Model):
    title = CharField(
    max_length = 255,
    verbose_name = "название тайла"
                )
    description = TextField(
    verbose_name="описание тайтла"
    )
    image = ImageField(
        upload_to='jobs',
        verbose_name='Фото'
    )


    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'тайтлед'
class Column(Model):
    title = CharField(
    max_length = 255,
    verbose_name = "название колумна"
                )
    description = TextField(
    verbose_name="описание колумна"
    )
    image = ImageField(
        upload_to='jobs',
        verbose_name='Фото'
    )


    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'колумны'
class Response(Model):
    title = CharField(
    max_length = 255,
    verbose_name = "название респонса"
                )
    description = TextField(
    verbose_name="описание респонса"
    )
    image = ImageField(
        upload_to='jobs',
        verbose_name='Фото'
    )


    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'респонса'
class Navigation(Model):
    title = CharField(
    max_length = 255,
    verbose_name = "название навигации"
                )
    description = TextField(
    verbose_name="описание навигации"
    )
    image = ImageField(
        upload_to='jobs',
        verbose_name='Фото'
    )


    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'навигации'
class Work(Model):
    title = CharField(
    max_length = 255,
    verbose_name = "название работы"
                )
    description = TextField(
    verbose_name="описание работы"
    )
    image = ImageField(
        upload_to='jobs',
        verbose_name='Фото'
    )


    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'работы'
class Conversation(Model):
    title = CharField(
    max_length = 255,
    verbose_name = "название общении"
                )


    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'общении'      

class Clients(Model):
    title = CharField(
    max_length = 255,
    verbose_name = "кол во клиентов"
                )
    description = TextField(
    verbose_name="описание клиента"
                )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'клиенты'
class Services(Model):
    title = CharField(
    max_length = 255,
    verbose_name = "тайтл"
                )
    description = TextField(
    verbose_name="описание тайтла"
                )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'сервисы'

class Design(Model):
    title = CharField(
    max_length = 255,
    verbose_name = "название дизайна"
                )
    description = TextField(
    verbose_name="описание дизайна"
                )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'дизайны'
class Plans(Model):
    title = CharField(
    max_length = 255,
    verbose_name = "название плана"
                )
    description = TextField(
    verbose_name="описание плана"
                )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'планы'
class Standart(Model):
    title = CharField(
    max_length = 255,
    verbose_name = "сумма"
                )
    title = CharField(
    max_length = 255,
    verbose_name = "вид"
                )
    description = TextField(
    verbose_name="описание "
                )
    description = TextField(
    verbose_name="описание "
                )
    description = TextField(
    verbose_name="описание "
                )
    description = TextField(
    verbose_name="описание "
                )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'стандарты'
class Blog(Model):
    title = CharField(
    max_length = 255,
    verbose_name = "название "
                )
    description = TextField(
    verbose_name="описание "
                )
    image = ImageField(
        upload_to='jobs',
        verbose_name='Фото'
    )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'блоги'
class Theend(Model):
    title = CharField(
    max_length = 255,
    verbose_name = "название"
    )
    description = TextField(
    verbose_name  = "описание"
    )
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'концы'
        

        
        

