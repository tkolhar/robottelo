"""Test module for Dashboard UI"""
from robottelo.decorators import stubbed, tier3
from robottelo.test import UITestCase


class DashboardTestCase(UITestCase):
    """Tests for Dashboard UI"""

    @stubbed()
    @tier3
    def test_save_dashboard(self):
        """@Test: Save the Dashboard UI

        @Feature: Dashboard

        @Steps:
        1.Navigate to Monitor -> Content Dashboard
        2.Try to remove some widgets
        3.Select the Manage Dropdown box
        4.Save the Dashboard

        @Assert: Dashboard Widgets are saved successfully.

        @Status: Manual
        """

    @stubbed()
    @tier3
    def test_reset_dashboard(self):
        """@Test: Reset the Dashboard to default UI

        @Feature: Dashboard

        @Steps:
        1.Navigate to Monitor -> Content Dashboard
        2.Try to remove some widgets
        3.Select the Manage Dropdown box
        4.Save the Dashboard
        5.Dashboard Widgets are saved successfully
        6.Click Reset to default

        @Assert: Dashboard is reset to default.

        @Status: Manual
        """

    @stubbed()
    @tier3
    def test_addwidgets_dashboard(self):
        """@Test: Add Widgets to Dashboard UI

        @Feature: Dashboard

        @Steps:
        1.Navigate to Monitor -> Content Dashboard
        2.Select Manage Dropdown box
        3.Add Widgets

        @Assert: User is able to add widgets.

        @Status: Manual
        """

    @stubbed()
    @tier3
    def test_bookmark_search_dashboard(self):
        """@Test: Bookmark the search filter in Dashboard UI

        @Feature: Dashboard

        @Steps:
        1.Navigate to Monitor -> Content Dashboard
        2.Add a filter to search box (eg. environment)
        3.Bookmark the search filter

        @Assert: User is able to list the Bookmark

        @Status: Manual
        """

    @stubbed()
    @tier3
    def test_host_configuration_status_dashboard(self):
        """@Test: Check if Host Configuration Status
        Widget links are working

        @Feature: Dashboard

        @Steps:
        1.Navigate to Monitor -> Content Dashboard
        2.Focus on the Host Configuration Status
        3.Select each of the link which
        has search string associated with it

        @Assert: Make sure each search takes you to correct info

        @Status: Manual
        """

    @stubbed()
    @tier3
    def test_host_configuration_dashboard(self):
        """@Test: Check if Host Configuration Chart
        is working in Dashboard UI

        @Feature: Dashboard

        @Steps:
        1.Navigate to Monitor -> Content Dashboard
        2.Focus on Host Configuration Chart
        3.Select the Circular chart which
        has search string associated with it

        @Assert: Make sure search string takes you to correct info

        @Status: Manual
        """

    @stubbed()
    @tier3
    def test_task_status_dashboard(self):
        """@Test: Check if Task Status Dashboard UI

        @Feature: Dashboard

        @Steps:
        1.Navigate to Monitor -> Content Dashboard
        2.Focus on Task Status
        3.Click each link

        @Assert: Make sure search string takes you to correct info

        @Status: Manual
        """

    @stubbed()
    @tier3
    def test_warning_error_task_status_dashboard(self):
        """@Test: Check if Latest Warning/Error
        Tasks Status are working in Dashboard UI

        @Feature: Dashboard

        @Steps:
        1.Navigate to Monitor -> Content Dashboard
        2.Focus on Latest Warning/Error Tasks

        @Assert: The links to all failed/warnings tasks are working

        @Status: Manual
        """

    @stubbed()
    @tier3
    def test_contentview_history_dashboard(self):
        """@Test: Check if Content View History
           are working in Dashboard UI

        @Feature: Dashboard

        @Steps:
        1.Navigate to Monitor -> Content Dashboard
        2.Focus on Content View History

        @Assert: Each Content View link shows its current status
        (the environment to which it is published)

        @Status: Manual
        """

    @stubbed()
    @tier3
    def test_discovered_host_dashboard(self):
        """@Test: Check if user can access
           Discovered Host [Widget]

        @Feature: Dashboard

        @Steps:
        1.Navigate to Monitor -> Content Dashboard
        2.Focus on Discovered Hosts
        3.Click on the list of Discovered Hosts

        @Assert: It takes you to discovered hosts

        @Status: Manual
        """
