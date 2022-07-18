# DMA2022DataProjectC

## Einleitung

Diese Projekt ist im Rahmen der Vorlesung Datenmanagement und Archivierung im Umfeld der Forschung (DAF) an der [Hoschule Mannheim](https://www.hs-mannheim.de/) mit Begleitung von [Dr. Maximilan Fünfgeld](https://lu.linkedin.com/in/fuenfgeld?original_referer=https%3A%2F%2Fwww.google.com%2F) entstanden und hat als Ziel dem Ablauf einer retrospektive klinische Studie zu planen und durchzuführen. Dabei sind besonderst folgende Punkte zu beachten:

* [Datenmanagementplan](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenmanagementplan)
* [Medizinische Daten richtig aufzubereiten](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenvorverarbeitung) und zu [analysieren](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Analyse)
* Reproduzierbarkeit der [Auswertungen](./src)

## Forschungsprojekt

In Deutschland sind etwa zwei Drittel aller Männer und rund die Hälfte aller Frauen übergewichtig. Davon weist ungefähr ein Viertel sogar starkes Übergewicht (Adipositas) auf. Auch die Zahl an übergewichtigen Kindern ist in den vergangenen Jahren gestiegen. Um eine bessere Vorsorge für unsere Kunden leisten zu können, wollen wir als Krankenkasse [folgendes](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki) untersuchen: 
> _Inwiefern Übergewicht mit unterschiedlichen Erkrankungen korreliert, also, ob nachweislich festzustellen ist, dass Menschen mit Übergewicht häufiger an     bestimmten Krankheiten erkranken._

Hierzu haben wir aus verschiedene Patientendaten aus den elektronische Patientenakte[(ePa)](https://www.bundesgesundheitsministerium.de/elektronische-patientenakte.html) als CSV-Datein expotiert. Diese wurden anschließend in einem [ETL-Process](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenvorverarbeitung) in einen [Sternschema tranfomiert](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Mappingtabellen), um effizenter Abfrage auf den Daten auführen zu könne. Dabei wurden unterschiedliche kritierien der [Datenqualität](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenqualit%C3%A4t) und der darauf folgenden [Datenintegrität](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenintegrit%C3%A4t) überprüft.
Zur Nachvollziehbarkeit und Sicherheit der Pipeline wurde verschiedene Risiken und Gegenmaßnahmen in der [Datenschutzfolgeabschätzung](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenschutzfolgeabsch%C3%A4tzung), wie eindeutige Checksummen für der Rohdaten, vorgestellt.

Eine Übersicht über die Projektplanung und ihreren Verlauf finden Sie im [Datenmanagementplan](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenmanagementplan)

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

4. Anschließend führen Sie zuerst das [ETL-Notebook](./src/ETL.ipynb) aus, welches die Rohdaten in ein passendes Datenschema für die Analyse verarbeiten. Danach können Sie das [Analyse-Notebook](./src/analysis.ipynb) öffnen und die einzelnen Sektionen einzeln durchführen. Falls Sie noch nie mit Jupyter-Notebooks gearbeitet haben finden Sie [hier](https://www.dataquest.io/blog/jupyter-notebook-tutorial/) erste Schritte.

## Video

TBD

## Literatur & Kurse

Zuvor wurden einige Themen für diese Projekt in anderen Gruppen ausgearbeitet und bieten eine gute Grundlage für Verständniss des Projektes.

* [Einführung in Python](https://www.python-lernen.de/)
* [Einführung in SQL & Data Engineering und Datenmodellierung](https://github.com/Fuenfgeld/2022TeamBDataEngineeringBC)
* [ETL-Process](https://github.com/Fuenfgeld/2022TeamADataEngineeringBC)
* [Medizinische Daten (Datentypen, Metadaten und biomedizinische Standards) & Archivierung nach FAIR](https://github.com/Fuenfgeld/2022TeamADataManagementBC)
