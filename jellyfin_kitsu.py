import re
from pathlib import Path

import dateutil.parser

from data_classes import BaseItemDto, ReportIncludeItemTypes, SortOrder, MetadataField
from jellyfin import jellyfin, TAG, get_media_folder, get_user, get_all_items, set_tag
from kitsu.kitsu_helper import inquire_kitsu_data, inquire_kitsu_data_by_id
from util.path_functions import remove_illegal_char


def list_missing_episodes(user, parent, special=False):
    all_items = jellyfin.users.get_items_by_user_id(
        sort_by=["SeriesSortName", "SortName"],
        sort_order=SortOrder.ASCENDING,
        include_item_types=[ReportIncludeItemTypes.EPISODE],
        recursive=True,
        is_missing=True,
        is_unaired=False,
        user_id=user.id,
        parent_id=parent.id,
    )
    for item in all_items.items:
        if not special and "special" in item.season_name.lower():
            continue
        print(f"{item.series_name} {item.season_name} Episode {item.index_number} - {item.name}")


def set_kitsu_season_data(user, parent, inquire=True, force=False):
    shows = get_all_items(user, parent)
    for show in shows:
        # force = True
        # if show.name != "Tonari no Seki-kun: The Master of Killing Time":
        #     continue
        seasons = get_all_items(user, show)
        for season in seasons:
            if TAG in season.tags and "Kitsu" in season.provider_ids and not force:
                continue

            if inquire is True:
                if season.location_type == 'FileSystem':
                    kitsu_data = inquire_kitsu_data(Path(season.path).name.replace("(Dub)", "").strip())
                else:
                    kitsu_data = inquire_kitsu_data(Path(show.path).name.replace("(Dub)", "").strip(), "TV")
            else:
                continue

            if kitsu_data.anime is None:
                continue
            new_season_info = BaseItemDto.from_dict(season.to_dict())
            new_season_info.name = kitsu_data.anime.title
            new_season_info.overview = kitsu_data.anime.synopsis
            new_season_info.index_number = None
            new_season_info.provider_ids["Kitsu"] = kitsu_data.anime.id
            if kitsu_data.anime.status == "finished":
                new_season_info.status = "Ended"
            if kitsu_data.anime.status == "current":
                new_season_info.status = 'Continuing'
            new_season_info.official_rating = kitsu_data.anime.age_rating
            new_season_info.community_rating = float(kitsu_data.anime.average_rating) / 10
            new_season_info.tags = set_tag(new_season_info.tags)
            new_season_info.locked_fields = [
                MetadataField.NAME,
                MetadataField.OVERVIEW,
                MetadataField.OFFICIAL_RATING,
                MetadataField.TAGS
            ]
            new_season_info.production_year = int(kitsu_data.anime.started_at.split("-")[0])
            new_season_info.start_date = dateutil.parser.parse(kitsu_data.anime.started_at)
            if kitsu_data.anime.ended_at is not None:
                new_season_info.end_date = dateutil.parser.parse(kitsu_data.anime.ended_at)

            # new_season_info.lock_data = True
            jellyfin.items.update_item(season.id, new_season_info)
            print(f"updated: {show.name} - {new_season_info.name}")


def list_kitsu_season_data(user, parent):
    shows = get_all_items(user, parent)
    for show in shows:
        seasons = get_all_items(user, show)
        for season in seasons:
            season_name = Path(season.path).name.replace("(Dub)", "").strip()
            if TAG not in season.tags or "Kitsu" not in season.provider_ids:
                print(f"{season_name.rjust(70)}")
                continue

            kitsu_data = inquire_kitsu_data_by_id(season.provider_ids["Kitsu"])
            if remove_illegal_char(season_name) == remove_illegal_char(kitsu_data.anime.title):
                continue
            print(f"{season_name.rjust(70)} -- {kitsu_data.anime.title} -- {kitsu_data.anime.url}")


def set_kitsu_season_index(user, parent):
    shows = get_all_items(user, parent)
    for show in shows:
        seasons = get_all_items(user, show)
        for season in seasons:
            if season.production_year is None:
                season.production_year = 9999999

        sorted_seasons = sorted(seasons, key=lambda k: k.production_year)

        for index, season in enumerate(sorted_seasons):
            if season.production_year == 9999999:
                continue
            new_season_info = BaseItemDto.from_dict(season.to_dict())
            new_season_info.index_number = index + 1
            print(f"{season.name} -- {new_season_info.index_number}")
            jellyfin.items.update_item(season.id, new_season_info)


def set_kitsu_episode_data(user, parent, force=False):
    shows = get_all_items(user, parent)
    for show in shows:
        seasons = get_all_items(user, show)
        for season in seasons:
            if TAG not in season.tags or "Kitsu" not in season.provider_ids:
                continue
            kitsu_data = inquire_kitsu_data_by_id(season.provider_ids["Kitsu"])
            episodes = get_all_items(user, season)
            for episode in episodes:
                if TAG in episode.tags and "Kitsu" in episode.provider_ids and not force:
                    continue

                episode_name = ".".join(Path(episode.path).name.split(".")[:-2])
                # if episode.name == episode_name or episode.name.startswith(episode_name + " -"):
                #     continue

                try:
                    episode_number = int(re.findall("[0-9]+", episode_name)[-1])
                except:
                    continue

                if episode_number > len(kitsu_data.episodes):
                    print(f"Episode not found: {episode_name}")
                    new_episode_info = BaseItemDto.from_dict(episode.to_dict())
                    new_episode_info.name = episode_name
                    new_episode_info.index_number = episode_number
                    jellyfin.items.update_item(episode.id, new_episode_info)
                    continue

                # kitsu_episode = None
                # if kitsu_data.episodes[episode_number - 1].number == episode_number:
                kitsu_episode = kitsu_data.episodes[episode_number - 1]
                # else:
                #     for ke in kitsu_data.episodes:
                #         if ke.number == episode_number:
                #             kitsu_episode = ke
                #             break
                # if kitsu_episode is None:
                #     raise Exception(f"Episode not found: {name}")

                new_episode_info = BaseItemDto.from_dict(episode.to_dict())
                new_episode_info.name = episode_name + (
                    f" - {kitsu_episode.canonical_title}" if kitsu_episode.canonical_title is not None else "")
                new_episode_info.overview = kitsu_episode.synopsis if kitsu_episode.synopsis != "" else None
                new_episode_info.parent_index_number = season.index_number
                new_episode_info.index_number = episode_number
                new_episode_info.provider_ids = {"Kitsu": kitsu_episode.id}
                if TAG not in new_episode_info.tags:
                    new_episode_info.tags.append(TAG)
                new_episode_info.tags = set_tag(new_episode_info.tags)
                new_episode_info.locked_fields = [
                    MetadataField.NAME,
                    MetadataField.OVERVIEW,
                    MetadataField.TAGS
                ]
                if kitsu_episode.airdate is not None:
                    new_episode_info.production_year = int(kitsu_episode.airdate.split("-")[0])
                    new_episode_info.premiere_date = dateutil.parser.parse(kitsu_episode.airdate)

                # new_season_info.lock_data = True
                print(f"{show.name} -- {season.name} -- {episode_number} :: {new_episode_info.name}")
                jellyfin.items.update_item(episode.id, new_episode_info)


def list_kitsu_episode_data(user, parent):
    shows = get_all_items(user, parent)
    for show in shows:
        # force = True
        # if show.name != "Tonari no Seki-kun: The Master of Killing Time":
        #     continue
        seasons = get_all_items(user, show)
        for season in seasons:
            if season.location_type != 'FileSystem':
                print("Error" + season.name)
                continue

            season_name = Path(season.path).name
            episodes = get_all_items(user, season)
            for episode in episodes:
                episode_name = ".".join(Path(episode.path).name.split(".")[:-2])
                try:
                    int(episode_name[len(season_name):].strip())
                except:
                    print(f"{season_name.rjust(60)} :: {episode_name}")


if __name__ == '__main__':
    jellyfin_user = get_user("jellyfin")
    # list_missing_episodes(jellyfin_user, get_media_folder("TV Shows"))
    # set_kitsu_season_data(jellyfin_user, get_media_folder("Anime"), inquire=True)
    # set_kitsu_season_data(jellyfin_user, get_media_folder("Anime (Dub)"), inquire=True)
    # list_kitsu_season_data(jellyfin_user, get_media_folder("Anime"))
    # list_kitsu_season_data(jellyfin_user, get_media_folder("Anime (Dub)"))
    # set_kitsu_season_index(jellyfin_user, get_media_folder("Anime"))
    # set_kitsu_season_index(jellyfin_user, get_media_folder("Anime (Dub)"))
    set_kitsu_episode_data(jellyfin_user, get_media_folder("Anime"))
    set_kitsu_episode_data(jellyfin_user, get_media_folder("Anime (Dub)"))
    # list_kitsu_episode_data(jellyfin_user, get_media_folder("Anime"))
    # list_kitsu_episode_data(jellyfin_user, get_media_folder("Anime (Dub)"))
