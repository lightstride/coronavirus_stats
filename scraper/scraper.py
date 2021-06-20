from bs4 import BeautifulSoup
import requests

def validate_country(ctry):
    ctry = ctry.lower()
    if ctry == 'usa':
        ctry = 'us'
 
    country_list = ctry.split(' ')
    
    if len(country_list)  == 2 :
        ctry = country_list[0] + '-' + country_list[1]
        
    return ctry   


def get_world_stats():
    try:
        source = requests.get('https://www.worldometers.info/coronavirus/').text
        soup = BeautifulSoup(source, 'lxml')

        stats_list = []

        data = soup.find_all('div', id='maincounter-wrap')
        for ele in data:
            stats_list.append(ele.div.span.text)
        stats = {'cases' : stats_list[0], 'deaths' : stats_list[1], 'recovered' : stats_list[2]}
    except:
        return {'error' : 'An error occured'}
    return stats

def get_country_stats(country):
 try:
   
    country = validate_country(country)
    
    source = requests.get(f'https://www.worldometers.info/coronavirus/country/{country}/').text
    soup = BeautifulSoup(source, 'lxml')
    stats_list = []
    data = soup.find_all("div", class_ = "maincounter-number")

    for ele in data:
        stats_list.append(ele.text.strip())
    stats = {'cases' : stats_list[0], 'deaths' : stats_list[1], 'recovered' : stats_list[2]}
    return stats
    
 except:
    return {'error': 'An error occured'}
