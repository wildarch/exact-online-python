# swagger_client.DefaultApi

All URIs are relative to *https://start.exactonline.nl/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**division_documents_document_attachments_get**](DefaultApi.md#division_documents_document_attachments_get) | **GET** /{division}/documents/DocumentAttachments | 
[**division_documents_documents_get**](DefaultApi.md#division_documents_documents_get) | **GET** /{division}/documents/Documents | 
[**division_logistics_item_groups_get**](DefaultApi.md#division_logistics_item_groups_get) | **GET** /{division}/logistics/ItemGroups | 
[**division_logistics_items_get**](DefaultApi.md#division_logistics_items_get) | **GET** /{division}/logistics/Items | Gets a list of items
[**division_logistics_items_guiditem_id_delete**](DefaultApi.md#division_logistics_items_guiditem_id_delete) | **DELETE** /{division}/logistics/Items(guid{item_id}) | Delete an item from the database
[**division_logistics_items_guiditem_id_put**](DefaultApi.md#division_logistics_items_guiditem_id_put) | **PUT** /{division}/logistics/Items(guid{item_id}) | Update an item in the database
[**division_logistics_items_post**](DefaultApi.md#division_logistics_items_post) | **POST** /{division}/logistics/Items | Add a new item to the database
[**division_logistics_sales_item_prices_get**](DefaultApi.md#division_logistics_sales_item_prices_get) | **GET** /{division}/logistics/SalesItemPrices | 
[**division_manufacturing_shop_order_routing_step_plans_get**](DefaultApi.md#division_manufacturing_shop_order_routing_step_plans_get) | **GET** /{division}/manufacturing/ShopOrderRoutingStepPlans | 
[**division_manufacturing_shop_orders_get**](DefaultApi.md#division_manufacturing_shop_orders_get) | **GET** /{division}/manufacturing/ShopOrders | 
[**division_manufacturing_time_transactions_get**](DefaultApi.md#division_manufacturing_time_transactions_get) | **GET** /{division}/manufacturing/TimeTransactions | 
[**division_manufacturing_time_transactions_guidid_delete**](DefaultApi.md#division_manufacturing_time_transactions_guidid_delete) | **DELETE** /{division}/manufacturing/TimeTransactions(guid{id}) | Delete a TimeTransaction from the database
[**division_manufacturing_time_transactions_guidid_put**](DefaultApi.md#division_manufacturing_time_transactions_guidid_put) | **PUT** /{division}/manufacturing/TimeTransactions(guid{id}) | Update a TimeTransaction in the database
[**division_manufacturing_time_transactions_post**](DefaultApi.md#division_manufacturing_time_transactions_post) | **POST** /{division}/manufacturing/TimeTransactions | Add a new TimeTransaction to the database
[**division_payroll_employees_get**](DefaultApi.md#division_payroll_employees_get) | **GET** /{division}/payroll/Employees | 
[**division_payroll_employment_contracts_get**](DefaultApi.md#division_payroll_employment_contracts_get) | **GET** /{division}/payroll/EmploymentContracts | 
[**division_project_projects_get**](DefaultApi.md#division_project_projects_get) | **GET** /{division}/project/Projects | 
[**get_me**](DefaultApi.md#get_me) | **GET** /current/Me | Get the current user&#39;s account information


# **division_documents_document_attachments_get**
> InlineResponse2001 division_documents_document_attachments_get(division, access_token, filter=filter, select=select, expand=expand, skiptoken=skiptoken, orderby=orderby)



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
division = 'division_example' # str | The division to query
access_token = 'access_token_example' # str | Access token to the authenticate the request
filter = 'filter_example' # str | Filter options for the returned results (optional)
select = 'select_example' # str | Restrict the returned properties to the given set (\"prop1,prop2,...\") (optional)
expand = 'expand_example' # str | Expand a given property from an ID to the actual endpoint data (optional)
skiptoken = 'skiptoken_example' # str | Skiptoken GUID (optional)
orderby = 'orderby_example' # str | Order the returned items by the given property (optional)

try: 
    api_response = api_instance.division_documents_document_attachments_get(division, access_token, filter=filter, select=select, expand=expand, skiptoken=skiptoken, orderby=orderby)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->division_documents_document_attachments_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **division** | **str**| The division to query | 
 **access_token** | **str**| Access token to the authenticate the request | 
 **filter** | **str**| Filter options for the returned results | [optional] 
 **select** | **str**| Restrict the returned properties to the given set (\&quot;prop1,prop2,...\&quot;) | [optional] 
 **expand** | **str**| Expand a given property from an ID to the actual endpoint data | [optional] 
 **skiptoken** | **str**| Skiptoken GUID | [optional] 
 **orderby** | **str**| Order the returned items by the given property | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **division_documents_documents_get**
> InlineResponse2002 division_documents_documents_get(division, access_token, filter=filter, select=select, expand=expand, skiptoken=skiptoken, orderby=orderby)



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
division = 'division_example' # str | The division to query
access_token = 'access_token_example' # str | Access token to the authenticate the request
filter = 'filter_example' # str | Filter options for the returned results (optional)
select = 'select_example' # str | Restrict the returned properties to the given set (\"prop1,prop2,...\") (optional)
expand = 'expand_example' # str | Expand a given property from an ID to the actual endpoint data (optional)
skiptoken = 'skiptoken_example' # str | Skiptoken GUID (optional)
orderby = 'orderby_example' # str | Order the returned items by the given property (optional)

try: 
    api_response = api_instance.division_documents_documents_get(division, access_token, filter=filter, select=select, expand=expand, skiptoken=skiptoken, orderby=orderby)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->division_documents_documents_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **division** | **str**| The division to query | 
 **access_token** | **str**| Access token to the authenticate the request | 
 **filter** | **str**| Filter options for the returned results | [optional] 
 **select** | **str**| Restrict the returned properties to the given set (\&quot;prop1,prop2,...\&quot;) | [optional] 
 **expand** | **str**| Expand a given property from an ID to the actual endpoint data | [optional] 
 **skiptoken** | **str**| Skiptoken GUID | [optional] 
 **orderby** | **str**| Order the returned items by the given property | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **division_logistics_item_groups_get**
> InlineResponse2003 division_logistics_item_groups_get(division, access_token, filter=filter, select=select, expand=expand)



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
division = 'division_example' # str | The division to query
access_token = 'access_token_example' # str | Access token to the authenticate the request
filter = 'filter_example' # str | Filter options for the returned results (optional)
select = 'select_example' # str | Restrict the returned properties to the given set (\"prop1,prop2,...\") (optional)
expand = 'expand_example' # str | Expand a given property from an ID to the actual endpoint data (optional)

try: 
    api_response = api_instance.division_logistics_item_groups_get(division, access_token, filter=filter, select=select, expand=expand)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->division_logistics_item_groups_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **division** | **str**| The division to query | 
 **access_token** | **str**| Access token to the authenticate the request | 
 **filter** | **str**| Filter options for the returned results | [optional] 
 **select** | **str**| Restrict the returned properties to the given set (\&quot;prop1,prop2,...\&quot;) | [optional] 
 **expand** | **str**| Expand a given property from an ID to the actual endpoint data | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **division_logistics_items_get**
> InlineResponse2004 division_logistics_items_get(division, access_token, filter=filter, select=select, expand=expand, skiptoken=skiptoken, orderby=orderby)

Gets a list of items

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
division = 'division_example' # str | The division to query
access_token = 'access_token_example' # str | Access token to the authenticate the request
filter = 'filter_example' # str | Filter options for the returned results (optional)
select = 'select_example' # str | Restrict the returned properties to the given set (\"prop1,prop2,...\") (optional)
expand = 'expand_example' # str | Expand a given property from an ID to the actual endpoint data (optional)
skiptoken = 'skiptoken_example' # str | Skiptoken GUID (optional)
orderby = 'orderby_example' # str | Order the returned items by the given property (optional)

try: 
    # Gets a list of items
    api_response = api_instance.division_logistics_items_get(division, access_token, filter=filter, select=select, expand=expand, skiptoken=skiptoken, orderby=orderby)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->division_logistics_items_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **division** | **str**| The division to query | 
 **access_token** | **str**| Access token to the authenticate the request | 
 **filter** | **str**| Filter options for the returned results | [optional] 
 **select** | **str**| Restrict the returned properties to the given set (\&quot;prop1,prop2,...\&quot;) | [optional] 
 **expand** | **str**| Expand a given property from an ID to the actual endpoint data | [optional] 
 **skiptoken** | **str**| Skiptoken GUID | [optional] 
 **orderby** | **str**| Order the returned items by the given property | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **division_logistics_items_guiditem_id_delete**
> division_logistics_items_guiditem_id_delete(division, item_id, access_token)

Delete an item from the database

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
division = 'division_example' # str | The division to query
item_id = 'item_id_example' # str | ID of Item to delete
access_token = 'access_token_example' # str | Access token to the authenticate the request

try: 
    # Delete an item from the database
    api_instance.division_logistics_items_guiditem_id_delete(division, item_id, access_token)
except ApiException as e:
    print "Exception when calling DefaultApi->division_logistics_items_guiditem_id_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **division** | **str**| The division to query | 
 **item_id** | **str**| ID of Item to delete | 
 **access_token** | **str**| Access token to the authenticate the request | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **division_logistics_items_guiditem_id_put**
> division_logistics_items_guiditem_id_put(division, item_id, access_token, item)

Update an item in the database

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
division = 'division_example' # str | The division to query
item_id = 'item_id_example' # str | ID of Item to update
access_token = 'access_token_example' # str | Access token to the authenticate the request
item = swagger_client.Item() # Item | 

try: 
    # Update an item in the database
    api_instance.division_logistics_items_guiditem_id_put(division, item_id, access_token, item)
except ApiException as e:
    print "Exception when calling DefaultApi->division_logistics_items_guiditem_id_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **division** | **str**| The division to query | 
 **item_id** | **str**| ID of Item to update | 
 **access_token** | **str**| Access token to the authenticate the request | 
 **item** | [**Item**](Item.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **division_logistics_items_post**
> division_logistics_items_post(division, access_token, item)

Add a new item to the database

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
division = 'division_example' # str | The division to query
access_token = 'access_token_example' # str | Access token to the authenticate the request
item = swagger_client.Item() # Item | 

try: 
    # Add a new item to the database
    api_instance.division_logistics_items_post(division, access_token, item)
except ApiException as e:
    print "Exception when calling DefaultApi->division_logistics_items_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **division** | **str**| The division to query | 
 **access_token** | **str**| Access token to the authenticate the request | 
 **item** | [**Item**](Item.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **division_logistics_sales_item_prices_get**
> InlineResponse2005 division_logistics_sales_item_prices_get(division, access_token, filter=filter, select=select, expand=expand, top=top)



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
division = 'division_example' # str | The division to query
access_token = 'access_token_example' # str | Access token to the authenticate the request
filter = 'filter_example' # str | Filter options for the returned results (optional)
select = 'select_example' # str | Restrict the returned properties to the given set (\"prop1,prop2,...\") (optional)
expand = 'expand_example' # str | Expand a given property from an ID to the actual endpoint data (optional)
top = 56 # int | Restrict the number of returned results to the specified amount (optional)

try: 
    api_response = api_instance.division_logistics_sales_item_prices_get(division, access_token, filter=filter, select=select, expand=expand, top=top)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->division_logistics_sales_item_prices_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **division** | **str**| The division to query | 
 **access_token** | **str**| Access token to the authenticate the request | 
 **filter** | **str**| Filter options for the returned results | [optional] 
 **select** | **str**| Restrict the returned properties to the given set (\&quot;prop1,prop2,...\&quot;) | [optional] 
 **expand** | **str**| Expand a given property from an ID to the actual endpoint data | [optional] 
 **top** | **int**| Restrict the number of returned results to the specified amount | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **division_manufacturing_shop_order_routing_step_plans_get**
> InlineResponse2006 division_manufacturing_shop_order_routing_step_plans_get(division, access_token, filter=filter, select=select, expand=expand, skiptoken=skiptoken, orderby=orderby)



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
division = 'division_example' # str | The division to query
access_token = 'access_token_example' # str | Access token to the authenticate the request
filter = 'filter_example' # str | Filter options for the returned results (optional)
select = 'select_example' # str | Restrict the returned properties to the given set (\"prop1,prop2,...\") (optional)
expand = 'expand_example' # str | Expand a given property from an ID to the actual endpoint data (optional)
skiptoken = 'skiptoken_example' # str | Skiptoken GUID (optional)
orderby = 'orderby_example' # str | Order the returned items by the given property (optional)

try: 
    api_response = api_instance.division_manufacturing_shop_order_routing_step_plans_get(division, access_token, filter=filter, select=select, expand=expand, skiptoken=skiptoken, orderby=orderby)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->division_manufacturing_shop_order_routing_step_plans_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **division** | **str**| The division to query | 
 **access_token** | **str**| Access token to the authenticate the request | 
 **filter** | **str**| Filter options for the returned results | [optional] 
 **select** | **str**| Restrict the returned properties to the given set (\&quot;prop1,prop2,...\&quot;) | [optional] 
 **expand** | **str**| Expand a given property from an ID to the actual endpoint data | [optional] 
 **skiptoken** | **str**| Skiptoken GUID | [optional] 
 **orderby** | **str**| Order the returned items by the given property | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **division_manufacturing_shop_orders_get**
> InlineResponse2007 division_manufacturing_shop_orders_get(division, access_token, filter=filter, select=select, expand=expand, skiptoken=skiptoken, orderby=orderby)



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
division = 'division_example' # str | The division to query
access_token = 'access_token_example' # str | Access token to the authenticate the request
filter = 'filter_example' # str | Filter options for the returned results (optional)
select = 'select_example' # str | Restrict the returned properties to the given set (\"prop1,prop2,...\") (optional)
expand = 'expand_example' # str | Expand a given property from an ID to the actual endpoint data (optional)
skiptoken = 'skiptoken_example' # str | Skiptoken GUID (optional)
orderby = 'orderby_example' # str | Order the returned items by the given property (optional)

try: 
    api_response = api_instance.division_manufacturing_shop_orders_get(division, access_token, filter=filter, select=select, expand=expand, skiptoken=skiptoken, orderby=orderby)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->division_manufacturing_shop_orders_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **division** | **str**| The division to query | 
 **access_token** | **str**| Access token to the authenticate the request | 
 **filter** | **str**| Filter options for the returned results | [optional] 
 **select** | **str**| Restrict the returned properties to the given set (\&quot;prop1,prop2,...\&quot;) | [optional] 
 **expand** | **str**| Expand a given property from an ID to the actual endpoint data | [optional] 
 **skiptoken** | **str**| Skiptoken GUID | [optional] 
 **orderby** | **str**| Order the returned items by the given property | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **division_manufacturing_time_transactions_get**
> InlineResponse2008 division_manufacturing_time_transactions_get(division, access_token, filter=filter, select=select, expand=expand, skiptoken=skiptoken, orderby=orderby)



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
division = 'division_example' # str | The division to query
access_token = 'access_token_example' # str | Access token to the authenticate the request
filter = 'filter_example' # str | Filter options for the returned results (optional)
select = 'select_example' # str | Restrict the returned properties to the given set (\"prop1,prop2,...\") (optional)
expand = 'expand_example' # str | Expand a given property from an ID to the actual endpoint data (optional)
skiptoken = 'skiptoken_example' # str | Skiptoken GUID (optional)
orderby = 'orderby_example' # str | Order the returned items by the given property (optional)

try: 
    api_response = api_instance.division_manufacturing_time_transactions_get(division, access_token, filter=filter, select=select, expand=expand, skiptoken=skiptoken, orderby=orderby)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->division_manufacturing_time_transactions_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **division** | **str**| The division to query | 
 **access_token** | **str**| Access token to the authenticate the request | 
 **filter** | **str**| Filter options for the returned results | [optional] 
 **select** | **str**| Restrict the returned properties to the given set (\&quot;prop1,prop2,...\&quot;) | [optional] 
 **expand** | **str**| Expand a given property from an ID to the actual endpoint data | [optional] 
 **skiptoken** | **str**| Skiptoken GUID | [optional] 
 **orderby** | **str**| Order the returned items by the given property | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **division_manufacturing_time_transactions_guidid_delete**
> division_manufacturing_time_transactions_guidid_delete(division, id, access_token)

Delete a TimeTransaction from the database

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
division = 'division_example' # str | The division to query
id = 'id_example' # str | ID of TimeTransaction to delete
access_token = 'access_token_example' # str | Access token to the authenticate the request

try: 
    # Delete a TimeTransaction from the database
    api_instance.division_manufacturing_time_transactions_guidid_delete(division, id, access_token)
except ApiException as e:
    print "Exception when calling DefaultApi->division_manufacturing_time_transactions_guidid_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **division** | **str**| The division to query | 
 **id** | **str**| ID of TimeTransaction to delete | 
 **access_token** | **str**| Access token to the authenticate the request | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **division_manufacturing_time_transactions_guidid_put**
> division_manufacturing_time_transactions_guidid_put(division, id, access_token, item)

Update a TimeTransaction in the database

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
division = 'division_example' # str | The division to query
id = 'id_example' # str | ID of TimeTransaction to update
access_token = 'access_token_example' # str | Access token to the authenticate the request
item = swagger_client.TimeTransaction() # TimeTransaction | 

try: 
    # Update a TimeTransaction in the database
    api_instance.division_manufacturing_time_transactions_guidid_put(division, id, access_token, item)
except ApiException as e:
    print "Exception when calling DefaultApi->division_manufacturing_time_transactions_guidid_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **division** | **str**| The division to query | 
 **id** | **str**| ID of TimeTransaction to update | 
 **access_token** | **str**| Access token to the authenticate the request | 
 **item** | [**TimeTransaction**](TimeTransaction.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **division_manufacturing_time_transactions_post**
> division_manufacturing_time_transactions_post(division, access_token, item)

Add a new TimeTransaction to the database

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
division = 'division_example' # str | The division to query
access_token = 'access_token_example' # str | Access token to the authenticate the request
item = swagger_client.TimeTransaction() # TimeTransaction | 

try: 
    # Add a new TimeTransaction to the database
    api_instance.division_manufacturing_time_transactions_post(division, access_token, item)
except ApiException as e:
    print "Exception when calling DefaultApi->division_manufacturing_time_transactions_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **division** | **str**| The division to query | 
 **access_token** | **str**| Access token to the authenticate the request | 
 **item** | [**TimeTransaction**](TimeTransaction.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **division_payroll_employees_get**
> InlineResponse2009 division_payroll_employees_get(division, access_token, filter=filter, select=select, expand=expand, skiptoken=skiptoken, orderby=orderby)



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
division = 'division_example' # str | The division to query
access_token = 'access_token_example' # str | Access token to the authenticate the request
filter = 'filter_example' # str | Filter options for the returned results (optional)
select = 'select_example' # str | Restrict the returned properties to the given set (\"prop1,prop2,...\") (optional)
expand = 'expand_example' # str | Expand a given property from an ID to the actual endpoint data (optional)
skiptoken = 'skiptoken_example' # str | Skiptoken GUID (optional)
orderby = 'orderby_example' # str | Order the returned items by the given property (optional)

try: 
    api_response = api_instance.division_payroll_employees_get(division, access_token, filter=filter, select=select, expand=expand, skiptoken=skiptoken, orderby=orderby)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->division_payroll_employees_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **division** | **str**| The division to query | 
 **access_token** | **str**| Access token to the authenticate the request | 
 **filter** | **str**| Filter options for the returned results | [optional] 
 **select** | **str**| Restrict the returned properties to the given set (\&quot;prop1,prop2,...\&quot;) | [optional] 
 **expand** | **str**| Expand a given property from an ID to the actual endpoint data | [optional] 
 **skiptoken** | **str**| Skiptoken GUID | [optional] 
 **orderby** | **str**| Order the returned items by the given property | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **division_payroll_employment_contracts_get**
> InlineResponse20010 division_payroll_employment_contracts_get(division, access_token, filter=filter, select=select, expand=expand, skiptoken=skiptoken, orderby=orderby)



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
division = 'division_example' # str | The division to query
access_token = 'access_token_example' # str | Access token to the authenticate the request
filter = 'filter_example' # str | Filter options for the returned results (optional)
select = 'select_example' # str | Restrict the returned properties to the given set (\"prop1,prop2,...\") (optional)
expand = 'expand_example' # str | Expand a given property from an ID to the actual endpoint data (optional)
skiptoken = 'skiptoken_example' # str | Skiptoken GUID (optional)
orderby = 'orderby_example' # str | Order the returned items by the given property (optional)

try: 
    api_response = api_instance.division_payroll_employment_contracts_get(division, access_token, filter=filter, select=select, expand=expand, skiptoken=skiptoken, orderby=orderby)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->division_payroll_employment_contracts_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **division** | **str**| The division to query | 
 **access_token** | **str**| Access token to the authenticate the request | 
 **filter** | **str**| Filter options for the returned results | [optional] 
 **select** | **str**| Restrict the returned properties to the given set (\&quot;prop1,prop2,...\&quot;) | [optional] 
 **expand** | **str**| Expand a given property from an ID to the actual endpoint data | [optional] 
 **skiptoken** | **str**| Skiptoken GUID | [optional] 
 **orderby** | **str**| Order the returned items by the given property | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **division_project_projects_get**
> InlineResponse20011 division_project_projects_get(division, access_token, filter=filter, select=select, expand=expand, skiptoken=skiptoken, orderby=orderby)



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
division = 'division_example' # str | The division to query
access_token = 'access_token_example' # str | Access token to the authenticate the request
filter = 'filter_example' # str | Filter options for the returned results (optional)
select = 'select_example' # str | Restrict the returned properties to the given set (\"prop1,prop2,...\") (optional)
expand = 'expand_example' # str | Expand a given property from an ID to the actual endpoint data (optional)
skiptoken = 'skiptoken_example' # str | Skiptoken GUID (optional)
orderby = 'orderby_example' # str | Order the returned items by the given property (optional)

try: 
    api_response = api_instance.division_project_projects_get(division, access_token, filter=filter, select=select, expand=expand, skiptoken=skiptoken, orderby=orderby)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->division_project_projects_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **division** | **str**| The division to query | 
 **access_token** | **str**| Access token to the authenticate the request | 
 **filter** | **str**| Filter options for the returned results | [optional] 
 **select** | **str**| Restrict the returned properties to the given set (\&quot;prop1,prop2,...\&quot;) | [optional] 
 **expand** | **str**| Expand a given property from an ID to the actual endpoint data | [optional] 
 **skiptoken** | **str**| Skiptoken GUID | [optional] 
 **orderby** | **str**| Order the returned items by the given property | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_me**
> InlineResponse200 get_me(access_token)

Get the current user's account information

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
access_token = 'access_token_example' # str | Access token to the authenticate the request

try: 
    # Get the current user's account information
    api_response = api_instance.get_me(access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_me: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access token to the authenticate the request | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

