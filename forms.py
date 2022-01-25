from .models import Task, TaskUpdate
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from django import forms


class CardForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title"]

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ["title", "status"]

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('status'),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
                )
            )
