from django_webtest import WebTest
from datetime import datetime
from mock import patch

class TestSidebar(WebTest):
    @patch('util.date_.now_')
    def test_contest_state(self, mock_now):
        mock_now.return_value = datetime(2014, 1, 1, 12, 0, 0)

        home = self.app.get('/')

        import ipdb; ipdb.set_trace()
