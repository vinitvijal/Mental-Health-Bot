from openai import OpenAI
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@csrf_exempt
def chat_with_bot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a friendly mental health assistant. Be kind, gentle, and helpful."},
                    {"role": "user", "content": user_message}
                ]
            )

            reply = response.choices[0].message.content
            return JsonResponse({'response': reply})

        except Exception as e:
            return JsonResponse({'response': str(e)}, status=500)



from django.shortcuts import render

def chat_page(request):
    return render(request, "chat.html")