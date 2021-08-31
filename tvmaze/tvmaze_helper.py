from tvmaze.tvmaze_class import search, get_show_by_id


def tvmaze_anime_inquire(query):
    json_list = search(query)
    if len(json_list) == 0:
        return None
    print()
    for i, v in enumerate(reversed(json_list)):
        print(f"{len(json_list) - i}. {v.name} ({v.id}) - {v.type} - {v.url}")

    print(f"Select for '{query}'")
    print()

    answer = input("Which Series? [1]: ") or "1"
    if answer.startswith("*"):
        answer = answer[1:]
        return get_show_by_id(maze_id=answer)
    answer = int(answer) - 1

    if answer < 0 or answer > len(json_list):
        print("skipping....")
        return None

    return json_list[answer]


if __name__ == '__main__':
    data = tvmaze_anime_inquire("2gether")
    print(data)
