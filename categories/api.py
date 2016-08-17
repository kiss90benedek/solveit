from django.http import HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_POST

from .models import Category


@require_POST
def create_new_category(request):
    try:
        request_data = request.POST
        Category.objects.create(
            name=request_data.get('category')
        )
        return JsonResponse({'success': 'true'})
    except TypeError:
        return HttpResponseBadRequest(content='json format is expected')
