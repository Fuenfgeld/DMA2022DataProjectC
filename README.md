# DMA2022DataProjectC

## Einleitung

Dieses Projekt ist im Rahmen der Vorlesung "Datenmanagement und Archivierung im Umfeld der Forschung (DAF)" an der [Hochschule Mannheim](https://www.hs-mannheim.de/) mit Unterstützung von [Dr. Maximilian Fünfgeld](https://lu.linkedin.com/in/fuenfgeld?original_referer=https%3A%2F%2Fwww.google.com%2F) entstanden und hat das Ziel eine retrospektive klinische Studie durchzuführen. Dabei sind folgende Punkte besonders zu beachten:

* Erstellen eines [Datenmanagementplans](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenmanagementplan)
* [Richtige Aufbereitung der medizinischen Daten](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenvorverarbeitung) und deren [Analyse](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Analyse)
* Reproduzierbarkeit der [Auswertungen](./src)

## Thema des Forschungsprojekts

In Deutschland sind etwa zwei Drittel aller Männer und rund die Hälfte aller Frauen übergewichtig. Davon weist ungefähr ein Viertel sogar starkes Übergewicht (Adipositas) auf. Auch die Zahl an übergewichtigen Kindern ist in den vergangenen Jahren gestiegen. Um eine bessere Vorsorge für unsere Kunden leisten zu können, wollen wir als Krankenkasse [folgendes](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki) untersuchen: 
> _Inwiefern Übergewicht mit unterschiedlichen Erkrankungen korreliert, also, ob nachweislich festzustellen ist, dass Menschen mit Übergewicht häufiger an     bestimmten Krankheiten erkranken._

Hierfür wurden Patientendaten aus der elektronischen Patientenakte [(ePa)](https://www.bundesgesundheitsministerium.de/elektronische-patientenakte.html) als _csv_-Dateien exportiert. Die Daten wurden in einem [ETL-Prozess](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenvorverarbeitung) in ein [Sternschema transformiert](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Mappingtabellen), um effizentere Abfragen mit den Daten durchführen zu können. Dabei wurden unterschiedliche Kritierien der [Datenqualität](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenvorverarbeitung#datenpr%C3%BCfung) überprüft.
Zur besseren Nachvollziehbarkeit und Risikominimierung wurden verschiedene Risiken und ihre Gegenmaßnahmen in der [Datenschutzfolgeabschätzung](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenschutzfolgeabsch%C3%A4tzung) vorgestellt.

Eine Übersicht über die gesamte Projektplanung und ihren Verlauf finden Sie im [Datenmanagementplan](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Datenmanagementplan)

![Datenflussdiagramm](https://raw.githubusercontent.com/Fuenfgeld/DMA2022DataProjectC/main/images/Datenflussdiagramm.svg)

_Abbildung 1: Datenflussdiagramm des gesamten Projekts mit Verweise auf die einzelnen Schritte._

Anschließend kann die [Analyse](https://github.com/Fuenfgeld/DMA2022DataProjectC/wiki/Analyse) zur Beantwortung der Forschungsfrage durchgeführt werden. Hierzu haben wir die Verteilung der BMI-Werte für die 10 am häufigsten vorkommenden Krankheiten betrachtet (Abb. 2). Dabei ist gut zu erkennen, dass die Anzahl vieler Krankeiten (Hyptertension,Prediabetes,...) bei einem BMI-Wert von ~28 rapide ansteigt. 

![AnalyseDiagramm](https://raw.githubusercontent.com/Fuenfgeld/DMA2022DataProjectC/main/images/distribution.svg)

_Abbildung 2: Verteilung der BMI-Werte pro Erkrankungsdiagnosen: Links als Boxplots und rechts als Verteilungsfunktionen dargestellt._


## Projekt Ausführung

Das Projekt kann entweder lokal oder online mit einem Google-Colab ausgeführt werden. 

### Google Colab

Für die Ausführung des Projekt in einem Colab-Book ist ein [Google-Account](https://support.google.com/accounts/answer/27441?hl=de) notwendig. Falls dieser nicht vorhanden sein sollte folgen Sie der manuellen Installationsanleitung. 

* [ETL-Colab-Book](https://colab.research.google.com/github/Fuenfgeld/DMA2022DataProjectC/blob/main/src/ETL.ipynb)
* [Analyse-Colab-Book](https://colab.research.google.com/github/Fuenfgeld/DMA2022DataProjectC/blob/main/src/analysis.ipynb) (⚠ Bitte führen Sie die Codeblöcke mit dem "Run all" Befehl aus, um eine korrekte Funktion zu gewährleisten.)

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

[https://drive.google.com/file/d/1Q1wn_I_Z_I0G6pcFTpyk6Pz8wL6TTOs4/view?usp=sharing](https://drive.google.com/file/d/1Q1wn_I_Z_I0G6pcFTpyk6Pz8wL6TTOs4/view?usp=sharing)

## Literatur & Kurse

Im Rahmen des Kurses wurden folgende Themen im Vorfeld ausgearbeitet, die eine gute Grundlage für das Verständnis dieses Projektes bilden:

* [Einführung in Python](https://www.python-lernen.de/)
* [Einführung in SQL & Data Engineering und Datenmodellierung](https://github.com/Fuenfgeld/2022TeamBDataEngineeringBC)
* [ETL-Process](https://github.com/Fuenfgeld/2022TeamADataEngineeringBC)
* [Medizinische Daten (Datentypen, Metadaten und biomedizinische Standards) & Archivierung nach FAIR](https://github.com/Fuenfgeld/2022TeamADataManagementBC)

## Disclaimer: In dem Projekt wurden synthetische Daten verwendet. Keine echten Patienten Data (siehe https://github.com/synthetichealth/synthea)

