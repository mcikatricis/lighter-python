# Account


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | 
**message** | **str** |  | [optional] 
**account_type** | **int** |  | 
**index** | **int** |  | 
**l1_address** | **str** |  | 
**cancel_all_time** | **int** |  | 
**total_order_count** | **int** |  | 
**total_isolated_order_count** | **int** |  | 
**pending_order_count** | **int** |  | 
**available_balance** | **str** |  | 
**status** | **int** |  | 
**collateral** | **str** |  | 

## Example

```python
from lighter.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


