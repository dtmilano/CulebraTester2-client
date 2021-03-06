# coding: utf-8

"""
    CulebraTester

    ## Snaky Android Test --- If you want to be able to try out the API using the **Execute** or **TRY** button from this page - an android device should be connected using `adb` - the server should have been started using `./culebratester2 start-server`  then you will be able to invoke the API and see the responses.   # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import sys
import unittest

from culebratester_client import api

import culebratester_client
#from api.default_api import DefaultApi  # noqa: E501
#from culebratester_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_culebra_help_api_get(self):
        """Test case for culebra_help_api_get

        Gets help  # noqa: E501
        """
        pass

    def test_culebra_info_get(self):
        """Test case for culebra_info_get

        Gets information about this app  # noqa: E501
        """
        pass

    def test_device_display_real_size_get(self):
        """Test case for device_display_real_size_get

        Gets display real size  # noqa: E501
        """
        pass

    def test_object_store_list_get(self):
        """Test case for object_store_list_get

        Lists the objects in store  # noqa: E501
        """
        pass

    def test_target_context_start_activity_get(self):
        """Test case for target_context_start_activity_get

        Starts an Activity  # noqa: E501
        """
        pass

    def test_ui_device_click_get(self):
        """Test case for ui_device_click_get

        Clicks at the specified location  # noqa: E501
        """
        pass

    def test_ui_device_current_package_name_get(self):
        """Test case for ui_device_current_package_name_get

        Gets the current package name  # noqa: E501
        """
        pass

    def test_ui_device_display_height_get(self):
        """Test case for ui_device_display_height_get

        Gets the display height  # noqa: E501
        """
        pass

    def test_ui_device_display_rotation_get(self):
        """Test case for ui_device_display_rotation_get

        Gets the display rotation  # noqa: E501
        """
        pass

    def test_ui_device_display_size_dp_get(self):
        """Test case for ui_device_display_size_dp_get

        Gets the display size in DP  # noqa: E501
        """
        pass

    def test_ui_device_display_width_get(self):
        """Test case for ui_device_display_width_get

        Gets the display width  # noqa: E501
        """
        pass

    def test_ui_device_dump_window_hierarchy_get_xml(self):
        """Test case for ui_device_dump_window_hierarchy_get

        Dumps the window hierarchy  # noqa: E501
        """
        api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient())
        api_response = api_instance.ui_device_dump_window_hierarchy_get(format='XML')
        print(api_response, file=sys.stderr)

    def test_ui_device_dump_window_hierarchy_get_json(self):
        """Test case for ui_device_dump_window_hierarchy_get

        Dumps the window hierarchy  # noqa: E501
        """
        api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient())
        api_response = api_instance.ui_device_dump_window_hierarchy_get(format='JSON')
        print(api_response, file=sys.stderr)

    def test_ui_device_find_object_get(self):
        """Test case for ui_device_find_object_get

        Finds an object  # noqa: E501
        """
        pass

    def test_ui_device_find_object_post(self):
        """Test case for ui_device_find_object_post

        Finds an object  # noqa: E501
        """
        pass

    def test_ui_device_last_traversed_text_get(self):
        """Test case for ui_device_last_traversed_text_get

        Retrieves the text from the last UI traversal event received.  # noqa: E501
        """
        pass

    def test_ui_device_press_back_get(self):
        """Test case for ui_device_press_back_get

        Simulates a short press on the BACK button.  # noqa: E501
        """
        pass

    def test_ui_device_press_delete_get(self):
        """Test case for ui_device_press_delete_get

        Simulates a short press on the DELETE key.  # noqa: E501
        """
        pass

    def test_ui_device_press_enter_get(self):
        """Test case for ui_device_press_enter_get

        Simulates a short press on the ENTER key.  # noqa: E501
        """
        pass

    def test_ui_device_press_home_get(self):
        """Test case for ui_device_press_home_get

        Simulates a short press on the HOME button.  # noqa: E501
        """
        pass

    def test_ui_device_press_key_code_get(self):
        """Test case for ui_device_press_key_code_get

        Simulates a short press using a key code.  # noqa: E501
        """
        pass

    def test_ui_device_product_name_get(self):
        """Test case for ui_device_product_name_get

        Retrieves the product name of the device.  # noqa: E501
        """
        pass

    def test_ui_device_screenshot_get(self):
        """Test case for ui_device_screenshot_get

        Gets the device screenshot  # noqa: E501
        """
        pass

    def test_ui_device_wait_for_idle_get(self):
        """Test case for ui_device_wait_for_idle_get

        Waits for the current application to idle.  # noqa: E501
        """
        pass

    def test_ui_device_wait_for_window_update_get(self):
        """Test case for ui_device_wait_for_window_update_get

        Waits for a window content update event to occur.  # noqa: E501
        """
        pass

    def test_ui_object2_oid_click_get(self):
        """Test case for ui_object2_oid_click_get

        Clicks on the specified object.  # noqa: E501
        """
        pass

    def test_ui_object2_oid_dump_get(self):
        """Test case for ui_object2_oid_dump_get

        Dumps the specified object.  # noqa: E501
        """
        pass

    def test_ui_object2_oid_set_text_post(self):
        """Test case for ui_object2_oid_set_text_post

        Sets the text content if this object is an editable field.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
