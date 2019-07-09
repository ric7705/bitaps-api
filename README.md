# bitaps-api

Payment forwarding API

## Example

```python
from bitaps_api import BitApsForwarding

api = BitApsForwarding(testnet=True)

# get forwarding address
res = api.generate_address()

# get address_state by access_token
res = api.generate_address(access_token='your token')

# get address_state by payment_code
res = api.generate_address(payment_code='your payment code')

```