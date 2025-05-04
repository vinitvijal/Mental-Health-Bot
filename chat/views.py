import openai
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

@csrf_exempt
def chat_with_bot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a friendly mental health assistant. Be kind, gentle, and helpful."},
                    {"role": "user", "content": user_message}
                ]
            )

            reply = response['choices'][0]['message']['content']
            return JsonResponse({'response': reply})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
