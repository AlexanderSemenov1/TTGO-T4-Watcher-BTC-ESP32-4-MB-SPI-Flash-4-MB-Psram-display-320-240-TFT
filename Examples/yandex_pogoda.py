# Test to download git
# Пример получения данных о погоде от Яндекс
# Кабинет разработчика  https://developer.tech.yandex.ru/?from=commercial  в котором нужно получит ключ доступа к API
import urequests, json

url = "https://api.weather.yandex.ru/v1/informers?lat=55.753215&lon=37.622504"  # Moscow
key = {'X-Yandex-API-Key': 'здесь должен быть ключ'}

gets = urequests.get(url, headers=key)
k = gets.json()


print(k)
