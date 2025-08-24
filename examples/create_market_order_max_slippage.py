import asyncio
import logging
import lighter

logging.basicConfig(level=logging.DEBUG)

# The API_KEY_PRIVATE_KEY provided belongs to a dummy account registered on Testnet.
# It was generated using the setup_system.py script, and serves as an example.
BASE_URL = "https://testnet.zklighter.elliot.ai"
API_KEY_PRIVATE_KEY = "0x321ec32c490960eb83df619e2701b5948e32da808fc0b6fd99550ce92af130f1c4088a37a0793972"
ACCOUNT_INDEX = 46
API_KEY_INDEX = 2


def trim_exception(e: Exception) -> str:
    return str(e).strip().split("\n")[-1]


async def main():
    client = lighter.SignerClient(
        url=BASE_URL,
        private_key=API_KEY_PRIVATE_KEY,
        account_index=ACCOUNT_INDEX,
        api_key_index=API_KEY_INDEX,
    )

    # tx = await client.create_market_order_limited_slippage(market_index=0, client_order_index=0, base_amount=30000000,
    #                                                        max_slippage=0.001, is_ask=True)
    tx = await client.create_market_order_if_slippage(market_index=0, client_order_index=0, base_amount=30000000,
                                                           max_slippage=0.01, is_ask=True)
    print("Create Order Tx:", tx)
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
