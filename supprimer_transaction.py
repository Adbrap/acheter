from ib_insync import *

# Connexion à TWS ou IB Gateway
ib = IB()
ib.connect('192.168.10.220', 7497, clientId=2)  # Mettre le port 7496 pour Live et le port 7497 pour Paper

# Se connecter à votre compte IB
accountName = "abtrading3333"
accountPassword = "ZD68gm5h!"
managedAccounts = ib.managedAccounts()
if len(managedAccounts) == 0:
    print("Erreur: Pas de compte géré trouvé.")
    ib.disconnect()
    exit()
account = managedAccounts[0]

# Créer un contrat pour l'action Google
contract = Stock('AMZN', 'SMART', 'USD')

# Récupérer toutes les positions pour l'action Google
positions = ib.positions()
goog_positions = [p for p in positions if p.contract.symbol == 'GOOG']

# Fermer toutes les positions sur l'action Google
if goog_positions:
    for position in goog_positions:
        order = MarketOrder('SELL', abs(position.position))
        trade = ib.placeOrder(contract, order)
        ib.sleep(1)
        print(f"Position {position.contract.symbol} fermée : {trade.orderStatus.status}, position : {position.position}, ordre : {trade.order.orderId}")
else:
    print("Erreur: Pas de position sur cette action.")

# Se déconnecter de TWS ou IB Gateway
ib.disconnect()
