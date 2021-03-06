from flask import url_for

from catwatch.tests.lib.util import ViewTestMixin


class TestLiveStream(ViewTestMixin):
    def test_live_stream_page(self):
        """ Live stream page renders successfully. """
        self.login()
        response = self.client.get(url_for('stream.live_stream'))

        assert response.status_code == 200

    def test_live_stream_contains_variables(self):
        """ Live stream page has various websocket variables. """
        self.login()
        response = self.client.get(url_for('stream.live_stream'))

        html = response.data

        assert 'data-faye-public-url="http://localhost:4242/stream"' in html
        assert 'src="http://localhost:4242/stream/client.js"' in html
        assert '<div id="broadcast"></div>' in html
