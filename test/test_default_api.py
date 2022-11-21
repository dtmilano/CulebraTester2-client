# coding: utf-8

"""
    CulebraTester

    ## Snaky Android Test --- If you want to be able to try out the API using the **Execute** or **TRY** button from this page - an android device should be connected using `adb` - the server should have been started using `./culebratester2 start-server`  then you will be able to invoke the API and see the responses.   # noqa: E501

    OpenAPI spec version: 2.0.57
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import culebratester_client
from culebratester_client.api.default_api import DefaultApi  # noqa: E501
from culebratester_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_configurator_get_wait_for_idle_timeout_get(self):
        """Test case for configurator_get_wait_for_idle_timeout_get

        Gets the current timeout used for waiting for the user interface to go into an idle state.  # noqa: E501
        """
        pass

    def test_configurator_set_wait_for_idle_timeout_get(self):
        """Test case for configurator_set_wait_for_idle_timeout_get

        Sets the timeout for waiting for the user interface to go into an idle state before starting a uiautomator action.  # noqa: E501
        """
        pass

    def test_culebra_help_api_get(self):
        """Test case for culebra_help_api_get

        Gets help  # noqa: E501
        """
        pass

    def test_culebra_info_get(self):
        """Test case for culebra_info_get

        Gets information about this app.  # noqa: E501
        """
        pass

    def test_culebra_quit_get(self):
        """Test case for culebra_quit_get

        Quits culebra server.  # noqa: E501
        """
        pass

    def test_device_display_real_size_get(self):
        """Test case for device_display_real_size_get

        Gets display real size.  # noqa: E501
        """
        pass

    def test_device_dumpsys_get(self):
        """Test case for device_dumpsys_get

        """
        pass

    def test_device_locale_get(self):
        """Test case for device_locale_get

        """
        pass

    def test_device_locale_post(self):
        """Test case for device_locale_post

        """
        pass

    def test_device_wait_for_new_toast_get(self):
        """Test case for device_wait_for_new_toast_get

        Waits for a new Toast.  # noqa: E501
        """
        pass

    def test_object_store_clear_get(self):
        """Test case for object_store_clear_get

        Clears all the objects in store.  # noqa: E501
        """
        pass

    def test_object_store_list_get(self):
        """Test case for object_store_list_get

        Lists the objects in store.  # noqa: E501
        """
        pass

    def test_object_store_remove_get(self):
        """Test case for object_store_remove_get

        Removes an object.  # noqa: E501
        """
        pass

    def test_target_context_start_activity_get(self):
        """Test case for target_context_start_activity_get

        Starts an Activity.  # noqa: E501
        """
        pass

    def test_ui_device_clear_last_traversed_text_get(self):
        """Test case for ui_device_clear_last_traversed_text_get

        Clears the text from the last UI traversal event.  # noqa: E501
        """
        pass

    def test_ui_device_click_get(self):
        """Test case for ui_device_click_get

        Clicks at the specified location.  # noqa: E501
        """
        pass

    def test_ui_device_click_post(self):
        """Test case for ui_device_click_post

        Clicks at the specified locations.  # noqa: E501
        """
        pass

    def test_ui_device_current_package_name_get(self):
        """Test case for ui_device_current_package_name_get

        Gets the current package name.  # noqa: E501
        """
        pass

    def test_ui_device_display_height_get(self):
        """Test case for ui_device_display_height_get

        Gets the display height.  # noqa: E501
        """
        pass

    def test_ui_device_display_rotation_get(self):
        """Test case for ui_device_display_rotation_get

        Gets the display rotation.  # noqa: E501
        """
        pass

    def test_ui_device_display_size_dp_get(self):
        """Test case for ui_device_display_size_dp_get

        Gets the display size in DP.  # noqa: E501
        """
        pass

    def test_ui_device_display_width_get(self):
        """Test case for ui_device_display_width_get

        Gets the display width.  # noqa: E501
        """
        pass

    def test_ui_device_drag_get(self):
        """Test case for ui_device_drag_get

        Performs a swipe from one coordinate to another coordinate.  # noqa: E501
        """
        pass

    def test_ui_device_dump_window_hierarchy_get(self):
        """Test case for ui_device_dump_window_hierarchy_get

        Dumps the window hierarchy.  # noqa: E501
        """
        pass

    def test_ui_device_find_object_get(self):
        """Test case for ui_device_find_object_get

        Finds an object.  # noqa: E501
        """
        pass

    def test_ui_device_find_object_post(self):
        """Test case for ui_device_find_object_post

        Finds an object.  # noqa: E501
        """
        pass

    def test_ui_device_find_objects_get(self):
        """Test case for ui_device_find_objects_get

        Finds *all* objects that match the selector criteria.  # noqa: E501
        """
        pass

    def test_ui_device_find_objects_post(self):
        """Test case for ui_device_find_objects_post

        Finds *all* objects.  # noqa: E501
        """
        pass

    def test_ui_device_freeze_rotation_get(self):
        """Test case for ui_device_freeze_rotation_get

        Disables the sensors and freezes the device rotation at its current rotation state.  # noqa: E501
        """
        pass

    def test_ui_device_has_object_get(self):
        """Test case for ui_device_has_object_get

        Returns whether there is a match for the given selector criteria.  # noqa: E501
        """
        pass

    def test_ui_device_has_object_post(self):
        """Test case for ui_device_has_object_post

        Returns whether there is a match for the given selector criteria.  # noqa: E501
        """
        pass

    def test_ui_device_is_natural_orientation_get(self):
        """Test case for ui_device_is_natural_orientation_get

        Check if the device is in its natural orientation.  # noqa: E501
        """
        pass

    def test_ui_device_is_screen_on_get(self):
        """Test case for ui_device_is_screen_on_get

        Checks the power manager if the screen is ON.  # noqa: E501
        """
        pass

    def test_ui_device_last_traversed_text_get(self):
        """Test case for ui_device_last_traversed_text_get

        Retrieves the text from the last UI traversal event received.  # noqa: E501
        """
        pass

    def test_ui_device_pixel_get(self):
        """Test case for ui_device_pixel_get

        Gets a pixel from device screen.  # noqa: E501
        """
        pass

    def test_ui_device_press_back_get(self):
        """Test case for ui_device_press_back_get

        Simulates a short press on the BACK button.  # noqa: E501
        """
        pass

    def test_ui_device_press_d_pad_center_get(self):
        """Test case for ui_device_press_d_pad_center_get

        Simulates a short press on the CENTER button.  # noqa: E501
        """
        pass

    def test_ui_device_press_d_pad_down_get(self):
        """Test case for ui_device_press_d_pad_down_get

        Simulates a short press on the DOWN button.  # noqa: E501
        """
        pass

    def test_ui_device_press_d_pad_left_get(self):
        """Test case for ui_device_press_d_pad_left_get

        Simulates a short press on the LEFT button.  # noqa: E501
        """
        pass

    def test_ui_device_press_d_pad_right_get(self):
        """Test case for ui_device_press_d_pad_right_get

        Simulates a short press on the RIGHT button.  # noqa: E501
        """
        pass

    def test_ui_device_press_d_pad_up_get(self):
        """Test case for ui_device_press_d_pad_up_get

        Simulates a short press on the UP button.  # noqa: E501
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

    def test_ui_device_press_recent_apps_get(self):
        """Test case for ui_device_press_recent_apps_get

        Simulates a short press on the Recent Apps button.  # noqa: E501
        """
        pass

    def test_ui_device_product_name_get(self):
        """Test case for ui_device_product_name_get

        Retrieves the product name of the device.  # noqa: E501
        """
        pass

    def test_ui_device_screenshot_get(self):
        """Test case for ui_device_screenshot_get

        Gets the device screenshot.  # noqa: E501
        """
        pass

    def test_ui_device_swipe_get(self):
        """Test case for ui_device_swipe_get

        Performs a swipe.  # noqa: E501
        """
        pass

    def test_ui_device_swipe_post(self):
        """Test case for ui_device_swipe_post

        Performs a swipe between points in the Point array.  # noqa: E501
        """
        pass

    def test_ui_device_unfreeze_rotation_get(self):
        """Test case for ui_device_unfreeze_rotation_get

        Re-enables the sensors and un-freezes the device rotation allowing its contents to rotate with the device physical rotation  # noqa: E501
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

    def test_ui_device_wait_get(self):
        """Test case for ui_device_wait_get

        Waits for given the condition to be met.  # noqa: E501
        """
        pass

    def test_ui_object2_oid_clear_get(self):
        """Test case for ui_object2_oid_clear_get

        Clears the text content if this object is an editable field.  # noqa: E501
        """
        pass

    def test_ui_object2_oid_click_and_wait_get(self):
        """Test case for ui_object2_oid_click_and_wait_get

        Clicks on the specified object.  # noqa: E501
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

    def test_ui_object2_oid_find_object_get(self):
        """Test case for ui_object2_oid_find_object_get

        Finds an object.  # noqa: E501
        """
        pass

    def test_ui_object2_oid_find_object_post(self):
        """Test case for ui_object2_oid_find_object_post

        Finds an object.  # noqa: E501
        """
        pass

    def test_ui_object2_oid_get_content_description_get(self):
        """Test case for ui_object2_oid_get_content_description_get

        Returns the content description for this object.  # noqa: E501
        """
        pass

    def test_ui_object2_oid_get_text_get(self):
        """Test case for ui_object2_oid_get_text_get

        Gets the text content.  # noqa: E501
        """
        pass

    def test_ui_object2_oid_long_click_get(self):
        """Test case for ui_object2_oid_long_click_get

        Long-clicks on the specified object.  # noqa: E501
        """
        pass

    def test_ui_object2_oid_set_text_get(self):
        """Test case for ui_object2_oid_set_text_get

        Sets the text content if this object is an editable field.  # noqa: E501
        """
        pass

    def test_ui_object2_oid_set_text_post(self):
        """Test case for ui_object2_oid_set_text_post

        Sets the text content if this object is an editable field.  # noqa: E501
        """
        pass

    def test_ui_object_oid_clear_text_field_get(self):
        """Test case for ui_object_oid_clear_text_field_get

        Clears the existing text contents in an editable field.  # noqa: E501
        """
        pass

    def test_ui_object_oid_click_and_wait_for_new_window_get(self):
        """Test case for ui_object_oid_click_and_wait_for_new_window_get

        Clicks on the specified object.  # noqa: E501
        """
        pass

    def test_ui_object_oid_click_get(self):
        """Test case for ui_object_oid_click_get

        Clicks on the specified object.  # noqa: E501
        """
        pass

    def test_ui_object_oid_dump_get(self):
        """Test case for ui_object_oid_dump_get

        Dumps the specified object.  # noqa: E501
        """
        pass

    def test_ui_object_oid_exists_get(self):
        """Test case for ui_object_oid_exists_get

        This basically returns immediately whether the view represented by this UiObject exists or not. If you need to wait longer for this view, then see waitForExists.  # noqa: E501
        """
        pass

    def test_ui_object_oid_get_child_count_get(self):
        """Test case for ui_object_oid_get_child_count_get

        Counts the child views immediately under the present UiObject.  # noqa: E501
        """
        pass

    def test_ui_object_oid_perform_two_pointer_gesture_post(self):
        """Test case for ui_object_oid_perform_two_pointer_gesture_post

        """
        pass

    def test_ui_object_oid_pinch_in_get(self):
        """Test case for ui_object_oid_pinch_in_get

        """
        pass

    def test_ui_object_oid_pinch_out_get(self):
        """Test case for ui_object_oid_pinch_out_get

        """
        pass

    def test_ui_object_oid_wait_for_exists_get(self):
        """Test case for ui_object_oid_wait_for_exists_get

        This method waits until the view becomes visible on the display, or until the timeout has elapsed. You can use this method in situations where the content that you want to select is not immediately displayed.  # noqa: E501
        """
        pass

    def test_until_find_object_get(self):
        """Test case for until_find_object_get

        Returns a SearchCondition that is satisfied when at least one element matching the selector can be found.  # noqa: E501
        """
        pass

    def test_until_find_object_post(self):
        """Test case for until_find_object_post

        Returns a SearchCondition that is satisfied when at least one element matching the selector can be found.  # noqa: E501
        """
        pass

    def test_until_find_objects_get(self):
        """Test case for until_find_objects_get

        Returns a SearchCondition that is satisfied when at least one element matching the selector can be found.  # noqa: E501
        """
        pass

    def test_until_find_objects_post(self):
        """Test case for until_find_objects_post

        Returns a SearchCondition that is satisfied when at least one element matching the selector can be found.  # noqa: E501
        """
        pass

    def test_until_new_window_get(self):
        """Test case for until_new_window_get

        Returns a condition that depends on a new window having appeared.  # noqa: E501
        """
        pass

    def test_until_oid_dump_get(self):
        """Test case for until_oid_dump_get

        Dumps the specified object.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
