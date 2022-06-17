from django.http import HttpResponse, JsonResponse
from django.utils.module_loading import import_string
from django.views.generic.edit import View, BaseFormView
from .settings import PAWN_MARKDOWNIFY_FUNCTION
from .forms import ImageForm

class MarkdownifyView(View):

    def post(self, request, *args, **kwargs):
        markdownify = import_string(PAWN_MARKDOWNIFY_FUNCTION)
        return HttpResponse(markdownify(request.POST['content']))

class ImageUploadView(BaseFormView):
    form_class = ImageForm
    success_url = '/'

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)

        response = super(ImageUploadView, self).form_invalid(form)
        return response

    def form_valid(self, form):
        response = super(ImageUploadView, self).form_valid(form)

        if self.request.is_ajax():
            image_path = form.save(commit=True)
            image_code = '![]({})'.format(image_path)
            return JsonResponse({'image_code': image_code})

        return response