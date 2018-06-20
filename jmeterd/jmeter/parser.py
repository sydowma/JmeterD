from rest_framework import parsers

class TextCSVParser(parsers.BaseParser):
    media_type = 'text/csv'

    def parse(self, stream, media_type=None, parse_context=None):

        return stream.read()


class JmxParser(parsers.BaseParser):
    media_type = 'application/octet-stream'

    def parse(self, stream, media_type=None, parse_context=None):

        return stream.read()
