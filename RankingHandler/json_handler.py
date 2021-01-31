import json
import requests
from RankingHandler.api_params import Type, get_string, get_rank_under


def get_ranking_data(type: Type):
    type_str = get_string(type)
    type_lim = get_rank_under(type)
    data = {}

    try:
        url = "https://ranking-gigantic.seichi.click/api/ranking"
        params = {"type": type_str, "offset": 0, "lim": type_lim, "duration": "monthly"}
        res = requests.get(url, params=params)
        data = res.json()
    except requests.HTTPError as e:
        print("HTTP Error:", e)
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)

    return regen_json(data["ranks"])


def regen_json(arg):
    result = []

    for data in arg:
        data["playername"] = data["player"]["name"]
        data["playeruuid"] = data["player"]["uuid"]
        data["amount"] = data["data"]["raw_data"]

        del data["lastquit"], data["player"], data["data"]

        result.append(data)

    return result
