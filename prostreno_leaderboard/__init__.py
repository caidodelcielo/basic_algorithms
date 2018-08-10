import urllib.request as urllib2
import json
import ssl
import bs4
import datetime


def start_scraping():
    time_before = datetime.datetime.now()

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    seznam_soutezicich = []

    for x in range(0, 2120, 20):
        html_page = urllib2.urlopen("https://prima.iprima.cz/iprima-api/View_Prostreno/ThemedContent/More?ts=25530863&offset=" + str(x), context=ctx)
        print('.', end='', flush=True)
        json_data = json.load(html_page)
        tyden_soup = bs4.BeautifulSoup(json_data['related_content'], 'html.parser')
        uzivatele_soup = tyden_soup.find_all(class_='component--scope__contestant')

        for uzivatel in uzivatele_soup:
            jmeno_souteziciho = uzivatel.find(class_='component--scope__contestant--inner__details--text__name').get_text()
            pocet_komentaru = int(uzivatel.find(class_='component--scope__contestant--inner__other--comments').find('strong').get_text())
            odkaz = 'http:' + uzivatel.find('a').get('href')
            seznam_soutezicich.append((jmeno_souteziciho, pocet_komentaru, odkaz))

    print('')
    serazeni_soutezici = sorted(seznam_soutezicich, key=lambda k: k[1], reverse=True)
    for idx, sort_uzivatel in enumerate(serazeni_soutezici):
        print(str(idx + 1) + ',' + sort_uzivatel[0] + ',' + str(sort_uzivatel[1]) + ',' + sort_uzivatel[2])

    time_after = datetime.datetime.now()
    print()
    print('Start: ' + str(time_before.hour) + ':' + str(time_before.minute))
    print('End: ' + str(time_after.hour) + ':' + str(time_after.minute))
