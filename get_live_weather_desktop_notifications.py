import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

notifier = ToastNotifier()


def getdata(url):
    request = requests.get(url)

    return request.text


htmldata = getdata("https://weather.com/en-US/weather/today/l/37.06,37.38?par=google")
soup = BeautifulSoup(htmldata, 'html.parser')

get_weather = soup.find("section", {"data-testid": "HourlyWeatherModule"})
temp = get_weather.find("span", {"data-testid": "TemperatureValue"}).text
chance_rain = get_weather.find("div", {"data-testid": "SegmentPrecipPercentage"}).find(
    "span", class_="Column--precip--3JCDO").text.split("in",)[1]

result = "The temperature {} in Gaziantep".format(temp) + "\n" + "{} chance of rain".format(chance_rain)
print(result)
notifier.show_toast("Weather update", result, duration=10)
