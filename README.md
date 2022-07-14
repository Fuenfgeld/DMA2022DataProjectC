# DMA2022DataProjectC

## Einleitung

Das Projekt ist in der Vorlesung Datenmanagement und Archivierung im Umfeld der Forschung (DAF) an der Hoschule Mannheim mit Begleitung von Dr. Maximilan Fünfgeld entstanden und hat als Ziel eine retrospektive klinische Studie zu planen und mit folgenden Punkten zu implementieren:

* eine [Datenmanagementplan](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenmanagementplan) erstellen
* synthetische [medizinische Daten aufzubereiten](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenvorverarbeitung) und zu [analysieren](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Analyse)
* reproduzierbare [Auswertungen zu implementieren](./src)

![Datenflussdiagramm](https://raw.githubusercontent.com/Fuenfgeld/DMA2022DataProjectC/main/images/Datenflussdiagramm.svg)


## Installation

Zur Ausführung des Projektes wird eine [Python 3 Version](https://www.python.org/downloads/) benötigt, anschließend führen Sie folgende Schritte aus:

1. Repository klonen: Kopieren Sie sich den Inhalt des Repositories auf Ihren Rechner. Eine genauere Erklärungd dazu finden Sie [hier](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

2. Installieren Sie die Python-Dependencies auf Ihren Rechner. Hierzu öffen Sie ein Terminal Fenster im Startverzeichniss des Projekts und führen folgenden Befehl aus:

```
pip install -r requirements.txt
```

3. Nun können Sie im Terminal die Jupyter-Notebook App öffnen:

```
jupyter notebook
```

Nun sollten sich im Browser die Jupyter-Notebook als Dateipfad des Projektes öffnen. Bei Problemen schauen Sie [hier](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html) nach.

4. Anschließend können Sie das ETL-Notebook und Analyse-Notebook öffnen und die einzelnen Sektionen einzeln durchführen. Falls Sie noch nie mit Jupyter-Notebooks gearbeitet haben finden Sie [hier](https://www.dataquest.io/blog/jupyter-notebook-tutorial/) erste Schritte.

## Video

TBD

## Literatur & Kurse

Zuvor wurden einige Themen für diese Projekt in anderen Gruppen ausgearbeitet und bieten eine gute Grundlage für Verständniss des Projektes.

* [Einführung in Python](https://www.python-lernen.de/)
* [Einführung in SQL & Data Engineering und Datenmodellierung](https://github.com/Fuenfgeld/2022TeamBDataEngineeringBC)
* [ETL-Process](https://github.com/Fuenfgeld/2022TeamADataEngineeringBC)
* [Medizinische Daten (Datentypen, Metadaten und biomedizinische Standards) & Archivierung nach FAIR](https://github.com/Fuenfgeld/2022TeamADataManagementBC)
