# TVMaze Free endpoints
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from tvmaze.exceptions import BadRequest

show_search = 'http://api.tvmaze.com/search/shows?q={0}'
show_single_search = 'http://api.tvmaze.com/singlesearch/shows?q={0}'
lookup_tvrage = 'http://api.tvmaze.com/lookup/shows?tvrage={0}'
lookup_tvdb = 'http://api.tvmaze.com/lookup/shows?thetvdb={0}'
lookup_imdb = 'http://api.tvmaze.com/lookup/shows?imdb={0}'
get_schedule = 'http://api.tvmaze.com/schedule?country={0}&date={1}'
get_full_schedule = 'http://api.tvmaze.com/schedule/full'
show_main_info = 'http://api.tvmaze.com/shows/{0}'
episode_list = 'http://api.tvmaze.com/shows/{0}/episodes?specials=1'
episode_by_number = 'http://api.tvmaze.com/shows/{0}/episodebynumber?season={1}&number={2}'
episodes_by_date = 'http://api.tvmaze.com/shows/{0}/episodesbydate?date={1}'
episodes_by_season = 'https://api.tvmaze.com/seasons/{0}/episodes'
show_cast = 'http://api.tvmaze.com/shows/{0}/cast'
show_index = 'http://api.tvmaze.com/shows?page={0}'
people_search = 'http://api.tvmaze.com/search/people?q={0}'
show_crew = 'http://api.tvmaze.com/shows/{0}/crew'
show_akas = 'http://api.tvmaze.com/shows/{0}/akas'
show_seasons = 'http://api.tvmaze.com/shows/{0}/seasons'
season_by_id = 'http://api.tvmaze.com/seasons/{0}'
episode_by_id = 'http://api.tvmaze.com/episodes/{0}'
show_images = 'https://api.tvmaze.com/shows/{0}/images'


def endpoint_standard_get(url):
    s = requests.Session()
    retries = Retry(total=5,
                    backoff_factor=0.1,
                    status_forcelist=[429])
    s.mount('http://', HTTPAdapter(max_retries=retries))
    try:
        r = s.get(url)
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(repr(e))

    s.close()

    if r.status_code in [404, 422]:
        return None

    if r.status_code == 400:
        raise BadRequest('Bad Request for url {}'.format(url))

    results = r.json()
    return results
