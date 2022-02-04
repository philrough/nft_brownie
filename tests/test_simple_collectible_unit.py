from scripts.utils import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
from brownie import network, SimpleCollectible
from scripts.simple_collectible.deploy_and_create import deploy_and_create 
import pytest


def test_can_create_simple_collectible_via_deploy():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    
    # Act
    simple_collectible = deploy_and_create()

    # Assert
    assert simple_collectible.ownerOf(0) == get_account(0) # first ganache account