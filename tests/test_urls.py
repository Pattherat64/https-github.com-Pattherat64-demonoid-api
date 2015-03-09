from unittest import TestCase

from requests import Session

from demonoid.urls import BASE_URL, URL


class UrlTests(TestCase):

    def test_init_default_parameter_values(self):
        u = URL()
        self.assertEqual(BASE_URL, u.base_url)
        self.assertEqual('', u.path)
        self.assertEqual({}, u.params)
        self.assertIsInstance(u._session, Session)
        self.assertIsNone(u._DOM)

    def test_init_with_given_values(self):
        url = 'http://potato.com'
        path = '/salad'
        params = {'kickstarter': 'genius'}
        u = URL(url, path, params)
        self.assertEqual(url, u.base_url)
        self.assertEqual(path, u.path)
        self.assertEqual(params, u.params)
        self.assertIsInstance(u._session, Session)
        self.assertIsNone(u._DOM)

    def test_add_params(self):
        u = URL()
        params = {'page': 7, 'category': 0}
        u.add_params(params)
        self.assertEqual(params, u.params)

    def test_add_param(self):
        u = URL()
        u.add_param('page', 7)
        self.assertEqual({'page': 7}, u.params)

    def test_url_property(self):
        u = URL(BASE_URL, 'files')
        self.assertEqual(BASE_URL + 'files', u.url)

    def test_combine_path_when_trailing_slash_base_url(self):
        u = URL(BASE_URL)
        self.assertEqual(BASE_URL + 'files', u.combine('files'))

    def test_combine_path_when_base_url_without_trailing_slash(self):
        base_url = 'http://demonoid.pw'
        u = URL(base_url)
        self.assertEqual(base_url + '/files', u.combine('files'))

    def test_combine_path_with_trailing_slash_and_url_with_preceding_slash(self):
        u = URL(BASE_URL)
        self.assertEqual(BASE_URL + 'files', u.combine('/files'))

    def test_DOM_property_updates_DOM_when_called_for_the_first_time(self):
        pass

    def test_DOM_property_reuses_existing_DOM(self):
        pass

    def test_update_DOM(self):
        pass

    def test_fetch(self):
        pass

    def test_string_representation(self):
        pass
