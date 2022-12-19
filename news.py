from newsapi.newsapi_client import NewsApiClient

# local file
import keys
from countries import get_countries_dict, find_countries_alpha, is_alpha

DEFAULT_LANGUAGE = 'en'
# page_size (int or None) – Use this to page through the results if the total results found is greater than the page size.
DEFAULT_PAGE_SIZE = 10
# page (int or None) – The number of results to return per page (request). 20 is the default, 100 is the maximum.
DEFAULT_PAGE = 10
# ref.: https://newsapi-python.readthedocs.io/en/latest/api.html#newsapi.NewsApiClient.get_top_headlines

categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
countries_dict = get_countries_dict()

api = NewsApiClient(api_key='c9cfcfc10c3645c5b8dc2226cecc080d')
# args = text.split(" ")

def string_handle(input):
   return input.lstrip(" ").rstrip(" ").lower()

def simple_search(input):
   input = string_handle(input)
   if input in countries_dict: # if input in dictionar
      return api.get_top_headlines(country=find_countries_alpha(input), page_size=DEFAULT_PAGE_SIZE)
   elif is_alpha(input): # if input is an country alpha
      return api.get_top_headlines(country=input, page_size=DEFAULT_PAGE_SIZE)
   elif input in categories:
      return api.get_top_headlines(category=input)
   else:
      headline_res = api.get_top_headlines(q=input)
      if headline_res:
         return api.get_top_headlines(q=input)
      else:
         
# TO-DO
def get_everthing(input):
   return api.get_everything(input, sort_by="relevency")


