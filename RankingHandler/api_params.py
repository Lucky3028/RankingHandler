from enum import Enum, auto


class Type(Enum):
    BREAK = auto()
    BUILD = auto()


def get_string(arg: Type):
    if arg == Type.BREAK:
        return "break"
    elif arg == Type.BUILD:
        return "build"
    else:
        raise TypeError("Unexpected arg:", arg)


def get_rank_under(arg: Type):
    if arg == Type.BREAK:
        return 20
    elif arg == Type.BUILD:
        return 10
    else:
        raise TypeError("Unexpected arg:", arg)


def get_winners_num(arg: Type):
    if arg == Type.BREAK:
        return 3
    elif arg == Type.BUILD:
        return 2
    else:
        raise TypeError("Unexpected arg:", arg)
