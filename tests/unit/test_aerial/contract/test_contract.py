from unittest.mock import Mock

from cosmpy.aerial.contract import LedgerContract
from cosmpy.aerial.wallet import LocalWallet
from cosmpy.common.utils import json_encode

# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2022 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------


def test_contract_behaves_like_address_string():
    """Test contract behaves like it's address string and can be serialized."""
    address = LocalWallet.generate().address()
    contract = LedgerContract(None, Mock(), address=address)

    assert contract.address

    assert contract == contract.address
    assert json_encode(contract) == json_encode(contract.address)
