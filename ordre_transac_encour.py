# Importer les modules requis
from ib_insync import *

# Se connecter à TWS/IB Gateway
ib = IB()
ib.connect('192.168.10.220', 7497, clientId=2)

# Créer un contrat pour l'action Google
contract = Stock('GOOG', 'SMART', 'USD')

# Créer un ordre d'achat
order = MarketOrder('BUY', 1)

# Passer l'ordre pour le contrat
trade = ib.placeOrder(contract, order)
ib.sleep(1)

# Obtenir tous les ordres en cours
orders = ib.orders()

# Afficher les ordres en cours
print('Ordres en cours:')
for order in orders:
    print(order)

# Obtenir toutes les transactions en cours
trades = ib.openTrades()

# Afficher les transactions en cours
print('Transactions en cours:')
for trade in trades:
    print(trade)

# Déconnecter de TWS/IB Gateway
ib.disconnect()
