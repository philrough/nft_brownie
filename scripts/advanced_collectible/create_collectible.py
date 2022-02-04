from brownie import AdvancedCollectible
from scripts.utils import fund_with_link, get_account, OPENSEA_URL
from web3 import Web3


def main():
    account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    fund_with_link(advanced_collectible.address, amount=Web3.toWei(0.1, "ether"))
    creation_transaction = advanced_collectible.createCollectible({"from": account})
    creation_transaction.wait(1)
    print("Collectible created!")
    print(
        f"Awesome, you can view your NFT at {OPENSEA_URL.format(advanced_collectible.address, advanced_collectible.tokenCounter() - 1)}"
    )