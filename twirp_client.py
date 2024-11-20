from twirp.context import Context
from twirp.exceptions import TwirpServerException

import haberdasher_twirp
import haberdasher_pb2

client = haberdasher_twirp.HaberdasherClient("http://localhost:3000")


def get_valute(id_str: str = "R01235"):
    try:
        response = client.GetDollarRate(ctx=Context(), request=haberdasher_pb2.ValuteId(id=id_str))
        print(response)
    except TwirpServerException as e:
        print(e.code, e.message, e.meta, e.to_dict())


if __name__ == "__main__":
    get_valute()
