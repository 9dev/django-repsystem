from ._base import BaseTestCase

from django.contrib.auth.models import User


class TestReputation(BaseTestCase):

    def setUp(self):
        super(TestReputation, self).setUp()
        self.florence = User.objects.get(pk=1)

    def test_can_see_his_reputation_score(self):
        # Florence logs in.
        self.login_as_admin()

        # She hits the homepage.
        self.get('/')

        # She sees her reputation score.
        self.assertEqual(
            self.browser.find_element_by_id('id_reputation').text,
            '0',
        )

    def test_can_see_his_level(self):
        self.fail()

    def test_can_see_user_reputation_score_in_admin_panel(self):
        self.fail()

    def test_can_see_user_level_in_admin_panel(self):
        self.fail()

    def test_can_gain_reputation_for_performing_actions(self):
        self.fail()

    def test_can_level_up(self):
        self.fail()

    def test_can_see_his_reputation_history(self):
        self.fail()
