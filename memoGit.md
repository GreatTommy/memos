# Mémo Git

## Création d'un commit

```bash
mkdir monPremierRepo
git init # activer un dossier comme repository Git (se placer dans le dossier)
git add checklist-vacances.md # ajouter un nouveau fichier à l'index git
git commit -m "Add checklist-vacances.md" # enregister les modifications
git commit -a -m "MAJ checklist-vacances.md" # mis à jour d'un fichier déja existant
```

## Lire l'historique

```shell
git log #  affiche la liste de tous les commits réalisés
```

Se lit du haut (le plus récent) en bas (le plus ancien)

Chaque commit est répertorié avec :

- son SHA
- son auteur
- sa date
- sa description 

## Historique de commits

```bash
git checkout SHADuCommit # se positionner sur un commit donné
git checkout master # revenir à la branche principale (la + récente)
```

## Modification de commit

```shell
git revert SHADuCommit # nouveau commit : inverse du précédent
git commit --amend -m "Votre nouveau message" # modifier le message du dernier commit
git reset --hard # annuler tous les changements (non commit)
```









 



