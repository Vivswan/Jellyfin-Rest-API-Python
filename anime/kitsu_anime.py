def any_key_dict(data, *keys):
    for key in keys:
        if key in data:
            return data[key]

    assert False


class MediaEntry:
    __slots__ = ('id', 'type', 'title', 'synopsis', 'subtype', 'status', 'slug', 'average_rating', 'user_count',
                 'favorites_count', 'popularity_rank', 'rating_rank', 'age_rating', 'age_rating_guide',
                 'poster_image_url', 'cover_image_url', 'started_at', 'ended_at', 'next_release')

    def __init__(self, id_: str, type_: str, attributes: dict):
        self.id = id_
        self.type = type_
        self.title = any_key_dict(attributes, 'canonicalTitle', 'title')
        self.synopsis = any_key_dict(attributes, 'synopsis')
        self.subtype = any_key_dict(attributes, 'subtype')
        self.status = any_key_dict(attributes, 'status')
        self.slug = any_key_dict(attributes, 'slug')
        self.average_rating = any_key_dict(attributes, 'averageRating', 'average_rating')
        self.user_count = any_key_dict(attributes, 'userCount', 'user_count')
        self.favorites_count = any_key_dict(attributes, 'favoritesCount', 'favorites_count')
        self.popularity_rank = any_key_dict(attributes, 'popularityRank', 'popularity_rank')
        self.rating_rank = any_key_dict(attributes, 'ratingRank', 'rating_rank')
        self.age_rating = any_key_dict(attributes, 'ageRating', 'age_rating')
        self.age_rating_guide = any_key_dict(attributes, 'ageRatingGuide', 'age_rating_guide')
        if 'posterImage' in attributes and attributes['posterImage'] is not None:
            self.poster_image_url = attributes['posterImage']['original']
        elif 'poster_image_url' in attributes:
            self.poster_image_url = attributes['poster_image_url']
        else:
            self.poster_image_url = None
        if 'coverImage' in attributes and attributes['coverImage'] is not None:
            self.cover_image_url = attributes['coverImage']['original']
        elif 'cover_image_url' in attributes:
            self.cover_image_url = attributes['cover_image_url']
        else:
            self.cover_image_url = None
        self.started_at = any_key_dict(attributes, 'startDate', 'started_at')
        self.ended_at = any_key_dict(attributes, 'endDate', 'ended_at')
        self.next_release = any_key_dict(attributes, 'nextRelease', 'next_release')

    @property
    def url(self) -> str:
        return f'https://kitsu.io/{self.type}/{self.slug}'

    def __str__(self):
        return self.title

    def to_json(self):
        result = {}
        for name in self.__slots__:
            result[name] = getattr(self, name)
        return result


class Anime(MediaEntry):
    __slots__ = ('id', 'type', 'title', 'synopsis', 'subtype', 'status', 'slug', 'average_rating', 'user_count',
                 'favorites_count', 'popularity_rank', 'rating_rank', 'age_rating', 'age_rating_guide',
                 'poster_image_url', 'cover_image_url', 'started_at', 'ended_at', 'next_release',
                 'episode_count', 'episode_length', 'total_length', 'youtube_video_id', 'nsfw')

    def __init__(self, data: dict):
        if 'attributes' in data:
            attributes = data['attributes']
        else:
            attributes = data

        super().__init__(data['id'], "anime", attributes)

        self.episode_count = any_key_dict(attributes, 'episodeCount', 'episode_count')
        self.episode_length = any_key_dict(attributes, 'episodeLength', 'episode_length')
        self.total_length = any_key_dict(attributes, 'totalLength', 'total_length')
        self.youtube_video_id = any_key_dict(attributes, 'youtubeVideoId', 'youtube_video_id')
        self.nsfw = any_key_dict(attributes, 'nsfw')
