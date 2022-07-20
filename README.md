# DMA2022DataProjectC

## Einleitung

Dieses Projekt ist im Rahmen der Vorlesung "Datenmanagement und Archivierung im Umfeld der Forschung (DAF)" an der [Hochschule Mannheim](https://www.hs-mannheim.de/) mit Unterstützung von [Dr. Maximilian Fünfgeld](https://lu.linkedin.com/in/fuenfgeld?original_referer=https%3A%2F%2Fwww.google.com%2F) entstanden und hat als Ziel eine retrospektiven klinischen Studie durchzuführen. Dabei sind folgende Punkte besonders zu beachten:

* Erstellen eines [Datenmanagementplans](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenmanagementplan)
* [Richtige Aufbereitung der medizinischen Daten](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenvorverarbeitung) und deren [Analyse](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Analyse)
* Reproduzierbarkeit der [Auswertungen](./src)

## Thema des Forschungsprojekts

In Deutschland sind etwa zwei Drittel aller Männer und rund die Hälfte aller Frauen übergewichtig. Davon weist ungefähr ein Viertel sogar starkes Übergewicht (Adipositas) auf. Auch die Zahl an übergewichtigen Kindern ist in den vergangenen Jahren gestiegen. Um eine bessere Vorsorge für unsere Kunden leisten zu können, wollen wir als Krankenkasse [folgendes](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki) untersuchen: 
> _Inwiefern Übergewicht mit unterschiedlichen Erkrankungen korreliert, also, ob nachweislich festzustellen ist, dass Menschen mit Übergewicht häufiger an     bestimmten Krankheiten erkranken._

Hierfür wurden Patientendaten aus der elektronischen Patientenakte [(ePa)](https://www.bundesgesundheitsministerium.de/elektronische-patientenakte.html) als _csv_-Dateien expotiert. Die Daten wurden in einem [ETL-Prozess](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenvorverarbeitung) in ein [Sternschema transformiert](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Mappingtabellen) um effizentere Abfragen auf den Daten ausführen zu können. Dabei wurden unterschiedliche Kritierien der [Datenqualität](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenqualit%C3%A4t) und der [Datenintegrität](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenintegrit%C3%A4t) überprüft.
Zur besseren Nachvollziehbarkeit und Risikominimierung wurden verschiedene Risiken und ihre Gegenmaßnahmen in der [Datenschutzfolgeabschätzung](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenschutzfolgeabsch%C3%A4tzung) vorgestellt.

Eine Übersicht über die gesamte Projektplanung und ihren Verlauf finden Sie im [Datenmanagementplan](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenmanagementplan)

![Datenflussdiagramm](https://raw.githubusercontent.com/Fuenfgeld/DMA2022DataProjectC/main/images/Datenflussdiagramm.svg)

## Projekt Ausführung

Das Projekt kann entweder lokal oder online mit einem Google-Colab ausgeführt werden. 

### Google Colab

Für die Ausführung des Projekt in einem Colab-Book ist ein [Google-Account](https://support.google.com/accounts/answer/27441?hl=de) notwending, falls dieser nicht vorhanden sein sollte folgen Sie der manuelle Installationsanleitung. 

* [ETL-Colab-Book](https://colab.research.google.com/github/Fuenfgeld/DMA2022DataProjectC/blob/main/src/ETL.ipynb)
* [Analyse-Colab-Book](https://colab.research.google.com/github/Fuenfgeld/DMA2022DataProjectC/blob/main/src/analysis.ipynb)

<font size="8">**⚠**</font> Um das Notebook in Goole-Colab ausführen zu können, muss zuvor folgender Zeilen zu beginn des Notebooks auskommentiert werden.

```
!git clone https://github.com/Fuenfgeld/DMA2022DataProjectC.git
%cd DMA2022DataProjectC/src
```

### Manuelle Installation

Zur Ausführung des Projektes wird eine [Python 3.x Version](https://www.python.org/downloads/) benötigt. Anschließend führen Sie folgende Schritte durch:

1. Repository klonen: Kopieren Sie sich den Inhalt des Repositories auf Ihren Rechner. Eine genaue Erklärung dazu finden Sie [hier](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

2. Installieren Sie die Python-Dependencies auf Ihren Rechner. Hierzu öffen Sie ein Terminal Fenster im Startverzeichnis des Projekts und führen folgenden Befehl aus:

```
pip install -r requirements.txt
```

3. Nun können Sie im Terminal die Jupyter-Notebook App öffnen:

```
jupyter notebook
```

Nun sollte sich im Browser das Jupyter-Notebook als Dateipfad des Projektes öffnen. Bei Problemen schauen Sie [hier](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html) nach. Falls Sie noch nie mit Jupyter-Notebooks gearbeitet haben finden Sie [hier](https://www.dataquest.io/blog/jupyter-notebook-tutorial/) erste einführende Schritte.

4. Führen Sie zuerst das [ETL-Notebook](./src/ETL.ipynb) aus, welches die Rohdaten in ein passendes Datenschema für die Analyse verarbeiten. Danach können Sie das [Analyse-Notebook](./src/analysis.ipynb) öffnen und die einzelnen Sektionen einzeln nachvollziehen. 

## Video

TBD

## Literatur & Kurse

Im Rahmen des Kurses wurden folgende Themen im Vorfeld ausgearbeitet, die eine gute Grundlage für das Verständnis dieses Projektes bilden:

* [Einführung in Python](https://www.python-lernen.de/)
* [Einführung in SQL & Data Engineering und Datenmodellierung](https://github.com/Fuenfgeld/2022TeamBDataEngineeringBC)
* [ETL-Process](https://github.com/Fuenfgeld/2022TeamADataEngineeringBC)
* [Medizinische Daten (Datentypen, Metadaten und biomedizinische Standards) & Archivierung nach FAIR](https://github.com/Fuenfgeld/2022TeamADataManagementBC)
