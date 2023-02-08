
# berechnung

## Heizwärmebedarf

"2  Heizwärmebedarf
Der effektive Heizwärmebedarf (QH,eff, QH,eff,korr) wird gemäss SIA 380/1:2016
[1] berechnet. Hierbei ist zu berücksichtigen:

- Ist    eine    Lüftungsanlage    vorhanden,    wird    der    flächenbezogene Aussenluftvolumenstrom gemäss Kap. 4 verwendet.
- Ist keine Lüftungsanlage vorhanden, kann bei den Standardnutzungsdaten der   flächenbezogene   Aussenluftvolumenstrom  jeder   Nutzung  an  die Dichtheit der Gebäudehülle angepasst werden (0.7 – 1.5 m3/(h m2)). Es wird  gemäss  Gl.  1  der  flächengemittelte  Wert  für  die  Berechnung  des Heizwärmebedarfs bestimmt.
- Liegt eine Mischnutzung vor, werden folgende Parameter flächenanteilig berücksichtigt:
  - Standardnutzungsdaten (Gl. 1), Wärmeeintrag von Personen (Gl. 2)
  - Konstanten ao  und Ƭo  (Gl. 1) zur Bestimmung des Ausnutzungsgrades ηg

Wie in Kap. 1.2 bereits beschrieben, basiert die Berechnung der Mischnutzung auf einem Einzonenmodell. Das Einzonenmodell wurde gewählt,  um  die  Berechnung,  die  Programmverwaltung  und  die Wärmeversorgung  durch  verschiedene  Wärmeerzeuger in verschiedenen Versorgungsbereichen einfach zu halten.

"Die  flächengemittelten  Standardnutzungsdaten  für  Mischnutzungen   SNutz berechnen sich aus der Summe der flächengemittelten Einzelreferenzwerten. Gl. 1 gilt für die Standardnutzungsdaten:

- Raumtemperatur
- Regelungszuschlag für Raumtemperatur
- Präsenzzeit pro Tag
- Elektrizitätsbedarf
- Reduktionsfaktor für Elektrizitätsbedarf
- Thermisch wirksamer Aussenluftvolumenstrom"

"𝑁𝑁𝑢𝑡𝑧
𝐴𝐸,𝑁𝑢𝑡𝑧,𝑛
𝑆𝑁𝑢𝑡𝑧  =    ∑   𝑆𝑁𝑢𝑡𝑧,𝑛  ∙       𝐴
𝑛=1                                     𝐸"                                               [Einheit]       Gl. 1            
                                                                  
 n              [-]          Laufindex für Anzahl Nutzungen NNutz, n = 1 … NNutz                                         
 SNutz,n              [Einheit]          Parameter der Standardnutzungsdaten bzw. Konstanten ao und Ƭo  der Nutzung n                                         
 AE,Nutz,n              [m2]          Energiebezugsfläche der Nutzung n                                         
 AE              [m2]          Energiebezugsfläche gesamt                                         
Gl.  1  kann  analog  auch  für  andere  Parameter  für  die  Flächenmittelung verwendet werden.                                                                  
Bei  einer  Mischnutzung  (Einzonenmodell)  gilt   Gl.  2  für  den  gesamten Wärmeeinträge     durch     Personen     QI,P       bei     der     Berechnung     des Heizwärmebedarfs gemäss SIA 380/1:                                                                  
"𝑁𝑁𝑢𝑡𝑧
 𝑡𝑃,𝑠𝑡𝑑,𝑁𝑢𝑡𝑧,𝑛     𝐴𝐸,𝑁𝑢𝑡𝑧,𝑛               𝑡𝑐
𝑄𝐼,𝑃  =  (  ∑   𝑄𝑃,𝑠𝑡𝑑,𝑁𝑢𝑡𝑧,𝑛  ∙ 𝐴                     ∙       𝐴        )  ∙  1000
𝑛=1                                           𝑃,𝑠𝑡𝑑,𝑁𝑢𝑡𝑧,𝑛                 𝐸"                                             [kWh/(m2a)]           Gl. 2          
                                                                  
 n              [-]          Laufindex für Anzahl Nutzungen NNutz, n = 1 … NNutz                                         
 QP,std,Nutz,n              [W/P]          Standardnutzungsdaten für Wärmeabgabe durch Personen gemäss SIA 380/1:2016 entsprechend der Nutzung n                                         
 tP,std,Nutz,n              [h/d]          Standardnutzungsdaten für Präsenzzeit pro Tag gemäss SIA 380/1:2016 entsprechend der Nutzung n                                         
 AP,std,Nutz,n              [m2/P]          Standardnutzungsdaten für Personenfläche gemäss SIA 380/1:2016 entsprechend der Nutzung n                                         
 tC              [d]          Länge Berechnungsschritt                                         
 AE,Nutz,n              [m2]          Energiebezugsfläche der Nutzung n                                         
 AE              [m2]          Energiebezugsfläche gesamt                                         

## Heizung und Warmwasser

Allgemeines
Wärmeerzeuger
Holzofen als Zusatzheizung
Speichertypen
Wärmeverluste
Zuordnung der Speicherverluste auf Wärmeerzeuger
Rückgewonnene Verluste für Heizung
Endenergie
Hilfsenergie
Referenztabellen Heizung und Warmwasser

4 Lüftung
Allgemeines
Kleinanlagen mit Standardwerten
Sonstige Lüftungsanlagen
Referenztabellen Lüftung

5 Elektrischer Ertrag aus PV und WKK/BHKW
Photovoltaik
WKK/BHKW

6 Elektrizität
Allgemeines
Wohnen
Referenztabellen Wohnen
Zweckbauten
Referenztabellen Zweckbauten

7   Etikette
Projektwert
Referenzwert
Kennwerte und Klassierung
