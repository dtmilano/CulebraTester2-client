# culebratester-client
## Snaky Android Test --- If you want to be able to try out the API using the **Execute** or **TRY** button from this page - an android device should be connected using `adb` - the server should have been started using `./culebratester2 start-server`  then you will be able to invoke the API and see the responses. 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.19
- Package version: 2.0.19
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import culebratester_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import culebratester_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
api = 'api_example' # str | Specify the API help is about

try:
    # Gets help
    api_response = api_instance.culebra_help_api_get(api)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->culebra_help_api_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))

try:
    # Gets information about this app
    api_response = api_instance.culebra_info_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->culebra_info_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))

try:
    # Gets display real size
    api_response = api_instance.device_display_real_size_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_display_real_size_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))

try:
    # Clears all the objects in store
    api_response = api_instance.object_store_clear_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->object_store_clear_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))

try:
    # Lists the objects in store
    api_response = api_instance.object_store_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->object_store_list_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
oid = 56 # int | The object ID

try:
    # Removes an object
    api_response = api_instance.object_store_remove_get(oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->object_store_remove_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
pkg = 'pkg_example' # str | the package name
cls = 'cls_example' # str | the class name

try:
    # Starts an Activity
    api_response = api_instance.target_context_start_activity_get(pkg, cls)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->target_context_start_activity_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
x = 56 # int | x coordinate
y = 56 # int | y coordinate

try:
    # Clicks at the specified location
    api_response = api_instance.ui_device_click_get(x, y)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_click_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))

try:
    # Gets the current package name
    api_response = api_instance.ui_device_current_package_name_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_current_package_name_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))

try:
    # Gets the display height
    api_response = api_instance.ui_device_display_height_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_display_height_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))

try:
    # Gets the display rotation
    api_response = api_instance.ui_device_display_rotation_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_display_rotation_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))

try:
    # Gets the display size in DP
    api_response = api_instance.ui_device_display_size_dp_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_display_size_dp_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))

try:
    # Gets the display width
    api_response = api_instance.ui_device_display_width_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_display_width_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
format = 'format_example' # str | the output format (optional)

try:
    # Dumps the window hierarchy
    api_response = api_instance.ui_device_dump_window_hierarchy_get(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_dump_window_hierarchy_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
resource_id = 'resource_id_example' # str | the resource id (optional)
ui_selector = 'ui_selector_example' # str | the selector sets the resource name criteria for matching. A UI element will be considered a match if its resource name exactly matches the selector parameter and all other criteria for this selector are met. The format of the selector string is `sel@[$]value,...` Where `sel` can be one of - clazz or className - clickable - depth - desc - index - instance - package - parentIndex - res - scrollable - text `@` replaces the `=` sign that is used to separate parameters and values in the URL. If the first character of value is `$` then a `Pattern` is created. (optional)
by_selector = 'by_selector_example' # str | the selector sets the resource name criteria for matching. A UI element will be considered a match if its resource name exactly matches the selector parameter and all other criteria for this selector are met. The format of the selector string is `sel@[$]value,...` Where `sel` can be one of - checkable - clazz - clickable - depth - desc - package - res - scrollable - text `@` replaces the `=` sign that is used to separate parameters and values in the URL. If the first character of value is `$` then a `Pattern` is created. (optional)

try:
    # Finds an object
    api_response = api_instance.ui_device_find_object_get(resource_id=resource_id, ui_selector=ui_selector, by_selector=by_selector)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_find_object_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
body = culebratester_client.Selector() # Selector | Selector

try:
    # Finds an object
    api_response = api_instance.ui_device_find_object_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_find_object_post: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
by_selector = 'by_selector_example' # str | the selector sets the resource name criteria for matching. A UI element will be considered a match if its resource name exactly matches the selector parameter and all other criteria for this selector are met. The format of the selector string is `sel@[$]value,...` Where `sel` can be one of - checkable - clazz - clickable - depth - desc - package - res - scrollable - text `@` replaces the `=` sign that is used to separate parameters and values in the URL. If the first character of value is `$` then a `Pattern` is created. (optional)

try:
    # Finds *all* objects that match the selector criteria.
    api_response = api_instance.ui_device_find_objects_get(by_selector=by_selector)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_find_objects_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))

try:
    # Retrieves the text from the last UI traversal event received.
    api_response = api_instance.ui_device_last_traversed_text_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_last_traversed_text_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))

try:
    # Simulates a short press on the BACK button.
    api_response = api_instance.ui_device_press_back_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_press_back_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))

try:
    # Simulates a short press on the DELETE key.
    api_response = api_instance.ui_device_press_delete_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_press_delete_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))

try:
    # Simulates a short press on the ENTER key.
    api_response = api_instance.ui_device_press_enter_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_press_enter_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))

try:
    # Simulates a short press on the HOME button.
    api_response = api_instance.ui_device_press_home_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_press_home_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
key_code = 56 # int | the key code of the event.
meta_state = 56 # int | an integer in which each bit set to 1 represents a pressed meta key (optional)

try:
    # Simulates a short press using a key code.
    api_response = api_instance.ui_device_press_key_code_get(key_code, meta_state=meta_state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_press_key_code_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))

try:
    # Simulates a short press on the Recent Apps button.
    api_response = api_instance.ui_device_press_recent_apps_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_press_recent_apps_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))

try:
    # Retrieves the product name of the device.
    api_response = api_instance.ui_device_product_name_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_product_name_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
scale = 3.4 # float | The scale of the screenshot (i.e. 0.5) (optional)
quality = 56 # int | The quality of the screenshot (i.e. 100) (optional)

try:
    # Gets the device screenshot
    api_response = api_instance.ui_device_screenshot_get(scale=scale, quality=quality)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_screenshot_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
start_x = 56 # int | from x
start_y = 56 # int | from y
end_x = 56 # int | to x
end_y = 56 # int | end y
steps = 56 # int | is the number of move steps sent to the system

try:
    # Performs a swipe.
    api_response = api_instance.ui_device_swipe_get(start_x, start_y, end_x, end_y, steps)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_swipe_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
body = culebratester_client.SwipeBody() # SwipeBody | 

try:
    # Performs a swipe between points in the Point array.
    api_response = api_instance.ui_device_swipe_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_swipe_post: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
timeout = 10000 # int | in milliseconds (optional) (default to 10000)

try:
    # Waits for the current application to idle.
    api_response = api_instance.ui_device_wait_for_idle_get(timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_wait_for_idle_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
timeout = 789 # int | in milliseconds
package_name = 'package_name_example' # str | the specified window package name (can be null or not present). If null, a window update from any front-end window will end the wait (optional)

try:
    # Waits for a window content update event to occur.
    api_response = api_instance.ui_device_wait_for_window_update_get(timeout, package_name=package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_wait_for_window_update_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
search_condition_ref = 789 # int | The search condition
timeout = 789 # int | The timeout in ms (optional)

try:
    # Waits for given the condition to be met.
    api_response = api_instance.ui_device_wait_get(search_condition_ref, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_wait_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
oid = 56 # int | The object ID

try:
    # Clears the text content if this object is an editable field.
    api_response = api_instance.ui_object2_oid_clear_get(oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_object2_oid_clear_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
oid = 56 # int | The object ID

try:
    # Clicks on the specified object.
    api_response = api_instance.ui_object2_oid_click_get(oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_object2_oid_click_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
oid = 56 # int | The object ID

try:
    # Dumps the specified object.
    api_response = api_instance.ui_object2_oid_dump_get(oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_object2_oid_dump_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
oid = 56 # int | The object ID

try:
    # Gets the text content.
    api_response = api_instance.ui_object2_oid_get_text_get(oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_object2_oid_get_text_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
oid = 56 # int | The object ID

try:
    # Long-clicks on the specified object.
    api_response = api_instance.ui_object2_oid_long_click_get(oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_object2_oid_long_click_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
oid = 56 # int | The object ID
text = 'text_example' # str | Text to enter in the field

try:
    # Sets the text content if this object is an editable field.
    api_response = api_instance.ui_object2_oid_set_text_get(oid, text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_object2_oid_set_text_get: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
body = culebratester_client.Text() # Text | Text to enter in the field
oid = 56 # int | The object ID

try:
    # Sets the text content if this object is an editable field.
    api_response = api_instance.ui_object2_oid_set_text_post(body, oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_object2_oid_set_text_post: %s\n" % e)

# create an instance of the API class
api_instance = culebratester_client.DefaultApi(culebratester_client.ApiClient(configuration))
by_selector = 'by_selector_example' # str | the selector sets the resource name criteria for matching. A UI element will be considered a match if its resource name exactly matches the selector parameter and all other criteria for this selector are met. The format of the selector string is `sel@[$]value,...` Where `sel` can be one of - checkable - clazz - clickable - depth - desc - package - res - scrollable - text `@` replaces the `=` sign that is used to separate parameters and values in the URL. If the first character of value is `$` then a `Pattern` is created. (optional)

try:
    # Returns a SearchCondition that is satisfied when at least one element matching the selector can be found.
    api_response = api_instance.until_find_object_get(by_selector=by_selector)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->until_find_object_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:9987/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**culebra_help_api_get**](docs/DefaultApi.md#culebra_help_api_get) | **GET** /culebra/help/{api} | Gets help
*DefaultApi* | [**culebra_info_get**](docs/DefaultApi.md#culebra_info_get) | **GET** /culebra/info | Gets information about this app
*DefaultApi* | [**device_display_real_size_get**](docs/DefaultApi.md#device_display_real_size_get) | **GET** /device/displayRealSize | Gets display real size
*DefaultApi* | [**object_store_clear_get**](docs/DefaultApi.md#object_store_clear_get) | **GET** /objectStore/clear | Clears all the objects in store
*DefaultApi* | [**object_store_list_get**](docs/DefaultApi.md#object_store_list_get) | **GET** /objectStore/list | Lists the objects in store
*DefaultApi* | [**object_store_remove_get**](docs/DefaultApi.md#object_store_remove_get) | **GET** /objectStore/remove | Removes an object
*DefaultApi* | [**target_context_start_activity_get**](docs/DefaultApi.md#target_context_start_activity_get) | **GET** /targetContext/startActivity | Starts an Activity
*DefaultApi* | [**ui_device_click_get**](docs/DefaultApi.md#ui_device_click_get) | **GET** /uiDevice/click | Clicks at the specified location
*DefaultApi* | [**ui_device_current_package_name_get**](docs/DefaultApi.md#ui_device_current_package_name_get) | **GET** /uiDevice/currentPackageName | Gets the current package name
*DefaultApi* | [**ui_device_display_height_get**](docs/DefaultApi.md#ui_device_display_height_get) | **GET** /uiDevice/displayHeight | Gets the display height
*DefaultApi* | [**ui_device_display_rotation_get**](docs/DefaultApi.md#ui_device_display_rotation_get) | **GET** /uiDevice/displayRotation | Gets the display rotation
*DefaultApi* | [**ui_device_display_size_dp_get**](docs/DefaultApi.md#ui_device_display_size_dp_get) | **GET** /uiDevice/displaySizeDp | Gets the display size in DP
*DefaultApi* | [**ui_device_display_width_get**](docs/DefaultApi.md#ui_device_display_width_get) | **GET** /uiDevice/displayWidth | Gets the display width
*DefaultApi* | [**ui_device_dump_window_hierarchy_get**](docs/DefaultApi.md#ui_device_dump_window_hierarchy_get) | **GET** /uiDevice/dumpWindowHierarchy | Dumps the window hierarchy
*DefaultApi* | [**ui_device_find_object_get**](docs/DefaultApi.md#ui_device_find_object_get) | **GET** /uiDevice/findObject | Finds an object
*DefaultApi* | [**ui_device_find_object_post**](docs/DefaultApi.md#ui_device_find_object_post) | **POST** /uiDevice/findObject | Finds an object
*DefaultApi* | [**ui_device_find_objects_get**](docs/DefaultApi.md#ui_device_find_objects_get) | **GET** /uiDevice/findObjects | Finds *all* objects that match the selector criteria.
*DefaultApi* | [**ui_device_last_traversed_text_get**](docs/DefaultApi.md#ui_device_last_traversed_text_get) | **GET** /uiDevice/lastTraversedText | Retrieves the text from the last UI traversal event received.
*DefaultApi* | [**ui_device_press_back_get**](docs/DefaultApi.md#ui_device_press_back_get) | **GET** /uiDevice/pressBack | Simulates a short press on the BACK button.
*DefaultApi* | [**ui_device_press_delete_get**](docs/DefaultApi.md#ui_device_press_delete_get) | **GET** /uiDevice/pressDelete | Simulates a short press on the DELETE key.
*DefaultApi* | [**ui_device_press_enter_get**](docs/DefaultApi.md#ui_device_press_enter_get) | **GET** /uiDevice/pressEnter | Simulates a short press on the ENTER key.
*DefaultApi* | [**ui_device_press_home_get**](docs/DefaultApi.md#ui_device_press_home_get) | **GET** /uiDevice/pressHome | Simulates a short press on the HOME button.
*DefaultApi* | [**ui_device_press_key_code_get**](docs/DefaultApi.md#ui_device_press_key_code_get) | **GET** /uiDevice/pressKeyCode | Simulates a short press using a key code.
*DefaultApi* | [**ui_device_press_recent_apps_get**](docs/DefaultApi.md#ui_device_press_recent_apps_get) | **GET** /uiDevice/pressRecentApps | Simulates a short press on the Recent Apps button.
*DefaultApi* | [**ui_device_product_name_get**](docs/DefaultApi.md#ui_device_product_name_get) | **GET** /uiDevice/productName | Retrieves the product name of the device.
*DefaultApi* | [**ui_device_screenshot_get**](docs/DefaultApi.md#ui_device_screenshot_get) | **GET** /uiDevice/screenshot | Gets the device screenshot
*DefaultApi* | [**ui_device_swipe_get**](docs/DefaultApi.md#ui_device_swipe_get) | **GET** /uiDevice/swipe | Performs a swipe.
*DefaultApi* | [**ui_device_swipe_post**](docs/DefaultApi.md#ui_device_swipe_post) | **POST** /uiDevice/swipe | Performs a swipe between points in the Point array.
*DefaultApi* | [**ui_device_wait_for_idle_get**](docs/DefaultApi.md#ui_device_wait_for_idle_get) | **GET** /uiDevice/waitForIdle | Waits for the current application to idle.
*DefaultApi* | [**ui_device_wait_for_window_update_get**](docs/DefaultApi.md#ui_device_wait_for_window_update_get) | **GET** /uiDevice/waitForWindowUpdate | Waits for a window content update event to occur.
*DefaultApi* | [**ui_device_wait_get**](docs/DefaultApi.md#ui_device_wait_get) | **GET** /uiDevice/wait | Waits for given the condition to be met.
*DefaultApi* | [**ui_object2_oid_clear_get**](docs/DefaultApi.md#ui_object2_oid_clear_get) | **GET** /uiObject2/{oid}/clear | Clears the text content if this object is an editable field.
*DefaultApi* | [**ui_object2_oid_click_get**](docs/DefaultApi.md#ui_object2_oid_click_get) | **GET** /uiObject2/{oid}/click | Clicks on the specified object.
*DefaultApi* | [**ui_object2_oid_dump_get**](docs/DefaultApi.md#ui_object2_oid_dump_get) | **GET** /uiObject2/{oid}/dump | Dumps the specified object.
*DefaultApi* | [**ui_object2_oid_get_text_get**](docs/DefaultApi.md#ui_object2_oid_get_text_get) | **GET** /uiObject2/{oid}/getText | Gets the text content.
*DefaultApi* | [**ui_object2_oid_long_click_get**](docs/DefaultApi.md#ui_object2_oid_long_click_get) | **GET** /uiObject2/{oid}/longClick | Long-clicks on the specified object.
*DefaultApi* | [**ui_object2_oid_set_text_get**](docs/DefaultApi.md#ui_object2_oid_set_text_get) | **GET** /uiObject2/{oid}/setText | Sets the text content if this object is an editable field.
*DefaultApi* | [**ui_object2_oid_set_text_post**](docs/DefaultApi.md#ui_object2_oid_set_text_post) | **POST** /uiObject2/{oid}/setText | Sets the text content if this object is an editable field.
*DefaultApi* | [**until_find_object_get**](docs/DefaultApi.md#until_find_object_get) | **GET** /until/findObject | Returns a SearchCondition that is satisfied when at least one element matching the selector can be found.

## Documentation For Models

 - [CulebraInfo](docs/CulebraInfo.md)
 - [CurrentPackageName](docs/CurrentPackageName.md)
 - [DisplayHeight](docs/DisplayHeight.md)
 - [DisplayRealSize](docs/DisplayRealSize.md)
 - [DisplayRotation](docs/DisplayRotation.md)
 - [DisplayRotationEnum](docs/DisplayRotationEnum.md)
 - [DisplaySizeDp](docs/DisplaySizeDp.md)
 - [DisplayWidth](docs/DisplayWidth.md)
 - [Help](docs/Help.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [LastTraversedText](docs/LastTraversedText.md)
 - [ObjectRef](docs/ObjectRef.md)
 - [Point](docs/Point.md)
 - [ProductName](docs/ProductName.md)
 - [Selector](docs/Selector.md)
 - [StatusResponse](docs/StatusResponse.md)
 - [SwipeBody](docs/SwipeBody.md)
 - [Text](docs/Text.md)
 - [WindowHierarchy](docs/WindowHierarchy.md)
 - [WindowHierarchyChild](docs/WindowHierarchyChild.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author


