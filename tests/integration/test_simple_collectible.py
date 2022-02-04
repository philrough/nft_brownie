from scripts.utils import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
from brownie import network, SimpleCollectible
from scripts.simple_collectible.deploy_and_create import deploy_and_create 
import pytest


def test_can_create_simple_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    
    # Arrange
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
    
    # Act
    tx = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    tx.wait(1)

    # Assert
    assert tx is not None