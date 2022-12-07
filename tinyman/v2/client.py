from algosdk.v2client.algod import AlgodClient
from tinyman.client import BaseTinymanClient
from tinyman.staking.constants import (
    TESTNET_STAKING_APP_ID,
    MAINNET_STAKING_APP_ID,
)

from tinyman.v2.constants import (
    TESTNET_VALIDATOR_APP_ID,
    MAINNET_VALIDATOR_APP_ID,
)


class TinymanV2Client(BaseTinymanClient):
    def fetch_pool(self, asset_a, asset_b, fetch=True):
        from .pools import Pool

        return Pool(self, asset_a, asset_a, fetch=fetch)


class TinymanV2TestnetClient(TinymanV2Client):
    def __init__(self, algod_client: AlgodClient, user_address=None):
        super().__init__(
            algod_client,
            validator_app_id=TESTNET_VALIDATOR_APP_ID,
            api_base_url="https://testnet.analytics.tinyman.org/api/",
            user_address=user_address,
            staking_app_id=TESTNET_STAKING_APP_ID,
        )


class TinymanV2MainnetClient(TinymanV2Client):
    def __init__(self, algod_client: AlgodClient, user_address=None):
        super().__init__(
            algod_client,
            validator_app_id=MAINNET_VALIDATOR_APP_ID,
            api_base_url="https://mainnet.analytics.tinyman.org/api/",
            user_address=user_address,
            staking_app_id=MAINNET_STAKING_APP_ID,
        )
