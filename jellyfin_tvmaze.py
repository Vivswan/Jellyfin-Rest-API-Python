from jellyfin import get_all_items, get_user, get_media_folder


def set_tvmaze_show_data(user, parent, inquire=True, force=False):
    shows = get_all_items(user, parent)
    for show in shows:
        if 'TVmaze' not in show.provider_ids.keys():
            print(show.name)
        # force = True
        # if show.name != "Tonari no Seki-kun: The Master of Killing Time":
        #     continue
        # seasons = get_all_items(user, show)
        # for season in seasons:
        #     if TAG in season.tags and "Kitsu" in season.provider_ids and not force:
        #         continue
        #
        #     if inquire is True:
        #         if season.location_type == 'FileSystem':
        #             kitsu_data = inquire_kitsu_data(Path(season.path).name.replace("(Dub)", "").strip())
        #         else:
        #             kitsu_data = inquire_kitsu_data(Path(show.path).name.replace("(Dub)", "").strip(), "TV")
        #     else:
        #         continue
        #
        #     if kitsu_data.anime is None:
        #         continue
        #     new_season_info = BaseItemDto.from_dict(season.to_dict())
        #     new_season_info.name = kitsu_data.anime.title
        #     new_season_info.overview = kitsu_data.anime.synopsis
        #     new_season_info.index_number = None
        #     new_season_info.provider_ids["Kitsu"] = kitsu_data.anime.id
        #     if kitsu_data.anime.status == "finished":
        #         new_season_info.status = "Ended"
        #     if kitsu_data.anime.status == "current":
        #         new_season_info.status = 'Continuing'
        #     new_season_info.official_rating = kitsu_data.anime.age_rating
        #     new_season_info.community_rating = float(kitsu_data.anime.average_rating) / 10
        #     new_season_info.tags = set_tag(new_season_info.tags)
        #     new_season_info.locked_fields = [
        #         MetadataField.NAME,
        #         MetadataField.OVERVIEW,
        #         MetadataField.OFFICIAL_RATING,
        #         MetadataField.TAGS
        #     ]
        #     new_season_info.production_year = int(kitsu_data.anime.started_at.split("-")[0])
        #     new_season_info.start_date = dateutil.parser.parse(kitsu_data.anime.started_at)
        #     if kitsu_data.anime.ended_at is not None:
        #         new_season_info.end_date = dateutil.parser.parse(kitsu_data.anime.ended_at)
        #
        #     # new_season_info.lock_data = True
        #     jellyfin.items.update_item(season.id, new_season_info)
        #     print(f"updated: {show.name} - {new_season_info.name}")


if __name__ == '__main__':
    jellyfin_user = get_user("jellyfin")
    # list_missing_episodes(jellyfin_user, get_media_folder("TV Shows"))
    set_tvmaze_show_data(jellyfin_user, get_media_folder("BL"), inquire=True)
    # list_kitsu_season_data(jellyfin_user, get_media_folder("Anime"))
    # set_kitsu_season_index(jellyfin_user, get_media_folder("Anime"))
    # set_kitsu_episode_data(jellyfin_user, get_media_folder("Anime"))
    # list_kitsu_episode_data(jellyfin_user, get_media_folder("Anime"))
