import json
import requests
from RankingHandler.api_params import Type, get_string, get_rank_under


# def get_data(type: Type):
#     type_str = get_string(type)
#     type_lim = get_rank_under(type)
#     data = {}
#
#     try:
#         url = "https://w4.minecraftserver.jp/api/ranking"
#         params = {"type": type_str, "offset": 0, "lim": type_lim, "duration": "monthly"}
#         res = requests.get(url, params=params)
#         data = res.json()
#     except requests.HTTPError as e:
#         print("HTTP Error:", e)
#     except json.JSONDecodeError as e:
#         print("JSON Decode Error:", e)
#
#     return regen_json(data["ranks"])


# デバッグ用のget_data
def get_ranking_data(arg: Type):
    json_sample = '{"result_count":20,"ranks":[{"player":{"name":"ilohas0096","uuid":"91c5a4c7-33f3-44d5-9965-56b0abfa4264"},"type":"break","rank":1,"data":{"raw_data":"904596154"},"lastquit":"2020-11-30 14:59:05"},{"player":{"name":"chorocra","uuid":"438ed7bf-cbcf-40d9-a672-aacc2868e267"},"type":"break","rank":2,"data":{"raw_data":"697895896"},"lastquit":"2020-11-30 14:59:05"},{"player":{"name":"zgonob","uuid":"870b8e91-1098-4cf6-bee5-fc05961acfd8"},"type":"break","rank":3,"data":{"raw_data":"320060245"},"lastquit":"2020-11-30 14:59:04"},{"player":{"name":"gettycraft","uuid":"3dc5d243-2c85-4abb-aada-237511b410b8"},"type":"break","rank":4,"data":{"raw_data":"246314391"},"lastquit":"2020-11-30 03:07:03"},{"player":{"name":"kurea32","uuid":"c5169f3f-263e-4bcc-96e2-aee61001b133"},"type":"break","rank":5,"data":{"raw_data":"216734324"},"lastquit":"2020-11-23 15:04:52"},{"player":{"name":"ru_rai721","uuid":"f9b57566-4921-44bf-9b86-418fa0cc7b76"},"type":"break","rank":6,"data":{"raw_data":"171517036"},"lastquit":"2020-11-29 23:33:57"},{"player":{"name":"ko0201_","uuid":"c6938a54-0631-4201-ba23-09dced95d41e"},"type":"break","rank":7,"data":{"raw_data":"165443790"},"lastquit":"2020-11-30 15:00:08"},{"player":{"name":"ainzhhh","uuid":"4a839cb8-aa43-438f-922b-b0c84eed40ae"},"type":"break","rank":8,"data":{"raw_data":"146693043"},"lastquit":"2020-11-30 07:19:59"},{"player":{"name":"tyanimo","uuid":"4becf8bc-9a46-4f8b-b6e6-9193cf53b46f"},"type":"break","rank":9,"data":{"raw_data":"145552722"},"lastquit":"2020-11-30 15:00:08"},{"player":{"name":"kei_3104","uuid":"73b41f61-3b2b-4730-b775-564516101b3c"},"type":"break","rank":10,"data":{"raw_data":"125890703"},"lastquit":"2020-11-30 14:59:12"},{"player":{"name":"_meltice_","uuid":"b38bc26f-955d-49b8-982f-0cb159bfe653"},"type":"break","rank":11,"data":{"raw_data":"119916061"},"lastquit":"2020-11-30 15:00:09"},{"player":{"name":"flame421","uuid":"ae34779a-e2bf-4559-882b-b52f05849c3e"},"type":"break","rank":12,"data":{"raw_data":"109540858"},"lastquit":"2020-11-29 18:34:08"},{"player":{"name":"koumei0722","uuid":"98ee2213-3f26-4efc-83a7-cfed8df6b51a"},"type":"break","rank":13,"data":{"raw_data":"104104063"},"lastquit":"2020-11-29 21:17:46"},{"player":{"name":"enon2750","uuid":"2353ffcf-7cf4-41f0-92c9-6f69debcaddd"},"type":"break","rank":14,"data":{"raw_data":"92679166"},"lastquit":"2020-11-29 23:08:08"},{"player":{"name":"kaerusan82433413","uuid":"9cec894e-9ae3-4a25-97c5-b7a6c55c1376"},"type":"break","rank":15,"data":{"raw_data":"84445237"},"lastquit":"2020-11-30 04:00:02"},{"player":{"name":"irohachan246","uuid":"3423c69b-a1cd-41cf-a896-992f9a6f5935"},"type":"break","rank":16,"data":{"raw_data":"83843300"},"lastquit":"2020-11-30 14:59:12"},{"player":{"name":"wanwanwan_o","uuid":"bab130b9-2247-4b18-967a-0867edcccf69"},"type":"break","rank":17,"data":{"raw_data":"81582284"},"lastquit":"2020-11-29 21:54:48"},{"player":{"name":"asobi_tai","uuid":"45b2190c-5b5b-4f0b-ba50-228562ddf6f0"},"type":"break","rank":18,"data":{"raw_data":"76703526"},"lastquit":"2020-11-30 11:00:18"},{"player":{"name":"mend3141","uuid":"deda238b-64a3-4931-8a85-f55109a57bb1"},"type":"break","rank":19,"data":{"raw_data":"73840355"},"lastquit":"2020-11-29 18:19:24"},{"player":{"name":"akaitachiiiiiiii","uuid":"3e75652f-46ed-4f0c-ad22-5deb3b362b78"},"type":"break","rank":20,"data":{"raw_data":"72748549"},"lastquit":"2020-11-06 20:59:52"}],"total_ranked_player":1398}'
    data = {}
    try:
        data = json.loads(json_sample)["ranks"]
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)
    return regen_json(data)


def regen_json(arg):
    result = []

    for data in arg:
        data["playername"] = data["player"]["name"]
        data["playeruuid"] = data["player"]["uuid"]
        data["amount"] = data["data"]["raw_data"]

        del data["lastquit"], data["player"], data["data"]

        result.append(data)

    return result
