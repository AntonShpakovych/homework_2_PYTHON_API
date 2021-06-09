import requests
from pprint import pprint

# URL = 'https://api.covid19api.com/summary'

# covid19 = requests.get(URL)
# covid19_global = covid19.json()["Global"]
# covid19 = covid19.json()["Countries"]
flag = True


try:
    URL = 'https://api.covid19api.com/summary'

    covid19 = requests.get(URL)

    covid19_global = covid19.json()["Global"]
    covid19 = covid19.json()["Countries"]
    # for item in covid19:
    #     print(item.values())
    while flag:
        a = int(input('\n1 - Show COVID19 information\n2 - Sort by new confirmed\n3 - Отримати детальну інформацію по назві країни\n4 - Глобальна інформація\n5 - Вихід'))
        if a == 1:
            tytles = sorted([item for item in list(covid19[0].keys()) if item not in [
                'ID', 'CountryCode', 'Slug', 'Date', 'Premium']])
            for item in tytles:
                if item == 'Country':
                    print("{0:_^30s}".format(item), end=' ')
                else:
                    print("{0:_^15s}".format(item), end=' ')
            else:
                print(' ')

            for item in covid19:
                for key in item:
                    if key in tytles:
                        if key == 'Country':
                            print("{0:<30}".format(item[key]), end=' ')
                        else:
                            print("{0:>15}".format(item[key]), end=' ')
                else:
                    print('')
        if a == 2:
            tytles = sorted([item for item in list(covid19[0].keys()) if item not in [
                'ID', 'CountryCode', 'Slug', 'Date', 'Premium']])
            for item in tytles:
                if item == 'Country':
                    print("{0:_^30s}".format(item), end=' ')
                else:
                    print("{0:_^15s}".format(item), end=' ')
            else:
                print(' ')

            def byNewConfirmed_key(covid19):
                return covid19["NewConfirmed"]

            covid19 = sorted(covid19, key=byNewConfirmed_key, reverse=True)
            for item in covid19:
                for key in item:
                    if key in tytles:
                        if key == 'Country':
                            print("{0:<30}".format(item[key]), end='')
                        else:
                            print("{0:<17}".format(item[key]), end='')
                else:
                    print('')
        if a == 3:
            name = input('Введіть назву країни')
            tytles = ([item for item in list(covid19[0].keys()) if item not in [
                      'ID', 'CountryCode', 'Slug', 'Date', 'Premium']])
            for item in tytles:
                if item == 'Country':
                    print("{0:_^30s}".format(item), end=' ')
                else:
                    print("{0:_^15s}".format(item), end=' ')
            else:
                print(' ')
            for item in covid19:
                if name in item.values():
                    for key in item:
                        if key in tytles:
                            if key == 'Country':
                                print("{0:<30}".format(item[key]), end='')
                            else:
                                print("{0:<17}".format(item[key]), end='')
                    else:
                        print('')
            continue

        if a == 4:
            pop_date = covid19_global.pop('Date')
            tytles = ([item for item in list(
                covid19_global.keys()) if item not in ['Date']])
            for item in tytles:
                print("{0:15s}".format(item), end=' ')
            else:
                print(' ')
            for item in covid19_global.values():
                print("{0:<17}".format(item), end='')
        if a == 5:
            break

        else:
            print('Not correct')
except ValueError:
    print('uncorrect Value')
