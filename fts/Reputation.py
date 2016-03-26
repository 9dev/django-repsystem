from ._base import BaseTestCase

from django.contrib.auth.models import User


class TestReputation(BaseTestCase):

    def setUp(self):
        super(TestReputation, self).setUp()
        self.florence = User.objects.get(pk=1)

    def publish_article(self):
        self.get('/create')
        self.set_field('id_title', 'Some title')
        self.set_field('id_content', 'Some content')
        self.submit()

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
        # Florence logs in.
        self.login_as_admin()

        # She hits the homepage.
        self.get('/')

        # She sees her level name and number.
        self.assertEqual(
            self.browser.find_element_by_id('id_level').text,
            '1 (Beginner)',
        )

    def test_can_see_user_reputation_score_and_level_in_admin_panel(self):
        # Florence logs in as an admin.
        self.login_as_admin()

        # She hits admin panel for User objects.
        self.get('/admin/auth/user')

        # She sees a row for her User object along with her reputation score and level.
        self.assertEqual(
            self.browser.find_element_by_class_name('row1').text,
            'admin admin@example.com Florence Jones 0 1 (Beginner)',
        )

    def test_can_gain_reputation_for_performing_actions(self):
        # Florence logs in as an admin.
        self.login_as_admin()

        # She hits Reputation section of admin panel.
        self.get('/admin/repsystem/reputation')

        # She sees her score is 0.
        self.assertEqual(
            self.browser.find_element_by_class_name('row1').text,
            'admin 0 1 (Beginner)',
        )

        # She performs an action to get some reputation points.
        self.publish_article()

        # She goes back to Reputation admin panel.
        self.get('/admin/repsystem/reputation')

        # She sees she's gained some reputation.
        self.assertEqual(
            self.browser.find_element_by_class_name('row1').text,
            'admin 10 1 (Beginner)',
        )

    def test_can_level_up(self):
        # Florence has almost reached the next level.
        reputation = self.florence.reputation
        reputation.score = 95
        reputation.save()

        # She logs in as an admin.
        self.login_as_admin()

        # She performs an action to gain some reputation points.
        self.publish_article()

        # She notices she just leveled up.
        self.assertEqual(
            self.browser.find_element_by_id('id_level').text,
            '2 (Master)',
        )

    def test_can_see_his_reputation_history(self):
        # She logs in as an admin.
        self.login_as_admin()

        # She performs several actions to gain some reputation points.
        self.publish_article()
        self.publish_article()
        self.publish_article()

        # She hits her reputation history page.
        self.get('/reputation_history')

        # She sees all her actions.
        self.assertIn(
            'You got 10 reputation points for: Publishing a new article.',
            self.browser.find_element_by_id('id_log_1').text
        )
        self.assertIn(
            'You got 10 reputation points for: Publishing a new article.',
            self.browser.find_element_by_id('id_log_2').text
        )
        self.assertIn(
            'You got 10 reputation points for: Publishing a new article.',
            self.browser.find_element_by_id('id_log_3').text
        )
