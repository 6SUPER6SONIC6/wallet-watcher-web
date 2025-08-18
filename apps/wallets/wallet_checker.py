from dataclasses import dataclass
from typing import List, Optional

import requests
from django.conf import settings

from .utils import format_amount, is_spam_token


@dataclass
class Token:
    """Represents a cryptocurrency token with its balance and value information."""
    name: str
    symbol: str
    balance: str
    usd_value: str

    @classmethod
    def from_eth_data(cls, data: dict) -> "Token":
        """Create ETH token from API response data."""
        balance = data["balance"]
        rate = data["price"]["rate"]
        usd_value = balance * rate

        return cls(
            name="Ethereum",
            symbol="ETH",
            balance=format_amount(balance),
            usd_value=format_amount(usd_value),
        )

    @classmethod
    def from_token_data(cls, data: dict) -> "Token":
        """Create token from API response token data."""
        token_info = data["tokenInfo"]
        raw_balance = int(data['rawBalance'])
        decimals = int(token_info['decimals'])
        balance = raw_balance / (10 ** decimals)
        price = token_info['price']
        rate = float(price['rate'])
        usd_value = balance * rate

        return cls(
            name=token_info["name"],
            symbol=token_info["symbol"],
            balance=format_amount(balance),
            usd_value=format_amount(usd_value),
        )


class WalletChecker:
    """Handles wallet data fetching and parsing from Ethplorer API."""

    def __init__(self):
        self.base_url = settings.ETH_BASE_URL
        self.api_key = settings.API_KEY

    def get_wallet_data(self, address: str) -> Optional[List[Token]]:
        """
        Fetch wallet data.

        Args:
            address (str): Address to fetch data for.

        Returns:
            List[Token]: List of Tokens parsed from API response or None if error occurred.
        """

        try:
            response = requests.get(
                f"{self.base_url}getAddressInfo/{address}/",
                params={"apiKey": self.api_key},
                timeout=10,
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(e)
            return None

        return self._parse_wallet_data(response.json())

    def _parse_wallet_data(self, json_data: dict) -> List[Token]:
        """Parse JSON response into a list of Tokens."""
        tokens = []
        eth_token = json_data["ETH"]

        tokens.append(Token.from_eth_data(eth_token))

        if json_data.get("tokens"):
            for token_data in json_data["tokens"]:
                if not is_spam_token(token_data):
                    try:
                        tokens.append(Token.from_token_data(token_data))
                    except (KeyError, ValueError, ZeroDivisionError) as e:
                        print(e)
                        continue

        return tokens
