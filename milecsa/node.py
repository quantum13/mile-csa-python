from __milecsa import __register_node as register_node, \
    __unregister_node as unregister_node

from .transactions import Transaction


class Node(Transaction):
    # todo inconsistency

    address = None

    def __init__(self, wallet, address, assetCode, amount):

        Transaction.__init__(self, wallet=wallet)

        self.assetCode = int(assetCode)
        self.amount = str(amount)

        self.address = address

    def register(self):
        return register_node(self.wallet.public_key,
                             self.wallet.private_key,
                             self.address,
                             self.block_id,
                             self.tx_id,
                             self.assetCode,
                             self.amount)

    def unregister(self):
        return unregister_node(self.wallet.public_key,
                               self.wallet.private_key,
                               self.block_id,
                               self.tx_id)
