import requests

def exchange_som(som):
    url = 'https://mbank.cbk.kg/svc-biz-ib-cbk-currencies/v1/unauthorized-api/private/currencies/exchange-rates'
    response = requests.get(url)

    data = response.json()
    result = {}
    kef_eur = data['rates'][0]['to'][0]['sell']
    kef_usd = data['rates'][2]['to'][1]['sell']
    kef_rub = data['rates'][3]['to'][1]['sell']
    result['euro'] = som/float(kef_eur)
    result['usd'] = som/float(kef_usd)
    result['rub'] = som/float(kef_rub)

    return f"Ваши {som} сомов будут {round(result['euro'],2)} евро, {round(result['usd'],2)} долларов и {round(result['rub'], 2)} рублей"