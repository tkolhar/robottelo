"""API Tests for the email notification feature"""

from robottelo.decorators import stubbed, tier1
from robottelo.test import APITestCase


class EmailTestCase(APITestCase):
    """API Tests for the email notification feature"""

    @stubbed()
    @tier1
    def test_positive_enable_and_disable_notification(self):
        """@Test: Manage user email notification preferences.

        @Feature: Email Notification

        @Steps:

        1. Enable and disable email notifications using /api/mail_notifications

        @Assert: Enabling and disabling email notification preferences saved
        accordingly.

        @Status: Manual
        """
