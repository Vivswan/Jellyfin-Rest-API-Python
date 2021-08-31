from typing import List

from _config import SERVER_ADDRESS, API_KEY
from data_classes import BaseItemDto, UserDto
from query_classes import Jellyfin

jellyfin = Jellyfin(SERVER_ADDRESS, API_KEY)
TAG = "vsapi-20210829"


def get_media_folder(name) -> BaseItemDto:
    for media_folder in jellyfin.library.get_media_folders().items:
        if media_folder.name == name:
            return media_folder

    raise Exception(f'Media Folder Not Found: "{name}"')


def get_user(username) -> UserDto:
    global jellyfin
    for user in jellyfin.users.get_users(is_disabled=False):
        if user.name == username:
            return user
    raise Exception(f'User Not Found: "{username}"')


def get_all_items(user, parent):
    result: List[BaseItemDto] = []
    items = jellyfin.users.get_items_by_user_id(
        user_id=user.id,
        parent_id=parent.id,
        sort_by=["SortName"],
        enable_images=False,
        enable_user_data=False,
        enable_image_types=False,
        enable_total_record_count=False
    ).items
    for i in items:
        try:
            result.append(jellyfin.users.get_item(user_id=user.id, item_id=i.id))
        except:
            pass

    return result


def set_tag(tags):
    temp_tags = []
    for tag in list(set(tags)):
        if not tag.startswith(TAG.split("-")[0]):
            temp_tags.append(tag)
    temp_tags.append(TAG)
    return list(set(temp_tags))
