from twirp.context import Context
from twirp.exceptions import TwirpServerException

import haberdasher_twirp, haberdasher_pb2

client = haberdasher_twirp.HaberdasherClient("http://localhost:3000")

try:
    response = client.GetDollarRate(ctx=Context(), request=haberdasher_pb2.ValuteId(id="R01235"))
    print(response)
except TwirpServerException as e:
    print(e.code, e.message, e.meta, e.to_dict())
