from django import forms
from .widgets import PawnWidget


class PawnFormField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super(PawnFormField, self).__init__(*args, **kwargs)

        if issubclass(self.widget.__class__, forms.widgets.MultiWidget):
            is_pawn_widget = any(
                issubclass(item.__class__, PawnWidget)
                for item in getattr(self.widget, 'widgets', list())
            )

            if not is_pawn_widget:
                self.widget = PawnWidget()

        elif not issubclass(self.widget.__class__, PawnWidget):
            self.widget = PawnWidget()