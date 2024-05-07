from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _

class ClearableMultipleFileInput(ClearableFileInput):
    initial_text = _('현재 이미지')
    input_text = _('새 이미지 업로드')
    clear_checkbox_label = _('이미지 삭제')
    template_name = 'widgets/clearable_file_input.html'
    multiple = True  
