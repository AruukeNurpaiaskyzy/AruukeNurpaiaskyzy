from django.shortcuts import render
from apps.base.models import Index, About, Action, Image, Team, Jobs, Create, Titled, Column, Response, Navigation, Work, Conversation, Clients, Services, Design, Plans, Standart, Blog, Theend
# Create your views here.

def index(request):
    index = Index.objects.all()
    about = About.objects.all().order_by('?')[:3]
    action = Action.objects.all()
    image_id = Image.objects.latest('id')
    team = Team.objects.latest('id')
    jobs = Jobs.objects.all()
    create = Create.objects.latest('id')
    titled = Titled.objects.latest('id')
    column = Column.objects.latest('id')
    response = Response.objects.latest('id')
    navigation = Navigation.objects.latest('id')
    work = Work.objects.latest('id')
    conversation = Conversation.objects.latest('id')
    clients = Clients.objects.all()
    services = Services.objects.latest('id')
    design = Design.objects.all()
    plans = Plans.objects.latest('id')
    standart = Standart.objects.all()
    blog = Blog.objects.all()
    theend = Theend.objects.latest('id')
    return render(request, "index.html", locals())

