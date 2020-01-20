from django.views import View
from invGateProject import settings
from django.http import HttpResponse
from django.db.models import Max
from django.db.models.functions import Greatest

from .models import WordCounter

import logging
import json
import requests
import os

logger = logging.getLogger(__name__)


class WordView(View):

    def get(self, request):

        # Valida el parametro de entrada
        word = request.GET.get('word', None)
        if word is None:
            return HttpResponse(json.dumps({'status': 'error', 'message': 'Falta el parametro de entrada'}),
                                status=400,
                                content_type="application/json")

        # Consulta a la API de invGate
        main_url = settings.config['master']['url']
        endpoint = settings.config['master']['endpoint']
        api_url = os.path.join(main_url, endpoint)
        headers = {
            'Accept': 'application/json',
            'Content-type': 'application/json'
        }
        body = {
            'keywords': word,
            'limit': 0,
        }

        req = requests.get(api_url,
                           headers=headers,
                           params=body,
                           auth=(settings.username, settings.password))

        count_result = 0
        if req.status_code == 200:
            req_json = req.json()
            if req_json['status'] == 'OK':
                count_result = len(req_json['data'])

        # Persiste en la DB la palabra buscada
        wordObj, created = WordCounter.objects.get_or_create(word=word)
        if created:
            wordObj.count = 1
        else:
            wordObj.count += 1
        wordObj.save()

        # Retorna el resultado
        return HttpResponse(json.dumps({'status': 'success', 'result': '{:d}'.format(count_result)}),
                            status=200,
                            content_type='application/json')


class MostWantedView(View):

    def get(self, request):

        args = WordCounter.objects.all()
        result_query = args.aggregate(Max('count'))

        result_count = None
        if 'count__max' in result_query:
            result_count = result_query['count__max']

            words = WordCounter.objects.filter(count=result_count)
            word_list = []
            for w in words:
                word_list.append(w.word)

        return HttpResponse(json.dumps({'status': 'success',
                                        'result': {'count': result_count, 'word_list': word_list}}),
                            status=200,
                            content_type='application/json')
