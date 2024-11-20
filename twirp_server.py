from xml.etree.ElementTree import XML, fromstring
import aiohttp
import uvicorn
from twirp.asgi import TwirpASGIApp

import haberdasher_twirp
import haberdasher_pb2


def find_valute_by_id(xml_object: XML, id: str) -> (str, str, float):
    name = None
    char_code = None
    value = None
    for elem in xml_object:
        if elem.attrib["ID"] == id:
            for field in elem:
                if field.tag == 'Name':
                    name = field.text
                if field.tag == 'CharCode':
                    char_code = field.text
                if field.tag == 'Value':
                    value = float(field.text.replace(',', '.'))
            break
    if None in (name, char_code, value):
        raise Exception(f"Not correct ValuteId.id: {id}")
    return name, char_code, value


class HaberdasherService(object):
    async def GetDollarRate(self, context, valute_id):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://www.cbr.ru/scripts/XML_daily.asp') as response:
                text = await response.text()
                result_xml = fromstring(text)
                name, char_code, value = find_valute_by_id(result_xml, valute_id.id)

        return haberdasher_pb2.DollarRate(
            name=name,
            char_code=char_code,
            value=value,
        )


service = haberdasher_twirp.HaberdasherServer(service=HaberdasherService())
app = TwirpASGIApp()
app.add_service(service)


if __name__ == "__main__":
    uvicorn.run(
        'twirp_server:app',
        host="0.0.0.0",
        port=3000,
    )
