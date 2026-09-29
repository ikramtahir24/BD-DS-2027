# Pourquoi tant d'entreprises ferment-elles au Maroc ?

*Question traitée : « Expliquer la fermeture d'un grand nombre d'entreprises au Maroc ».*

## 1. Cadrage : défaillances ≠ fermetures

Les chiffres disponibles mesurent les **défaillances** (faillites) recensées par Inforisk, et non toutes les fermetures (cessations volontaires, radiations). Autre précision : la tendance s'est **inversée en 2025**.

## 2. Ampleur du phénomène

- **15 658 défaillances en 2024**, un record, en hausse d'environ 10 % sur un an (Inforisk).
- Hausses annuelles de **+18 % en 2022 et +13 % en 2023**. Entre 2009 et 2024, les défaillances ont progressé en moyenne de **14 % par an** (hors 2020). Sur 2021-2024, cela représente environ **+47 %** (valeurs 2021-2023 reconstituées, voir limites).
- **2025 : -3,3 %** (≈ 15 100), une première depuis la période Covid. Prévision Inforisk 2026 : ~15 300, soit une stabilisation.
- Pour comparaison, Allianz Trade avait anticipé jusqu'à 16 800 cas en 2025 : les prévisions divergent selon les sources et les méthodes.

*(Graphique : `graphique_defaillances.png`, généré par `analyse_defaillances.py`.)*

## 3. Qui ferme, et où ?

- **Taille :** les TPE représentent **98,8 %** des défaillances, les moyennes entreprises 1,1 % et les grandes 0,1 %.
- **Secteurs (2024) :** commerce 33 %, immobilier 20 %, BTP 15 %, transport 9 %. Commerce, BTP et immobilier concentrent à eux seuls environ 60 % des entreprises marocaines, ce qui explique en partie leur poids mécanique.
- **Géographie :** Casablanca-Settat regroupe 4 410 défaillances en 2025, soit 29 % du total national.

## 4. Les causes

1. **Fin des aides Covid.** Les soutiens publics ont contenu les faillites jusqu'en 2021 ; leur retrait a été suivi d'une vague de défaillances (+18 % en 2022).
2. **Fragilité structurelle des TPE.** Sous-capitalisation, accès limité au financement, rapport de force défavorable avec les grands clients et **délais de paiement élevés**, qui asphyxient la trésorerie. Beaucoup ne passent pas le cap des 5 ans, surnommé la « vallée de la mort ».
3. **Chocs macroéconomiques 2022-2024.** Inflation, sécheresse et hausse des coûts ont pesé sur la demande et les marges, notamment dans le commerce et le BTP.
4. **Le stock de « sociétés zombies ».** La DGI dénombre plus de **300 000** sociétés fantômes ou inactives, soit environ une entreprise active sur trois. Selon Inforisk, le vrai risque se concentre sur elles plutôt que sur les faillites recensées.

## 5. Pourquoi le recul en 2025 ?

Inforisk l'explique par une conjoncture favorable : **croissance du PIB de 5 %**, pluviométrie améliorant la campagne agricole, **20 millions de touristes**, **inflation de 0,8 %** et investissements publics liés à la CAN 2025 et à la Coupe du monde 2030 qui dynamisent le BTP. Les faillites ne reculent donc pas parce que la fragilité structurelle disparaît, mais parce que le contexte est porteur.

## 6. Synthèse

Le nombre élevé de défaillances tient moins à un choc unique qu'à un **tissu de TPE fragiles** (98,8 % des cas), exposées aux délais de paiement, au retrait des aides Covid et aux chocs de conjoncture, avec de fortes concentrations dans le commerce, l'immobilier et le BTP. Le recul de 3,3 % en 2025 est conjoncturel et reste à confirmer.

## 7. Limites

- Les valeurs 2021, 2022, 2023 et 2025 sont **reconstituées** à partir des pourcentages publiés (statut `derive` dans le CSV) ; les sources mentionnent aussi ~+10 % ou +11 % pour 2024. À vérifier auprès d'Inforisk.
- Inforisk mesure les défaillances déclarées ; elles sous-estiment les cessations informelles.
- Analyse descriptive, sans modèle économétrique : les causes sont cohérentes avec les données mais non quantifiées.

## 8. Sources

- Inforisk via Le360 (2024) : https://fr.le360.ma/economie/entreprises-un-nombre-record-de-faillites-au-maroc-en-2024_VZKZZVNEF5G4LOC34JIR5VX7EE/
- Inforisk via Industries.ma (secteurs, aides Covid) : https://industries.ma/entreprises-marocaines-les-faillites-atteignent-un-niveau-record-en-2024/
- Inforisk via FNH (bilan 2025) : https://fnh.ma/article/actualite-economique/defaillances-entreprises-baisse-faillites
- Inforisk, sociétés zombies : https://inforisk.ma/blog/2026/02/05/defaillances-dentreprises-au-maroc-pourquoi-le-risque-se-concentre-sur-les-300-000-societes-zombies/
- Allianz Trade via LesEco.ma : https://leseco.ma/business/defaillances-dentreprises-une-hausse-record-attendue.html
