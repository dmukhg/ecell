from ecell2.conman.core.models import Incubation, Updates
from forms import incubationForm, updateForm 

handlers = { 'incubation' : {'model' : Incubation,
                             'fields': ['pk','name','description','published'],
                             'form'  : incubationForm
                            },
             'update' :     {'model' : Updates,
                             'fields': ['pk','description','url','active'],
                             'form'  : updateForm
                             },
           }
