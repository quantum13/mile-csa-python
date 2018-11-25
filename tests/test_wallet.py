import unittest
from milecsa import Wallet
import local_config


class MyTestCase(unittest.TestCase):

    def test_something(self):

        wallet0 = Wallet(phrase="secret-phrase")

        print()
        print(wallet0.public_key, wallet0.private_key)

        state = wallet0.get_state()
        print()
        print(state.balances, state.preferred_transaction_id, wallet0.public_key)
        for b in state.balances:
            print(b)

        wqr0 = wallet0.phrase_qr()
        print(wqr0)
        wqr0.save("./img-wqr0.png")

        wqr1 = wallet0.payment_qr(asset=1, amount=10)
        print(wqr1)
        wqr1.save("./img-wqr1.png")

        trx = wallet0.get_transactions()
        for t in trx:
            asset = wallet0.get_chain().asset_name(t.assetCode)
            print(t, t.source, "->[", t.description, "]", t.destination, " asset: ", t.assetCode, asset, " amount: ", t.amount)


if __name__ == '__main__':
    unittest.main()
