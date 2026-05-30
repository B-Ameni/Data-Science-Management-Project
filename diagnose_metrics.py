"""
Diagnostiquer pourquoi Precision@5 et Recall@5 sont à 0
"""
import pandas as pd
import numpy as np

print("=== DIAGNOSTIC ===\n")

print("1  Vérifier les films du test set")
print(f"   Test set contient {len(test_df)} interactions")
print(f"   Utilisateurs uniques dans test: {test_df['user_id'].nunique()}")
print(f"   Films uniques dans test: {test_df['item_id'].nunique()}")
print(f"   Films du test: {sorted(test_df['item_id'].unique())[:20]}")

print("\n2  Vérifier les recommandations")
sample_user = test_df['user_id'].iloc[0]
print(f"   Utilisateur: {sample_user}")

recs = recommend_hybrid(sample_user, n=5, alpha=0.5)
rec_items = [item for item, _ in recs]
print(f"   Recommandations: {rec_items}")

test_items = test_df[test_df['user_id'] == sample_user]['item_id'].values
print(f"   Films attendus (test): {test_items}")
print(f"   Intersection: {set(rec_items) & set(test_items)}")

print("\n3  Vérifier l'historique utilisateur (train)")
train_items = train_df[train_df['user_id'] == sample_user]['item_id'].values
print(f"   Films dans train: {train_items}")
print(f"   Recommandations vs Train: {set(rec_items) & set(train_items)}")

print("\n4  Problème probable:")
print("    Les recommandations CF filtrent les films déjà vus (train)")
print("    Les films du test ne sont pas dans train => pas recommandés")
print("    Solution: Calculer RMSE plutôt que Precision/Recall")
print("    Solution 2: Hit Rate (au moins 1 film trouvé)")
