from django.shortcuts import render
from django.http import JsonResponse
from .mpesa import AccessToken, Password
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def pay(request):
    return render(request, 'pay.html')

def stk(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        amount = request.POST.get('amount')

        if not phone or not amount:
            return JsonResponse({"error": "Missing phone or amount"}, status=400)

        access_token = AccessToken.get_access_token()
        apiurl = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

        headers = {'Authorization': f"Bearer {access_token}", 'Content-Type': 'application/json'}

        payload = {
            "BusinessShortCode": Password.shortcode,
            "Password": Password.decoded_password,
            "Timestamp": Password.timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": int(amount),
            "PartyA": phone,
            "PartyB": Password.shortcode,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa",
            "AccountReference": "Alex",
            "TransactionDesc": "Product Payment",
        }

        response = requests.post(apiurl, headers=headers, json=payload)
        saf_response = response.json()

        # ✅ Return only "success" if ResponseCode is "0"
        if saf_response.get("ResponseCode") == "0":
            return JsonResponse({"message": "success"})
        else:
            return JsonResponse({"message": "failed", "error": saf_response.get("ResponseDescription")}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)



