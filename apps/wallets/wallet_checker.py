from dataclasses import dataclass
from typing import List, Optional

import requests
from django.conf import settings

from .utils import format_amount, is_spam_token


@dataclass
class Token:
    """
    Represents a cryptocurrency token with its balance and value information

    Attributes:
        name (str): Full name of the token(e.g., "Ethereum")
        symbol (str): The symbol of the token(e.g., "ETH")
        balance (str): Formatted token balance for display
        usd_value (str): Formatted UDS value for display
        raw_usd_value (float): Raw UDS value for calculations
    """
    name: str
    symbol: str
    balance: str
    usd_value: str
    raw_usd_value: float

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
            raw_usd_value=usd_value,
        )

    @classmethod
    def from_token_data(cls, data: dict) -> "Token":
        """Create a token from API response token data."""
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
            raw_usd_value=usd_value,
        )


class WalletChecker:
    """Handles wallet data fetching and parsing from Ethplorer API."""

    def __init__(self, address: str):
        self.base_url = settings.ETH_BASE_URL
        self.api_key = settings.API_KEY
        self.address = address

    def get_wallet_data(self) -> Optional[dict]:
        """
        Fetch and parse wallet data from Ethplorer API

        Returns:
            dict | None: Dictionary containing:
                - 'tokens' (List[Token]): List of tokens in the wallet
                - 'total_balance' (str): Total portfolio value in USD (formatted)
            Returns None if API request fails or wallet data cannot be retrieved
        """

        try:
            response = requests.get(
                f"{self.base_url}getAddressInfo/{self.address}/",
                params={"apiKey": self.api_key},
                timeout=10,
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(e)
            return None
        else:
            tokens, total_usd_balance = self._parse_wallet_data(response.json())

        return {
            "tokens": tokens,
            "total_balance": total_usd_balance,
        }

    def _parse_wallet_data(self, json_data: dict) -> tuple[List[Token], str]:
        """Parse Ethplorer API response into Token objects and calculate total balance."""
        tokens = []
        total_usd_balance = 0
        eth_token = Token.from_eth_data(json_data["ETH"])

        tokens.append(eth_token)
        total_usd_balance += eth_token.raw_usd_value

        if json_data.get("tokens"):
            for token_data in json_data["tokens"]:
                if not is_spam_token(token_data):
                    try:
                        token = Token.from_token_data(token_data)
                        tokens.append(token)
                    except (KeyError, ValueError, ZeroDivisionError) as e:
                        print(e)
                        continue
                    else:
                        total_usd_balance += token.raw_usd_value

        return tokens, format_amount(total_usd_balance)
