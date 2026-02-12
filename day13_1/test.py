import requests
import base64

API_KEY = "YOUR_TEST_SECRET_KEY"
encoded_key = base64.b64encode(f"{API_KEY}:".encode()).decode()
headers = {"Authorization": f"Basic {encoded_key}"}

url = "https://sandbox.tosspayments.com/v1/payments"

data = {
    "method": "CARD",
    "amount": 1000,
    "orderId": "test_order_001",
    "orderName": "테스트 상품",
    "cardNumber": "4000000000000002",
    "cardExpirationYear": "2027",
    "cardExpirationMonth": "12",
    "cardPassword": "12",
    "customerName": "홍길동"
}

headers = {
    "Authorization": f"Basic {encoded_key}",
    "Content-Type": "application/json"
}

response = requests.post(url, json=data, headers=headers)

print(response.status_code)
# JSON이 아닐 수도 있으니 안전하게 출력
try:
    print(response.json())
except:
    print(response.text)
