import pycountry

def init():
   countries = {}
   for country in pycountry.countries:
      countries[country.name.lower()] = country.alpha_2.lower()

   api_list = ['ae', 'ar', 'at', 'au', 'be', 'bg', 'br', 'ca', 'ch', 'cn', 'co', 'cu', 'cz', 
   'de', 'eg', 'es', 'fr', 'gb', 'gr', 'hk', 'hu', 'id', 'ie', 'il', 'in', 'is', 'it', 'jp',
   'kr', 'lt', 'lv', 'ma', 'mx', 'my', 'ng', 'nl', 'no', 'nz', 'ph', 'pk', 'pl', 'pt', 'ro',
   'rs', 'ru', 'sa', 'se', 'sg', 'si', 'sk', 'th', 'tr', 'tw', 'ua', 'us', 've', 'za', 'zh']

   tmp = [countries[x] for x in countries.keys()]
   alpha_2 = list(set(tmp) & set(api_list))
   tmp_2 = {v:k for k, v in countries.items()}
   return {tmp_2[x]:x for x in alpha_2}

countries = init()

alphas = [v for k, v in countries.items()]

def get_countries_dict():
   return countries 

def is_alpha(country_alpha):
   return country_alpha in alphas

def find_countries_alpha(country_name):
   return countries[country_name.lower()]
