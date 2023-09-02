from django.http import JsonResponse
from rest_framework.viewsets import ViewSet

from quiz.models import Country


class CheckQuizResponse(ViewSet):
    # check user provided capital respective to country
    def create(self, request):
        try:
            api_response_status_code = 200
            country_id = request.POST.get('country_id')
            user_answer = request.POST.get('user_answer')

            country = Country.objects.get(id=country_id)
            if user_answer.lower() == country.capital.lower():
                response_data = {'result': 'Correct!'}
            else:
                response_data = {'result': 'Incorrect', 'correct_answer': country.capital}

        except Country.DoesNotExist:
            api_response_status_code = 400
            response_data = {'result': 'Failed', 'message': "Country is not valid"}
        except Exception as e:
            api_response_status_code = 400
            response_data = {'result': 'Failed', 'message': "Country is not valid"}

        return JsonResponse(response_data, status=api_response_status_code)
