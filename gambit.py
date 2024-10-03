import pygambit as gbt
g = gbt.Game.new_tree(players=["Buyer", "Seller"],title="One-shot trust game, after Kreps (1990)")
print(g.root)