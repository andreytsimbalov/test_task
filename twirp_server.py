import random

from twirp.asgi import TwirpASGIApp

import haberdasher_twirp, haberdasher_pb2

class HaberdasherService(object):
    def GetDollarRate(self, context, valute_id):
        return haberdasher_pb2.DollarRate(
            name=random.choice(["bowler", "baseball cap", "top hat", "derby"]),
            char_code=random.choice(["white", "black", "brown", "red", "blue"]),
            value=123.1,
        )


service = haberdasher_twirp.HaberdasherServer(service=HaberdasherService())
app = TwirpASGIApp()
app.add_service(service)
