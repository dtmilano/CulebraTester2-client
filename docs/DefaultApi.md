# culebratester_client.DefaultApi

All URIs are relative to *http://localhost:9987/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**culebra_help_api_get**](DefaultApi.md#culebra_help_api_get) | **GET** /culebra/help/{api} | Gets help
[**culebra_info_get**](DefaultApi.md#culebra_info_get) | **GET** /culebra/info | Gets information about this app
[**device_display_real_size_get**](DefaultApi.md#device_display_real_size_get) | **GET** /device/displayRealSize | Gets display real size
[**object_store_clear_get**](DefaultApi.md#object_store_clear_get) | **GET** /objectStore/clear | Clears all the objects in store
[**object_store_list_get**](DefaultApi.md#object_store_list_get) | **GET** /objectStore/list | Lists the objects in store
[**object_store_remove_get**](DefaultApi.md#object_store_remove_get) | **GET** /objectStore/remove | Removes an object
[**target_context_start_activity_get**](DefaultApi.md#target_context_start_activity_get) | **GET** /targetContext/startActivity | Starts an Activity
[**ui_device_click_get**](DefaultApi.md#ui_device_click_get) | **GET** /uiDevice/click | Clicks at the specified location
[**ui_device_current_package_name_get**](DefaultApi.md#ui_device_current_package_name_get) | **GET** /uiDevice/currentPackageName | Gets the current package name
[**ui_device_display_height_get**](DefaultApi.md#ui_device_display_height_get) | **GET** /uiDevice/displayHeight | Gets the display height
[**ui_device_display_rotation_get**](DefaultApi.md#ui_device_display_rotation_get) | **GET** /uiDevice/displayRotation | Gets the display rotation
[**ui_device_display_size_dp_get**](DefaultApi.md#ui_device_display_size_dp_get) | **GET** /uiDevice/displaySizeDp | Gets the display size in DP
[**ui_device_display_width_get**](DefaultApi.md#ui_device_display_width_get) | **GET** /uiDevice/displayWidth | Gets the display width
[**ui_device_dump_window_hierarchy_get**](DefaultApi.md#ui_device_dump_window_hierarchy_get) | **GET** /uiDevice/dumpWindowHierarchy | Dumps the window hierarchy
[**ui_device_find_object_get**](DefaultApi.md#ui_device_find_object_get) | **GET** /uiDevice/findObject | Finds an object
[**ui_device_find_object_post**](DefaultApi.md#ui_device_find_object_post) | **POST** /uiDevice/findObject | Finds an object
[**ui_device_find_objects_get**](DefaultApi.md#ui_device_find_objects_get) | **GET** /uiDevice/findObjects | Finds *all* objects that match the selector criteria.
[**ui_device_last_traversed_text_get**](DefaultApi.md#ui_device_last_traversed_text_get) | **GET** /uiDevice/lastTraversedText | Retrieves the text from the last UI traversal event received.
[**ui_device_press_back_get**](DefaultApi.md#ui_device_press_back_get) | **GET** /uiDevice/pressBack | Simulates a short press on the BACK button.
[**ui_device_press_delete_get**](DefaultApi.md#ui_device_press_delete_get) | **GET** /uiDevice/pressDelete | Simulates a short press on the DELETE key.
[**ui_device_press_enter_get**](DefaultApi.md#ui_device_press_enter_get) | **GET** /uiDevice/pressEnter | Simulates a short press on the ENTER key.
[**ui_device_press_home_get**](DefaultApi.md#ui_device_press_home_get) | **GET** /uiDevice/pressHome | Simulates a short press on the HOME button.
[**ui_device_press_key_code_get**](DefaultApi.md#ui_device_press_key_code_get) | **GET** /uiDevice/pressKeyCode | Simulates a short press using a key code.
[**ui_device_press_recent_apps_get**](DefaultApi.md#ui_device_press_recent_apps_get) | **GET** /uiDevice/pressRecentApps | Simulates a short press on the Recent Apps button.
[**ui_device_product_name_get**](DefaultApi.md#ui_device_product_name_get) | **GET** /uiDevice/productName | Retrieves the product name of the device.
[**ui_device_screenshot_get**](DefaultApi.md#ui_device_screenshot_get) | **GET** /uiDevice/screenshot | Gets the device screenshot
[**ui_device_swipe_get**](DefaultApi.md#ui_device_swipe_get) | **GET** /uiDevice/swipe | Performs a swipe.
[**ui_device_swipe_post**](DefaultApi.md#ui_device_swipe_post) | **POST** /uiDevice/swipe | Performs a swipe between points in the Point array.
[**ui_device_wait_for_idle_get**](DefaultApi.md#ui_device_wait_for_idle_get) | **GET** /uiDevice/waitForIdle | Waits for the current application to idle.
[**ui_device_wait_for_window_update_get**](DefaultApi.md#ui_device_wait_for_window_update_get) | **GET** /uiDevice/waitForWindowUpdate | Waits for a window content update event to occur.
[**ui_object2_oid_click_get**](DefaultApi.md#ui_object2_oid_click_get) | **GET** /uiObject2/{oid}/click | Clicks on the specified object.
[**ui_object2_oid_dump_get**](DefaultApi.md#ui_object2_oid_dump_get) | **GET** /uiObject2/{oid}/dump | Dumps the specified object.
[**ui_object2_oid_get_text_get**](DefaultApi.md#ui_object2_oid_get_text_get) | **GET** /uiObject2/{oid}/getText | Gets the text content.
[**ui_object2_oid_long_click_get**](DefaultApi.md#ui_object2_oid_long_click_get) | **GET** /uiObject2/{oid}/longClick | Long-clicks on the specified object.
[**ui_object2_oid_set_text_post**](DefaultApi.md#ui_object2_oid_set_text_post) | **POST** /uiObject2/{oid}/setText | Sets the text content if this object is an editable field.

# **culebra_help_api_get**
> Help culebra_help_api_get(api)

Gets help

Gets help info about the *API* specified as parameter. For example you can obtain information about * /uiDevice/click * /device/displayRealSize * /uiDevice/screenshot * etc.

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()
api = 'api_example' # str | Specify the API help is about

try:
    # Gets help
    api_response = api_instance.culebra_help_api_get(api)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->culebra_help_api_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| Specify the API help is about | 

### Return type

[**Help**](Help.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **culebra_info_get**
> CulebraInfo culebra_info_get()

Gets information about this app

Gets information about this app

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()

try:
    # Gets information about this app
    api_response = api_instance.culebra_info_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->culebra_info_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CulebraInfo**](CulebraInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_display_real_size_get**
> DisplayRealSize device_display_real_size_get()

Gets display real size

Gets the display real size

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()

try:
    # Gets display real size
    api_response = api_instance.device_display_real_size_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_display_real_size_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DisplayRealSize**](DisplayRealSize.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_store_clear_get**
> StatusResponse object_store_clear_get()

Clears all the objects in store

Clears all the objects in store

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()

try:
    # Clears all the objects in store
    api_response = api_instance.object_store_clear_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->object_store_clear_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_store_list_get**
> list[InlineResponse200] object_store_list_get()

Lists the objects in store

Lists the objects in store

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()

try:
    # Lists the objects in store
    api_response = api_instance.object_store_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->object_store_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_store_remove_get**
> StatusResponse object_store_remove_get(oid)

Removes an object

Removes an object that has been stored in ObjectStore

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()
oid = 56 # int | The object ID

try:
    # Removes an object
    api_response = api_instance.object_store_remove_get(oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->object_store_remove_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **int**| The object ID | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **target_context_start_activity_get**
> StatusResponse target_context_start_activity_get(pkg, cls)

Starts an Activity

Starts an Activity

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()
pkg = 'pkg_example' # str | the package name
cls = 'cls_example' # str | the class name

try:
    # Starts an Activity
    api_response = api_instance.target_context_start_activity_get(pkg, cls)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->target_context_start_activity_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pkg** | **str**| the package name | 
 **cls** | **str**| the class name | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_click_get**
> StatusResponse ui_device_click_get(x, y)

Clicks at the specified location

Clicks at the specified location

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()
x = 56 # int | x coordinate
y = 56 # int | y coordinate

try:
    # Clicks at the specified location
    api_response = api_instance.ui_device_click_get(x, y)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_click_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x** | **int**| x coordinate | 
 **y** | **int**| y coordinate | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_current_package_name_get**
> CurrentPackageName ui_device_current_package_name_get()

Gets the current package name

Gets the current package name

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()

try:
    # Gets the current package name
    api_response = api_instance.ui_device_current_package_name_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_current_package_name_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrentPackageName**](CurrentPackageName.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_display_height_get**
> DisplayHeight ui_device_display_height_get()

Gets the display height

Gets the display height

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()

try:
    # Gets the display height
    api_response = api_instance.ui_device_display_height_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_display_height_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DisplayHeight**](DisplayHeight.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_display_rotation_get**
> DisplayRotation ui_device_display_rotation_get()

Gets the display rotation

Gets the display rotation

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()

try:
    # Gets the display rotation
    api_response = api_instance.ui_device_display_rotation_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_display_rotation_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DisplayRotation**](DisplayRotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_display_size_dp_get**
> DisplaySizeDp ui_device_display_size_dp_get()

Gets the display size in DP

Gets the display size in DP

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()

try:
    # Gets the display size in DP
    api_response = api_instance.ui_device_display_size_dp_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_display_size_dp_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DisplaySizeDp**](DisplaySizeDp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_display_width_get**
> DisplayWidth ui_device_display_width_get()

Gets the display width

Gets the display width

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()

try:
    # Gets the display width
    api_response = api_instance.ui_device_display_width_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_display_width_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DisplayWidth**](DisplayWidth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_dump_window_hierarchy_get**
> WindowHierarchy ui_device_dump_window_hierarchy_get(format=format)

Dumps the window hierarchy

Dumps the window hierarchy

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()
format = 'format_example' # str | the output format (optional)

try:
    # Dumps the window hierarchy
    api_response = api_instance.ui_device_dump_window_hierarchy_get(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_dump_window_hierarchy_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| the output format | [optional] 

### Return type

[**WindowHierarchy**](WindowHierarchy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_find_object_get**
> ObjectRef ui_device_find_object_get(resource_id=resource_id, ui_selector=ui_selector, by_selector=by_selector)

Finds an object

Finds an object. The object found, if any, can be later used in other call like API.click.

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()
resource_id = 'resource_id_example' # str | the resource id (optional)
ui_selector = 'ui_selector_example' # str | the selector sets the resource name criteria for matching. A UI element will be considered a match if its resource name exactly matches the selector parameter and all other criteria for this selector are met. The format of the selector string is `sel@[$]value,...` Where `sel` can be one of - clazz or className - clickable - depth - desc - index - instance - package - parentIndex - res - scrollable - text `@` replaces the `=` sign that is used to separate parameters and values in the URL. If the first character of value is `$` then a `Pattern` is created. (optional)
by_selector = 'by_selector_example' # str | the selector sets the resource name criteria for matching. A UI element will be considered a match if its resource name exactly matches the selector parameter and all other criteria for this selector are met. The format of the selector string is `sel@[$]value,...` Where `sel` can be one of - checkable - clazz - clickable - depth - desc - package - res - scrollable - text `@` replaces the `=` sign that is used to separate parameters and values in the URL. If the first character of value is `$` then a `Pattern` is created. (optional)

try:
    # Finds an object
    api_response = api_instance.ui_device_find_object_get(resource_id=resource_id, ui_selector=ui_selector, by_selector=by_selector)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_find_object_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| the resource id | [optional] 
 **ui_selector** | **str**| the selector sets the resource name criteria for matching. A UI element will be considered a match if its resource name exactly matches the selector parameter and all other criteria for this selector are met. The format of the selector string is &#x60;sel@[$]value,...&#x60; Where &#x60;sel&#x60; can be one of - clazz or className - clickable - depth - desc - index - instance - package - parentIndex - res - scrollable - text &#x60;@&#x60; replaces the &#x60;&#x3D;&#x60; sign that is used to separate parameters and values in the URL. If the first character of value is &#x60;$&#x60; then a &#x60;Pattern&#x60; is created. | [optional] 
 **by_selector** | **str**| the selector sets the resource name criteria for matching. A UI element will be considered a match if its resource name exactly matches the selector parameter and all other criteria for this selector are met. The format of the selector string is &#x60;sel@[$]value,...&#x60; Where &#x60;sel&#x60; can be one of - checkable - clazz - clickable - depth - desc - package - res - scrollable - text &#x60;@&#x60; replaces the &#x60;&#x3D;&#x60; sign that is used to separate parameters and values in the URL. If the first character of value is &#x60;$&#x60; then a &#x60;Pattern&#x60; is created. | [optional] 

### Return type

[**ObjectRef**](ObjectRef.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_find_object_post**
> ObjectRef ui_device_find_object_post(body)

Finds an object

Finds an object. The object found, if any, can be later used in other call like API.click.

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()
body = culebratester_client.Selector() # Selector | Selector

try:
    # Finds an object
    api_response = api_instance.ui_device_find_object_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_find_object_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Selector**](Selector.md)| Selector | 

### Return type

[**ObjectRef**](ObjectRef.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_find_objects_get**
> list[ObjectRef] ui_device_find_objects_get(by_selector=by_selector)

Finds *all* objects that match the selector criteria.

Finds an object. The object found, if any, can be later used in other call like API.click.

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()
by_selector = 'by_selector_example' # str | the selector sets the resource name criteria for matching. A UI element will be considered a match if its resource name exactly matches the selector parameter and all other criteria for this selector are met. The format of the selector string is `sel@[$]value,...` Where `sel` can be one of - checkable - clazz - clickable - depth - desc - package - res - scrollable - text `@` replaces the `=` sign that is used to separate parameters and values in the URL. If the first character of value is `$` then a `Pattern` is created. (optional)

try:
    # Finds *all* objects that match the selector criteria.
    api_response = api_instance.ui_device_find_objects_get(by_selector=by_selector)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_find_objects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **by_selector** | **str**| the selector sets the resource name criteria for matching. A UI element will be considered a match if its resource name exactly matches the selector parameter and all other criteria for this selector are met. The format of the selector string is &#x60;sel@[$]value,...&#x60; Where &#x60;sel&#x60; can be one of - checkable - clazz - clickable - depth - desc - package - res - scrollable - text &#x60;@&#x60; replaces the &#x60;&#x3D;&#x60; sign that is used to separate parameters and values in the URL. If the first character of value is &#x60;$&#x60; then a &#x60;Pattern&#x60; is created. | [optional] 

### Return type

[**list[ObjectRef]**](ObjectRef.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_last_traversed_text_get**
> LastTraversedText ui_device_last_traversed_text_get()

Retrieves the text from the last UI traversal event received.

Retrieves the text from the last UI traversal event received.

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()

try:
    # Retrieves the text from the last UI traversal event received.
    api_response = api_instance.ui_device_last_traversed_text_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_last_traversed_text_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LastTraversedText**](LastTraversedText.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_press_back_get**
> StatusResponse ui_device_press_back_get()

Simulates a short press on the BACK button.

Simulates a short press on the BACK button.

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()

try:
    # Simulates a short press on the BACK button.
    api_response = api_instance.ui_device_press_back_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_press_back_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_press_delete_get**
> StatusResponse ui_device_press_delete_get()

Simulates a short press on the DELETE key.

Simulates a short press on the DELETE key.

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()

try:
    # Simulates a short press on the DELETE key.
    api_response = api_instance.ui_device_press_delete_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_press_delete_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_press_enter_get**
> StatusResponse ui_device_press_enter_get()

Simulates a short press on the ENTER key.

Simulates a short press on the ENTER key.

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()

try:
    # Simulates a short press on the ENTER key.
    api_response = api_instance.ui_device_press_enter_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_press_enter_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_press_home_get**
> StatusResponse ui_device_press_home_get()

Simulates a short press on the HOME button.

Simulates a short press on the HOME button.

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()

try:
    # Simulates a short press on the HOME button.
    api_response = api_instance.ui_device_press_home_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_press_home_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_press_key_code_get**
> StatusResponse ui_device_press_key_code_get(key_code, meta_state=meta_state)

Simulates a short press using a key code.

Simulates a short press using a key code.

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()
key_code = 56 # int | the key code of the event.
meta_state = 56 # int | an integer in which each bit set to 1 represents a pressed meta key (optional)

try:
    # Simulates a short press using a key code.
    api_response = api_instance.ui_device_press_key_code_get(key_code, meta_state=meta_state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_press_key_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_code** | **int**| the key code of the event. | 
 **meta_state** | **int**| an integer in which each bit set to 1 represents a pressed meta key | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_press_recent_apps_get**
> StatusResponse ui_device_press_recent_apps_get()

Simulates a short press on the Recent Apps button.

Simulates a short press on the Recent Apps button.

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()

try:
    # Simulates a short press on the Recent Apps button.
    api_response = api_instance.ui_device_press_recent_apps_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_press_recent_apps_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_product_name_get**
> ProductName ui_device_product_name_get()

Retrieves the product name of the device.

Retrieves the product name of the device.

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()

try:
    # Retrieves the product name of the device.
    api_response = api_instance.ui_device_product_name_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_product_name_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProductName**](ProductName.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_screenshot_get**
> str ui_device_screenshot_get(scale=scale, quality=quality)

Gets the device screenshot

Gets the device screenshot and can be influenced by the parameters. For example the `scale` of the screenshot or its `quality` can be specified. **NOTE**: [`UiDevice.takeScreenshot()`](https://developer.android.com/reference/android/support/test/uiautomator/UiDevice.html#takeScreenshot(java.io.File,%20float,%20int)) usually ignores these parameters so expect no change. 

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()
scale = 3.4 # float | The scale of the screenshot (i.e. 0.5) (optional)
quality = 56 # int | The quality of the screenshot (i.e. 100) (optional)

try:
    # Gets the device screenshot
    api_response = api_instance.ui_device_screenshot_get(scale=scale, quality=quality)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_screenshot_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scale** | **float**| The scale of the screenshot (i.e. 0.5) | [optional] 
 **quality** | **int**| The quality of the screenshot (i.e. 100) | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_swipe_get**
> StatusResponse ui_device_swipe_get(start_x, start_y, end_x, end_y, steps)

Performs a swipe.

Performs a swipe from one coordinate to another using the number of steps to determine smoothness and speed. Each step execution is throttled to 5ms per step. So for a 100 steps, the swipe will take about 1/2 second to complete.

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()
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
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_x** | **int**| from x | 
 **start_y** | **int**| from y | 
 **end_x** | **int**| to x | 
 **end_y** | **int**| end y | 
 **steps** | **int**| is the number of move steps sent to the system | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_swipe_post**
> StatusResponse ui_device_swipe_post(body)

Performs a swipe between points in the Point array.

Each step execution is throttled to 5ms per step. So for a 100 steps, the swipe will take about 1/2 second to complete

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()
body = culebratester_client.SwipeBody() # SwipeBody | 

try:
    # Performs a swipe between points in the Point array.
    api_response = api_instance.ui_device_swipe_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_swipe_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SwipeBody**](SwipeBody.md)|  | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_wait_for_idle_get**
> StatusResponse ui_device_wait_for_idle_get(timeout=timeout)

Waits for the current application to idle.

Waits for the current application to idle.

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()
timeout = 10000 # int | in milliseconds (optional) (default to 10000)

try:
    # Waits for the current application to idle.
    api_response = api_instance.ui_device_wait_for_idle_get(timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_wait_for_idle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| in milliseconds | [optional] [default to 10000]

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_device_wait_for_window_update_get**
> StatusResponse ui_device_wait_for_window_update_get(timeout, package_name=package_name)

Waits for a window content update event to occur.

If a package name for the window is specified, but the current window does not have the same package name, the function returns immediately.

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()
timeout = 789 # int | in milliseconds
package_name = 'package_name_example' # str | the specified window package name (can be null or not present). If null, a window update from any front-end window will end the wait (optional)

try:
    # Waits for a window content update event to occur.
    api_response = api_instance.ui_device_wait_for_window_update_get(timeout, package_name=package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_device_wait_for_window_update_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| in milliseconds | 
 **package_name** | **str**| the specified window package name (can be null or not present). If null, a window update from any front-end window will end the wait | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_object2_oid_click_get**
> StatusResponse ui_object2_oid_click_get(oid)

Clicks on the specified object.

The target object should have been found using `findObject` with a `selector`.

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()
oid = 56 # int | The object ID

try:
    # Clicks on the specified object.
    api_response = api_instance.ui_object2_oid_click_get(oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_object2_oid_click_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **int**| The object ID | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_object2_oid_dump_get**
> Selector ui_object2_oid_dump_get(oid)

Dumps the specified object.

The target object should have been found using `findObject` with a `selector`.

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()
oid = 56 # int | The object ID

try:
    # Dumps the specified object.
    api_response = api_instance.ui_object2_oid_dump_get(oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_object2_oid_dump_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **int**| The object ID | 

### Return type

[**Selector**](Selector.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_object2_oid_get_text_get**
> Text ui_object2_oid_get_text_get(oid)

Gets the text content.

The target object should have been found using `findObject` with a `selector`.

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()
oid = 56 # int | The object ID

try:
    # Gets the text content.
    api_response = api_instance.ui_object2_oid_get_text_get(oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_object2_oid_get_text_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **int**| The object ID | 

### Return type

[**Text**](Text.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_object2_oid_long_click_get**
> StatusResponse ui_object2_oid_long_click_get(oid)

Long-clicks on the specified object.

The target object should have been found using `findObject` with a `selector`.

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()
oid = 56 # int | The object ID

try:
    # Long-clicks on the specified object.
    api_response = api_instance.ui_object2_oid_long_click_get(oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_object2_oid_long_click_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **int**| The object ID | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ui_object2_oid_set_text_post**
> StatusResponse ui_object2_oid_set_text_post(body, oid)

Sets the text content if this object is an editable field.

The target object should have been found using `findObject` with a `selector`.

### Example
```python
from __future__ import print_function
import time
import culebratester_client
from culebratester_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = culebratester_client.DefaultApi()
body = culebratester_client.OidSetTextBody() # OidSetTextBody | Text to enter in the field
oid = 56 # int | The object ID

try:
    # Sets the text content if this object is an editable field.
    api_response = api_instance.ui_object2_oid_set_text_post(body, oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ui_object2_oid_set_text_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OidSetTextBody**](OidSetTextBody.md)| Text to enter in the field | 
 **oid** | **int**| The object ID | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

