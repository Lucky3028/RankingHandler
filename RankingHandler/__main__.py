import os
import random
import time

from RankingHandler.json_handler import get_ranking_data
from RankingHandler.api_params import Type, get_winners_num, get_rank_under


def main():
    print("RankingHandler is going to execute the process for giving monthly prize.")
    print("")

    print("===今月の月別景品付与の対象になったプレイヤーの方々を一覧表示します。===")
    os.system("pause")

    print(f"（整地量：{get_rank_under(Type.BREAK)}名）")
    ranking_break = get_ranking_data(Type.BREAK)
    for data in ranking_break:
        print(data)
        time.sleep(0.2)

    print("")

    print(f"（建築量：{get_rank_under(Type.BUILD)}名）")
    ranking_build = get_ranking_data(Type.BUILD)
    for data in ranking_build:
        print(data)
        time.sleep(0.2)

    print("")

    print("===景品が実際に付与される方はこちら！===")
    os.system("pause")

    print(f"（整地量：{get_winners_num(Type.BREAK)}名／{get_rank_under(Type.BREAK)}名）")
    winners_break = random.sample(ranking_break, get_winners_num(Type.BREAK))
    for winner in winners_break:
        print(winner)
        time.sleep(1)

    print("")
    os.system("pause")
    print("")

    print(f"（建築量：{get_winners_num(Type.BUILD)}名／{get_rank_under(Type.BUILD)}名）")
    winners_build = random.sample(ranking_build, get_winners_num(Type.BUILD))
    for winner in winners_build:
        print(winner)
        time.sleep(1)

    print("")
    print("RankingHandler has completed the task.")


if __name__ == "__main__":
    main()
