from __future__ import unicode_literals

import re
from datetime import datetime

import requests
import requests.compat

from tvmaze import endpoints
from tvmaze.endpoints import endpoint_standard_get
from tvmaze.exceptions import *


class Show(object):
    def __init__(self, data):
        self.status = data.get('status')
        self.rating = data.get('rating')
        self.genres = data.get('genres')
        self.weight = data.get('weight')
        self.updated = data.get('updated')
        self.name = data.get('name')
        self.language = data.get('language')
        self.schedule = data.get('schedule')
        self.url = data.get('url')
        self.image = data.get('image')
        self.externals = data.get('externals')
        self.premiered = data.get('premiered')
        self.summary = remove_html_tags(data.get('summary', ''))
        self.links = data.get('_links')
        if data.get('webChannel'):
            self.web_channel = WebChannel(data.get('webChannel'))
        else:
            self.web_channel = None
        self.runtime = data.get('runtime')
        self.type = data.get('type')
        self.id = data.get('id')
        self.maze_id = self.id
        if data.get('network'):
            self.network = Network(data.get('network'))
        else:
            self.network = None
        self.__episodes = list()
        self.__seasons = dict()
        self.__cast = None
        self.__crew = None
        self.__aka = None
        self.__images = None

    def __repr__(self):
        if self.premiered:
            year = str(self.premiered[:4])
        else:
            year = None
        if self.web_channel:
            platform = ',show_web_channel='
            network = self.web_channel.name
        elif self.network:
            platform = ',network='
            network = self.network.name
        else:
            platform = ''
            network = ''

        return _valid_encoding('<Show(maze_id={id},name={name},year={year}{platform}{network})>'.format(
            id=self.maze_id,
            name=self.name,
            year=year,
            platform=platform,
            network=network)
        )

    def __str__(self):
        return _valid_encoding(self.name)

    def __unicode__(self):
        return self.name

    def __iter__(self):
        return iter(self.seasons.values())

    # Python 3 bool evaluation
    def __bool__(self):
        return bool(self.id)

    # Python 2 bool evaluation
    def __nonzero__(self):
        return bool(self.id)

    def __len__(self):
        return len(self.seasons)

    def __getitem__(self, item):
        try:
            return self.seasons[item]
        except KeyError:
            raise SeasonNotFound('Season {0} does not exist for show {1}.'.format(item, self.name))

    @property
    def episodes(self):
        if not self.__episodes:
            self.__episodes = get_episode_of_show(self.maze_id, specials=True)
        return self.__episodes

    @property
    def seasons(self):
        if not self.__seasons:
            self.__seasons = get_seasons_of_show(self.maze_id)
        return self.__seasons

    @property
    def cast(self):
        if not self.__cast:
            self.__cast = get_show_cast(self.maze_id)
        return self.__cast

    @property
    def crew(self):
        if not self.__crew:
            self.__crew = get_show_crew(self.maze_id)
        return self.__crew

    @property
    def aka(self):
        if not self.__aka:
            self.__aka = get_show_aka(self.maze_id)
        return self.__aka

    @property
    def images(self):
        if not self.__images:
            self.__images = get_show_images(self.maze_id)
        return self.__images


class Season(object):
    def __init__(self, data):
        self.show = None
        self.__episodes = list()
        self.id = data.get('id')
        self.url = data.get('url')
        self.season_number = data.get('number')
        self.name = data.get('name')
        self.episode_order = data.get('episodeOrder')
        self.premier_date = data.get('premierDate')
        self.end_date = data.get('endDate')
        if data.get('network'):
            self.network = Network(data.get('network'))
        else:
            self.network = None
        if data.get('webChannel'):
            self.web_channel = WebChannel(data.get('webChannel'))
        else:
            self.web_channel = None
        self.image = data.get('image')
        self.summary = data.get('summary')
        self.links = data.get('_links')

    def __repr__(self):
        return _valid_encoding('<Season(id={id},season_number={number})>'.format(
            id=self.id,
            number=str(self.season_number).zfill(2)
        ))

    def __iter__(self):
        return iter(self.episodes)

    def __len__(self):
        return len(self.episodes)

    def __getitem__(self, item):
        try:
            return self.episodes[item]
        except KeyError:
            raise EpisodeNotFound(
                'Episode {0} does not exist for season {1} of show {2}.'.format(item, self.season_number,
                                                                                self.show))

    # Python 3 bool evaluation
    def __bool__(self):
        return bool(self.id)

    # Python 2 bool evaluation
    def __nonzero__(self):
        return bool(self.id)

    @property
    def episodes(self):
        if not self.__episodes:
            self.__episodes = get_episode_list_of_season(self.id)
        return self.__episodes


class Episode(object):
    def __init__(self, data):
        self.title = data.get('name')
        self.airdate = data.get('airdate')
        self.url = data.get('url')
        self.season_number = data.get('season')
        self.episode_number = data.get('number')
        self.image = data.get('image')
        self.airstamp = data.get('airstamp')
        self.airtime = data.get('airtime')
        self.runtime = data.get('runtime')
        self.summary = remove_html_tags(data.get('summary'))
        self.maze_id = data.get('id')
        self.special = self.is_special()
        # Reference to show for when using get_schedule()
        if data.get('show'):
            self.show = Show(data.get('show'))
        # Reference to show for when using get_full_schedule()
        if data.get('_embedded'):
            if data['_embedded'].get('show'):
                self.show = Show(data['_embedded']['show'])

    def __repr__(self):
        if self.special:
            epnum = 'Special'
        else:
            epnum = self.episode_number
        return '<Episode(season={season},episode_number={number})>'.format(
            season=str(self.season_number).zfill(2),
            number=str(epnum).zfill(2)
        )

    def __str__(self):
        season = 'S' + str(self.season_number).zfill(2)
        if self.special:
            episode = ' Special'
        else:
            episode = 'E' + str(self.episode_number).zfill(2)
        return _valid_encoding(season + episode + ' ' + self.title)

    def is_special(self):
        if self.episode_number:
            return False
        return True


class Person(object):
    def __init__(self, data):
        if data.get('person'):
            data = data['person']
        self.links = data.get('_links')
        self.id = data.get('id')
        self.image = data.get('image')
        self.name = data.get('name')
        self.score = data.get('score')
        self.url = data.get('url')
        self.character = None
        self.castcredits = None
        self.crewcredits = None
        self.populate(data)

    def populate(self, data):
        if data.get('_embedded'):
            if data['_embedded'].get('castcredits'):
                self.castcredits = [CastCredit(credit)
                                    for credit in data['_embedded']['castcredits']]
            elif data['_embedded'].get('crewcredits'):
                self.crewcredits = [CrewCredit(credit)
                                    for credit in data['_embedded']['crewcredits']]

    def __repr__(self):
        return _valid_encoding('<Person(name={name},maze_id={id})>'.format(
            name=self.name,
            id=self.id
        ))

    def __str__(self):
        return _valid_encoding(self.name)


class Character(object):
    def __init__(self, data):
        self.id = data.get('id')
        self.url = data.get('url')
        self.name = data.get('name')
        self.image = data.get('image')
        self.links = data.get('_links')
        self.person = None

    def __repr__(self):
        return _valid_encoding('<Character(name={name},maze_id={id})>'.format(
            name=self.name,
            id=self.id
        ))

    def __str__(self):
        return _valid_encoding(self.name)

    def __unicode__(self):
        return self.name


class Cast(object):
    def __init__(self, data):
        self.people = []
        self.characters = []
        self.populate(data)

    def populate(self, data):
        for cast_member in data:
            self.people.append(Person(cast_member['person']))
            self.characters.append(Character(cast_member['character']))
            self.people[-1].character = self.characters[-1]  # add reference to character
            self.characters[-1].person = self.people[-1]  # add reference to cast member


class CastCredit(object):
    def __init__(self, data):
        self.links = data.get('_links')
        self.character = None
        self.show = None
        self.populate(data)

    def populate(self, data):
        if data.get('_embedded'):
            if data['_embedded'].get('character'):
                self.character = Character(data['_embedded']['character'])
            elif data['_embedded'].get('show'):
                self.show = Show(data['_embedded']['show'])


class CrewCredit(object):
    def __init__(self, data):
        self.links = data.get('_links')
        self.type = data.get('type')
        self.show = None
        self.populate(data)

    def populate(self, data):
        if data.get('_embedded'):
            if data['_embedded'].get('show'):
                self.show = Show(data['_embedded']['show'])


class Crew(object):
    def __init__(self, data):
        self.person = Person(data.get('person'))
        self.type = data.get('type')

    def __repr__(self):
        return _valid_encoding('<Crew(name={name},maze_id={id},type={type})>'.format(
            name=self.person.name,
            id=self.person.id,
            type=self.type
        ))


class AKA(object):
    def __init__(self, data):
        self.name = data.get('name')
        self.country = data.get('country')

    def __repr__(self):
        return '<AKA(name={name},country={country})>'.format(name=self.name, country=self.country)


class Network(object):
    def __init__(self, data):
        self.name = data.get('name')
        self.maze_id = data.get('id')
        if data.get('country'):
            self.country = data['country'].get('name')
            self.timezone = data['country'].get('timezone')
            self.code = data['country'].get('code')

    def __repr__(self):
        return '<Network(name={name},country={country})>'.format(name=self.name, country=self.country)


class WebChannel(object):
    def __init__(self, data):
        self.name = data.get('name')
        self.maze_id = data.get('id')
        if data.get('country'):
            self.country = data['country'].get('name')
            self.timezone = data['country'].get('timezone')
            self.code = data['country'].get('code')

    def __repr__(self):
        return '<WebChannel(name={name},country={country})>'.format(name=self.name, country=self.country)


class Image(object):
    def __init__(self, data):
        self.id = data.get('id')
        self.type = data.get('type')
        self.main = data.get('main')
        original = data.get('resolutions').get('original')
        self.url = original.get('url')
        self.width = original.get('width')
        self.height = original.get('height')

    def __repr__(self):
        return f'<Image(type={self.type})>'


def _valid_encoding(text):
    if not text:
        return
    if sys.version_info > (3,):
        return text
    else:
        return unicode(text).encode('utf-8')


def _url_quote(show):
    return requests.compat.quote(show.encode('UTF-8'))


def remove_html_tags(text):
    if not text:
        return None
    return re.sub(r'<.*?>', '', text)


def get_show_with_qualifiers(show_name, qualifiers):
    shows = get_show_list(show_name)
    best_match = -1  # Initialize match value score
    show_match = None

    for show in shows:
        if show.premiered:
            premiered = show.premiered[:-6].lower()
        else:
            premiered = None
        if show.network and show.network.name:
            network = show.network.name.lower()
        else:
            network = None
        if show.web_channel and show.web_channel.name:
            web_channel = show.web_channel.name.lower()
        else:
            web_channel = None
        if show.network and show.network.code:
            country = show.network.code.lower()
        else:
            if show.web_channel and show.web_channel.code:
                country = show.web_channel.code.lower()
            else:
                country = None
        if show.language:
            language = show.language.lower()
        else:
            language = None

        attributes = [premiered, country, network, language, web_channel]
        show_score = len(set(qualifiers) & set(attributes))
        if show_score > best_match:
            best_match = show_score
            show_match = show
    return show_match


def get_show_by_search(show_name, show_year, show_network, show_language, show_country, show_web_channel, embed):
    if show_year:
        show_year = str(show_year)
    qualifiers = list(filter(None, [show_year, show_network, show_language, show_country, show_web_channel]))
    if qualifiers:
        qualifiers = [q.lower() for q in qualifiers if q]
        show = get_show_with_qualifiers(show_name, qualifiers)
    else:
        return show_single_search(show=show_name, embed=embed)
    if embed:
        return show_main_info(maze_id=show.id, embed=embed)
    else:
        return show


def get_show_by_id(maze_id=None, tvdb_id=None, tvrage_id=None, imdb_id=None, show_name=None,
                   show_year=None, show_network=None, show_language=None, show_country=None,
                   show_web_channel=None, embed=None):
    """
    Get Show object directly via id or indirectly via name + optional qualifiers

    If only a show_name is given, the show with the highest score using the
    tvmaze algorithm will be returned.
    If you provide extra qualifiers such as network or language they will be
    used for a more specific match, if one exists.
    Args:
        maze_id: Show maze_id
        tvdb_id: Show tvdb_id
        tvrage_id: Show tvrage_id
        imdb_id: Show imdb_id
        show_name: Show name to be searched
        show_year: Show premiere year
        show_network: Show TV Network (like ABC, NBC, etc.)
        show_web_channel: Show Web Channel (like Netflix, Amazon, etc.)
        show_language: Show language
        show_country: Show country
        embed: embed parameter to include additional data. Currently 'episodes' and 'cast' are supported
    """
    errors = []
    if not (maze_id or tvdb_id or tvrage_id or imdb_id or show_name):
        raise MissingParameters(
            'Either maze_id, tvdb_id, tvrage_id, imdb_id or show_name are required to get show, none provided,')
    if maze_id:
        try:
            return show_main_info(maze_id, embed=embed)
        except IDNotFound as e:
            errors.append(e.value)
    if tvdb_id:
        try:
            return show_main_info(lookup_tvdb(tvdb_id).id, embed=embed)
        except IDNotFound as e:
            errors.append(e.value)
    if tvrage_id:
        try:
            return show_main_info(lookup_tvrage(tvrage_id).id, embed=embed)
        except IDNotFound as e:
            errors.append(e.value)
    if imdb_id:
        try:
            return show_main_info(lookup_imdb(imdb_id).id, embed=embed)
        except IDNotFound as e:
            errors.append(e.value)
    if show_name:
        try:
            show = get_show_by_search(show_name, show_year, show_network, show_language,
                                      show_country, show_web_channel, embed=embed)
            return show
        except ShowNotFound as e:
            errors.append(e.value)
    raise ShowNotFound(' ,'.join(errors))


# Return list of Show objects
def get_show_list(show_name):
    """
    Return list of Show objects from the TVMaze "Show Search" endpoint

    List will be ordered by tvmaze score and should mimic the results you see
    by doing a show search on the website.
    :param show_name: Name of show
    :return: List of Show(s)
    """
    shows = search(show_name)
    return shows


def search(show):
    _show = _url_quote(show)
    url = endpoints.show_search.format(_show)
    q = endpoint_standard_get(url)
    if q:
        shows = []
        for result in q:
            show = Show(result['show'])
            show.score = result['score']
            shows.append(show)
        return shows
    else:
        raise ShowNotFound('Show {0} not found'.format(show))


def show_single_search(show, embed=None):
    if not (embed in [None, 'episodes', 'cast', 'previousepisode', 'nextepisode']):
        raise InvalidEmbedValue('Value for embed must be "episodes", "cast", "previousepisode", "nextepisode", or None')
    _show = _url_quote(show)
    if embed:
        url = endpoints.show_single_search.format(_show) + '&embed=' + embed
    else:
        url = endpoints.show_single_search.format(_show)
    q = endpoint_standard_get(url)
    if q:
        return Show(q)
    else:
        raise ShowNotFound('show name "{0}" not found'.format(show))


def lookup_tvrage(tvrage_id):
    url = endpoints.lookup_tvrage.format(tvrage_id)
    q = endpoint_standard_get(url)
    if q:
        return Show(q)
    else:
        raise IDNotFound('TVRage id {0} not found'.format(tvrage_id))


def lookup_tvdb(tvdb_id):
    url = endpoints.lookup_tvdb.format(tvdb_id)
    q = endpoint_standard_get(url)
    if q:
        return Show(q)
    else:
        raise IDNotFound('TVDB ID {0} not found'.format(tvdb_id))


def lookup_imdb(imdb_id):
    url = endpoints.lookup_imdb.format(imdb_id)
    q = endpoint_standard_get(url)
    if q:
        return Show(q)
    else:
        raise IDNotFound('IMDB ID {0} not found'.format(imdb_id))


def get_schedule(country='US', date=str(datetime.today().date())):
    url = endpoints.get_schedule.format(country, date)
    q = endpoint_standard_get(url)
    if q:
        return [Episode(episode) for episode in q]
    else:
        raise ScheduleNotFound('Schedule for country {0} at date {1} not found'.format(country, date))


# ALL known future episodes, several MB large, cached for 24 hours
def get_full_schedule():
    url = endpoints.get_full_schedule
    q = endpoint_standard_get(url)
    if q:
        return [Episode(episode) for episode in q]
    else:
        raise GeneralError('Something went wrong, www.tvmaze.com may be down')


def show_main_info(maze_id, embed=None):
    if not (embed in [None, 'episodes', 'cast', 'previousepisode', 'nextepisode']):
        raise InvalidEmbedValue('Value for embed must be "episodes", "cast", "previousepisode", "nextepisode", or None')
    if embed:
        url = endpoints.show_main_info.format(maze_id) + '?embed=' + embed
    else:
        url = endpoints.show_main_info.format(maze_id)
    q = endpoint_standard_get(url)
    if q:
        return Show(q)
    else:
        raise IDNotFound('Maze id {0} not found'.format(maze_id))


def get_episode_of_show(maze_id, specials=None):
    if specials:
        url = endpoints.episode_list.format(maze_id) + '&specials=1'
    else:
        url = endpoints.episode_list.format(maze_id)
    q = endpoint_standard_get(url)
    if type(q) == list:
        return [Episode(episode) for episode in q]
    else:
        raise IDNotFound('Maze id {0} not found'.format(maze_id))


def get_episode_list_of_season(season_id):
    url = endpoints.episodes_by_season.format(season_id)
    q = endpoint_standard_get(url)
    if type(q) == list:
        return [Episode(episode) for episode in q]
    else:
        raise IDNotFound('Maze id {0} not found'.format(season_id))


def get_episode_by_number(maze_id, season_number, episode_number):
    url = endpoints.episode_by_number.format(maze_id,
                                             season_number,
                                             episode_number)
    q = endpoint_standard_get(url)
    if q:
        return Episode(q)
    else:
        raise EpisodeNotFound(
            'Couldn\'t find season {0} episode {1} for TVMaze ID {2}'.format(season_number,
                                                                             episode_number,
                                                                             maze_id))


def get_episodes_by_date(maze_id, airdate):
    try:
        datetime.strptime(airdate, '%Y-%m-%d')
    except ValueError:
        raise IllegalAirDate('Airdate must be string formatted as \"YYYY-MM-DD\"')
    url = endpoints.episodes_by_date.format(maze_id, airdate)
    q = endpoint_standard_get(url)
    if q:
        return [Episode(episode) for episode in q]
    else:
        raise NoEpisodesForAirdate(
            'Couldn\'t find an episode airing {0} for TVMaze ID {1}'.format(airdate, maze_id))


def get_episode_by_id(episode_id):
    url = endpoints.episode_by_id.format(episode_id)
    q = endpoint_standard_get(url)
    if q:
        return Episode(q)
    else:
        raise EpisodeNotFound('Couldn\'t find Episode with ID {0}'.format(episode_id))


def get_seasons_of_show(maze_id):
    url = endpoints.show_seasons.format(maze_id)
    q = endpoint_standard_get(url)
    if q:
        season_dict = dict()
        for season in q:
            season_dict[season['number']] = Season(season)
        return season_dict
    else:
        raise SeasonNotFound('Couldn\'t find Season\'s for TVMaze ID {0}'.format(maze_id))


def get_season_by_id(season_id):
    url = endpoints.season_by_id.format(season_id)
    q = endpoint_standard_get(url)
    if q:
        return Season(q)
    else:
        raise SeasonNotFound('Couldn\'t find Season with ID {0}'.format(season_id))


def get_show_cast(maze_id):
    url = endpoints.show_cast.format(maze_id)
    q = endpoint_standard_get(url)
    if q:
        return Cast(q)
    else:
        raise CastNotFound('Couldn\'nt find show cast for TVMaze ID {0}'.format(maze_id))


def get_show_crew(maze_id):
    url = endpoints.show_crew.format(maze_id)
    q = endpoint_standard_get(url)
    if isinstance(q, list):
        return [Crew(crew) for crew in q]
    else:
        raise CrewNotFound('Couldn\'t find crew for TVMaze ID {}'.format(maze_id))


def get_show_aka(maze_id):
    url = endpoints.show_akas.format(maze_id)
    q = endpoint_standard_get(url)
    if q:
        return [AKA(aka) for aka in q]
    else:
        raise AKASNotFound('Couldn\'t find AKA\'s for TVMaze ID {0}'.format(maze_id))


def get_show_images(maze_id):
    url = endpoints.show_images.format(maze_id)
    q = endpoint_standard_get(url)
    if q:
        return [Image(aka) for aka in q]
    else:
        raise AKASNotFound('Couldn\'t find AKA\'s for TVMaze ID {0}'.format(maze_id))
