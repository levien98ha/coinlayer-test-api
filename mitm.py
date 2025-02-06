from mitmproxy import http
import csv

def export_csv(rates):
  csv_file = 'crypto_rates.csv'
  with open(csv_file, mode='w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(['Currency', 'Rate'])
      
      for currency, rate in rates.items():
          writer.writerow([currency, rate])

def mitm_response(response):
    rates = response['rates']
    export_csv(rates)
    print(f"{'Currency':<10} {'Rate':<15}")
    print("-" * 25)
    for currency, rate in rates.items():
        print(f"{currency:<10} {rate:<15}")

def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_host == "api.coinlayer.com":
        print("Original Request Headers:", flow.request.headers)
        flow.request.headers["mitm_config"] = "test"
        print("Modified Request Headers:", flow.request.headers)
    else:
        print("Request to a different endpoint:", flow.request.url)

    print("Request URL:", flow.request.url)
    print("Request Method:", flow.request.method)
    print("Request Headers:", flow.request.headers)
    print("Request to a different endpoint:", flow.request.path)


def response(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_host == "api.coinlayer.com":
        response_format = flow.response.json()
        if response_format["success"]:
            mitm_response(response_format)
            return response_format
        print("Response Status Code:", flow.response)
        print("Response Content:", flow.response.text)