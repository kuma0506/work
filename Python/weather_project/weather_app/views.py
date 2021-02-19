import locale
from datetime import date
import datetime
import requests
from django.http import HttpResponse
from django.shortcuts import render
from weather_app.models import Country
from .models import Country, CountryAcs
import json
from django.http.response import JsonResponse


def index(request):
    # 今日の日付取得
    today = day_of_the_week(date.today(), flag=1)
    # 画面コンボボックスの国名（日本語）をIDの昇順で取得する
    Countries = Country.objects.all().order_by('id')
    # 検索履歴「CountryAcs」の上位5件を「CountryAcs.Id」の降順で取得する
    Country_Acs = CountryAcs.objects.all().order_by('-id')[:5]

    # 天気予報情報を格納する配列
    weather_infos = []
    # 検索履歴「CountryAcs」の上位5件の天気予報情報を取得し、天気予報情報ｓに格納する
    for r in Country_Acs:
        Country_info = Country.objects.get(id=r.Country_id)
        r = weather_info(Country_info, flag=1)
        # 天気予報情報取得

        city_weather = {
            'city': Country_info.CountryName_Ja,            # 都市
            'country_id': Country_info.id,                  # 都市ID
            'icon': r['weather'][0]['icon'],                # 天気アイコン
            'temperature_max': r['main']['temp_max'],       # 最高気温
            'temperature_min': r['main']['temp_min'],       # 最低気温
            'humidity': r['main']['humidity'],              # 湿度（%）
        }
        weather_infos.append(city_weather)

    return render(request, 'weather_app/index.html', {'today': today, 'Countries': Countries, 'weather_infos': weather_infos})


def search(request):
    # 画面入力値のIDから国情報を取得する
    Country_info = Country.objects.get(pk=request.POST.get('CountryId'))
    # search(3日間の予報)
    r = weather_info(Country_info, flag=2)
    try:
        city_weather = {
            'city': Country_info.CountryName_Ja,                                             # 都市
            'cityid': Country_info.id,                                                       # 都市ID
            # 当日の天気予報
            'days_0': day_of_the_week(date.today(), flag=2),                                 # 当日_日付
            'icon_0': r[0]['weather'][0]['icon'],                                    # 当日_天気アイコン
            'temperature_max_0': r[0]['main']['temp_max'],                           # 当日_最高気温
            'temperature_min_0': r[0]['main']['temp_min'],                           # 当日_最低気温
            'humidity_0': r[0]['main']['humidity'],                                  # 当日_湿度（%）
            # 翌日の天気予報
            'days_1': day_of_the_week(date.today() + datetime.timedelta(days=1), flag=2),    # 翌日_日付
            'icon_1': r[7]['weather'][0]['icon'],                                    # 翌日_天気アイコン
            'temperature_max_1': r[7]['main']['temp_max'],                           # 翌日_最高気温
            'temperature_min_1': r[7]['main']['temp_min'],                           # 翌日_最低気温
            'humidity_1': r[7]['main']['humidity'],                                  # 翌日_湿度（%）
            # 翌々日の天気予報
            'days_2': day_of_the_week(date.today() + datetime.timedelta(days=2), flag=2),    # 翌々日_日付
            'icon_2': r[15]['weather'][0]['icon'],                                   # 翌々日_天気アイコン
            'temperature_max_2': r[15]['main']['temp_max'],                          # 翌々日_最高気温
            'temperature_min_2': r[15]['main']['temp_min'],                          # 翌々日_最低気温
            'humidity_2': r[15]['main']['humidity'],                                 # 翌々日_湿度（%）
        }

        # 3時間ごとの予報を取得する
        # search,ajax(3時間ごとの予報)
        r = weather_info(Country_info, flag=3)

        print('-----------------------------------------------------')
        print(r)
        print('-----------------------------------------------------')


        # 日付、曜日のリストを取得する
        days = days_list(r)
        weather_after_Three_hours = weather_info_list(days, r)
        context = {'city_weather': city_weather, 'weather_after_Three_hours': weather_after_Three_hours}

        # 検索履歴「CountryAcs」の上位5件を「CountryAcs.Id」の降順で取得する
        Country_Acs = CountryAcs.objects.all().order_by('-id')[:5]

        for r in Country_Acs:
            # 検索履歴「CountryAcs」の上位5件中に画面入力値と同じデータが存在すれば削除する
            if r.Country_id == Country_info.id:
                CountryAcs.objects.filter(Country_id=Country_info.id).delete()

        # 画面入力値のIDを検索履歴として、「CountryAcs」にINSERTする
        CountryAcs.objects.create(Country_id=Country_info.id)
        return render(request, 'weather_app/weather.html', context)

    except KeyError:
        return render(request, 'weather_app/weather.html', {'flag': True})


# オープンウェザーマップ情報を取得する
def weather_info(Country_info, flag):
    # index用
    if flag == 1:
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=944bb06989061f3b648dc2c61cfa3f68"
        return requests.get(url.format(Country_info.CountryName_En)).json()
    # search(3日間の予報)
    elif flag == 2:
        sample = "http://api.openweathermap.org/data/2.5/forecast?q={}&appid=944bb06989061f3b648dc2c61cfa3f68&lang=ja&units=metric"
        list = {
            0:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][0],
            7:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][7],
            15: requests.get(sample.format(Country_info.CountryName_En)).json()['list'][15]
        }
        return list
    # search,ajax(3時間ごとの予報)
    elif flag == 3:
        sample = "http://api.openweathermap.org/data/2.5/forecast?q={}&appid=944bb06989061f3b648dc2c61cfa3f68&lang=ja&units=metric"
        list = {
            0:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][0],
            1:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][1],
            2:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][2],
            3:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][3],
            4:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][4],
            5:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][5],
            6:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][6],
            7:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][7],
            8:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][8],
            9:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][9]
        }
        return list
    # ajax(6時間ごとの予報)
    elif flag == 4:
        sample = "http://api.openweathermap.org/data/2.5/forecast?q={}&appid=944bb06989061f3b648dc2c61cfa3f68&lang=ja&units=metric"
        list = {
            0:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][0],
            1:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][2],
            2:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][4],
            3:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][6],
            4:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][8],
            5:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][10],
            6:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][12],
            7:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][14],
            8:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][16],
            9:  requests.get(sample.format(Country_info.CountryName_En)).json()['list'][18]
        }
        return list

    else:
        return HttpResponse('error')


def day_of_the_week(days, flag):
    # index用
    if flag == 1:
        day = days.strftime('%Y/%m/%d')
    # search_city_weather用
    elif flag == 2:
        day = days.strftime('%m/%d')
    else:
        return HttpResponse('error')
    youbi = days.strftime('%a')
    return day+youbi_Change(youbi)

# 日付、曜日のリストを取得する
def days_list(r):
    # 日付を格納する配列、最初の値 or 時刻が0：00の時のみセットする
    days = []
    # 日付を比較する用の変数
    compare_dates = ""
    for i in range(10):
        day_Youbi = ""
        # 日にちを取得する『yyyy/MM/dd』
        day = datetime.datetime.fromtimestamp(r[i]['dt']).strftime('%Y/%m/%d')
        # 時間を取得する『HH:MM』
        time  = datetime.datetime.fromtimestamp(r[i]['dt']).strftime('%H:%M')
        # 英語の曜日を日本語に変換する
        youbi = youbi_Change(datetime.datetime.fromtimestamp(r[i]['dt']).strftime('%a'))
        # 最初の0件目に日付、曜日をセットする「mm/dd(*)」
        if i == 0:
            day_Youbi = datetime.datetime.fromtimestamp(r[i]['dt']).strftime('%m/%d')+youbi
            # 日付が変わった場合、日付をセットする「dd(*)」
        elif compare_dates != day:
            day_Youbi = datetime.datetime.fromtimestamp(r[i]['dt']).strftime('%d')+youbi
        days.append(day_Youbi)
        # 日付を更新する
        compare_dates = day
    return days


# 英語の曜日を日本語に変換する
def youbi_Change(youbi_En):
    if youbi_En == "Sun":
        youbi = "（日）"
    elif youbi_En == "Mon":
        youbi = "（月）"
    elif youbi_En == "Tue":
        youbi = "（火）"
    elif youbi_En == "Wed":
        youbi = "（水）"
    elif youbi_En == "Thu":
        youbi = "（木）"
    elif youbi_En == "Fri":
        youbi = "（金）"
    elif youbi_En == "Sat":
        youbi = "（土）"

    return youbi


def test(request):
    return render(request, 'weather_app/test.html')


def weather_info_list(days, r):
    weather_after_Three_hours = {
        'days_01': days[0],
        'days_02': days[1],
        'days_03': days[2],
        'days_04': days[3],
        'days_05': days[4],
        'days_06': days[5],
        'days_07': days[6],
        'days_08': days[7],
        'days_09': days[8],
        'days_10': days[9],
        'times_01': datetime.datetime.fromtimestamp(r[0]['dt']).strftime('%H:%M'),
        'times_02': datetime.datetime.fromtimestamp(r[1]['dt']).strftime('%H:%M'),
        'times_03': datetime.datetime.fromtimestamp(r[2]['dt']).strftime('%H:%M'),
        'times_04': datetime.datetime.fromtimestamp(r[3]['dt']).strftime('%H:%M'),
        'times_05': datetime.datetime.fromtimestamp(r[4]['dt']).strftime('%H:%M'),
        'times_06': datetime.datetime.fromtimestamp(r[5]['dt']).strftime('%H:%M'),
        'times_07': datetime.datetime.fromtimestamp(r[6]['dt']).strftime('%H:%M'),
        'times_08': datetime.datetime.fromtimestamp(r[7]['dt']).strftime('%H:%M'),
        'times_09': datetime.datetime.fromtimestamp(r[8]['dt']).strftime('%H:%M'),
        'times_10': datetime.datetime.fromtimestamp(r[9]['dt']).strftime('%H:%M'),
        'icon_01': r[0]['weather'][0]['icon'],
        'icon_02': r[1]['weather'][0]['icon'],
        'icon_03': r[2]['weather'][0]['icon'],
        'icon_04': r[3]['weather'][0]['icon'],
        'icon_05': r[4]['weather'][0]['icon'],
        'icon_06': r[5]['weather'][0]['icon'],
        'icon_07': r[6]['weather'][0]['icon'],
        'icon_08': r[7]['weather'][0]['icon'],
        'icon_09': r[8]['weather'][0]['icon'],
        'icon_10': r[9]['weather'][0]['icon'],
        'temp_01': r[0]['main']['temp'],
        'temp_02': r[1]['main']['temp'],
        'temp_03': r[2]['main']['temp'],
        'temp_04': r[3]['main']['temp'],
        'temp_05': r[4]['main']['temp'],
        'temp_06': r[5]['main']['temp'],
        'temp_07': r[6]['main']['temp'],
        'temp_08': r[7]['main']['temp'],
        'temp_09': r[8]['main']['temp'],
        'temp_10': r[9]['main']['temp'],
        'humidity_01': r[0]['main']['humidity'],
        'humidity_02': r[1]['main']['humidity'],
        'humidity_03': r[2]['main']['humidity'],
        'humidity_04': r[3]['main']['humidity'],
        'humidity_05': r[4]['main']['humidity'],
        'humidity_06': r[5]['main']['humidity'],
        'humidity_07': r[6]['main']['humidity'],
        'humidity_08': r[7]['main']['humidity'],
        'humidity_09': r[8]['main']['humidity'],
        'humidity_10': r[9]['main']['humidity'],
        'speed_01': r[0]['wind']['speed'],
        'speed_02': r[1]['wind']['speed'],
        'speed_03': r[2]['wind']['speed'],
        'speed_04': r[3]['wind']['speed'],
        'speed_05': r[4]['wind']['speed'],
        'speed_06': r[5]['wind']['speed'],
        'speed_07': r[6]['wind']['speed'],
        'speed_08': r[7]['wind']['speed'],
        'speed_09': r[8]['wind']['speed'],
        'speed_10': r[9]['wind']['speed'],
    }
    return weather_after_Three_hours


def every_hours_ajax(request):
    # 3 or 6取得
    time = request.GET.get('time')
    cityid = request.GET.get('countryId')

    # 画面入力値のIDから国情報を取得する
    Country_info = Country.objects.get(pk=request.GET.get('countryId'))

    # 3時間ごとの予報の場合、
    if time == '3':
        # 天気予報情報を取得する
        r = weather_info(Country_info, flag=3)
        # 日付、曜日のリストを取得する
        days = days_list(r)
        weather_after_Three_hours = weather_info_list(days, r)
        return JsonResponse(weather_after_Three_hours)
    # 6時間ごとの予報の場合、
    elif time == '6':
        # 天気予報情報を取得する
        r = weather_info(Country_info, flag=4)
        # 日付、曜日のリストを取得する
        days = days_list(r)
        weather_after_six_hours = weather_info_list(days, r)
        return JsonResponse(weather_after_six_hours)
    else:
        return HttpResponse('error')
