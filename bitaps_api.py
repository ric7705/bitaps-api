import requests


class BitApsForwarding:

    def __init__(self, testnet=True):
        test = testnet
        currency = 'eth'

        self.base_url = f"https://api.bitaps.com/{currency}{'' if not test else '/testnet'}/v1"

    def generate_address(self, payload):
        path = '/create/payment/address'

        return requests.post(url=self.base_url + path, json=payload)

    def get_header(self, token_only=False, **auth_type):
        headers = {}

        if 'Access-Token' in auth_type:
            headers['Access-Token'] = auth_type['Access-Token']
        elif 'Payment-Code' in auth_type:
            headers['Payment-Code'] = auth_type['Payment-Code']

        if token_only and 'Access-Token' not in headers:
            raise Exception('Access-Token is required')

        if not headers:
            raise Exception('auth_type is required')

        return headers

    def address_state(self, address, **auth_type):
        '''
        Payment address state
        '''

        path = f'/payment/address/state/{address}'

        headers = self.get_header(**auth_type)

        return requests.get(url=self.base_url+path, headers=headers)

    def address_transactions(self, address, **auth_type):
        '''
        List of payment address transactions
        '''
        path = f'/payment/address/transactions/{address}'

        headers = self.get_header(**auth_type)

        return requests.get(url=self.base_url + path, headers=headers)

    def callback_log(self, address, **auth_type):
        '''
        Callback log for payment address
        '''
        path = f'/payment/address/callback/log/{address}'

        headers = self.get_header(**auth_type)

        return requests.get(url=self.base_url + path, headers=headers)

    # to access the following API, the token is required

    def daily_stat(self, start, to, limit, page, domain_hash, **auth_type):
        '''
        Daily domain statistics
        '''

        payload = {
            "from": start,
            "to": to,
            "limit": limit,
            "page": page
        }
        path = f'/domain/daily/statistic/{domain_hash}'

        headers = self.get_header(token_only=True, **auth_type)

        return requests.get(url=self.base_url + path, headers=headers, params=payload)

    def transactions_list(self, start, to, limit, page, type, domain_hash, **auth_type):
        '''
        A request header Access-Token is required
        '''

        payload = {
            "from": start,
            "to": to,
            "limit": limit,
            "page": page,
            "type": type
        }

        path = f'/domain/transactions/{domain_hash}'

        headers = self.get_header(token_only=True, **auth_type)

        return requests.get(url=self.base_url + path, headers=headers, params=payload)

    def created_addresses_list(self, start, to, limit, page, domain_hash, **auth_type):
        '''
        List of created addresses
        '''
        payload = {
            "from": start,
            "to": to,
            "limit": limit,
            "page": page,
        }

        path = f'/domain/addresses/{domain_hash}'

        headers = self.get_header(token_only=True, **auth_type)

        return requests.get(url=self.base_url + path, headers=headers, params=payload)

    def domain_statistics(self, domain_hash, **auth_type):
        '''
        Domain statistics
        '''
        path = f'/domain/addresses/{domain_hash}'

        headers = self.get_header(token_only=True, **auth_type)

        return requests.get(url=self.base_url + path, headers=headers)

    def create_access_token(self, callback_link):
        '''
        Create domain access token
        '''
        path = '/create/domain/access/token'
        payload = {
            "callback_link": callback_link
        }

        return requests.post(url=self.base_url + path, json=payload)

    def create_authorization_code(self, callback_link):
        '''
        Create domain authorization code
        '''
        path = '/create/domain/authorization/code'
        payload = {
            "callback_link": callback_link
        }

        return requests.post(url=self.base_url + path, json=payload)
