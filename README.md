# Praktikum 'Verteilte Systeme'
RESTfull Webservice, MQTT, Docker

# User-Stories

## Aufgabe 1: RESTfull Webservice

Zu Programmieren ist ein RESTfull-Webservice auf dem Raspberry Pi.
Über diesen Webservice wird die am Raspberry Pi angeschlossene PiCamera bedient.
Der Server ist mit Hilfe von CherryPy implementiert.

| Als          | will ich                                                                                                                                      | damit                                                                                                               |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Studierender | selbständig, alle erforderlichen Libraries und Funktionalitäten studieren, überprüfen und installieren.                                       | er den Server implementieren kann.                                                                                  |
| Server       | auf einen HTTP-Request vom Benutzer warten.                                                                                                   | dieser die entsprechende Funktion ausführt.                                                                         |
| Server       | die Kamera-Schnittstelle des Raspberry Pi verwalten.                                                                                          | der Benutzer die Kamera des Raspberry Pi nutzen kann.                                                               |
| Benutzer     | einen HTTP-GET-Request von einem beliebigen Rechner abschicken in der Form von </br>__curl http://pi.local:8080/index.html__ .                | der Server die Startseite zur Bedienung der PiCamera ausliefert. Diese ist nur eine statische HTML-Seite angezeigt. |
| Benutzer     | einen HTTP-GET-Request von einem beliebigen Rechner abschicken in der Form von </br>__curl http://pi.local:8080/api/camera__ .                | der Server, falls vorhanden, das zuletzt erstellte Bild ausliefert.                                                 |
| Benutzer     | einen HTTP-POST-Request von einem beliebigen Rechner abschicken in der Form von </br>__curl -X "POST" http://pi.local:8080/api/camera__ .     | der Server ein Bild mit der PiCamera erstellt.                                                                      |
| Benutzer     | einen HTTP-DELETE-Request von einem beliebigen Rechner abschicken in der Form von </br>__curl -X "DELETE" http://pi.local:8080/api/camera__ . | der Server das Bild, falls vorhanden, löscht.                                                                       |
<center> Tabelle: User Story - RESTfull Webservice </center>


## Aufgabe 2: MQTT-Teilnehmer

Zu programmieren ist ein MQTT-Teilnehmer auf dem Raspberry Pi, der die PiCamera ansteuert. Ein weiterer MQTT-Teilnehmer PUBLISHED Daten im JSON-Format, der MQTT-Teilnehmer, der die PiCamera steuert, nimmt diese entgegen, dekodiert die entsprechende Aktion aus der JSON-Nachricht und führt die entsprechende Aktion mit der PiCamera aus.

| Als                | will ich                                                                                                                                          | damit                                                            |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| Studierender       | selbständig, alle erforderlichen Libraries und Funktionalitäten studieren, überprüfen und installieren.                                           | er den Server implementieren kann.                               |
| MQTT-Teilnehmer #1 | mich auf einen MQTT-Broker über SUBSCRIBE registieren.                                                                                            | ich von ihm Daten in Form von JSON empfangen kann.               |
| MQTT-Teilnehmer #1 | die im JSON-Format empfangenen Daten dekodieren                                                                                                   | ich die entsprechenden Aktionen mit der PiCamera ausführen kann. |
| MQTT-Teilnehmer #2 | über den MQTT-Broker und PUBLISH einen Befehl in Form von </br>__mosquitto_pub -h pi.local -t pi/camera -m "{'cmd':'capture'}"__ verschicken.     | MQTT-Teilnehmer #1 ein Bild mit der PiCamera macht.              |
| MQTT-Teilnehmer #2 | über den MQTT-Broker und PUBLISH einen Befehl in Form von </br>__mosquitto_pub -h pi.local -t pi/camera -m "{'cmd':'video_start'}"__ verschicken. | MQTT-Teilnehmer #1 eine Video-Aufnahme mit der PiCamera startet. |
| MQTT-Teilnehmer #2 | über den MQTT-Broker und PUBLISH einen Befehl in Form von </br>__mosquitto_pub -h pi.local -t pi/camera -m "{'cmd':'video_stop'}"__ verschicken.  | MQTT-Teilnehmer #1 ein gestartetes Video stoppt.                 |
| MQTT-Teilnehmer #2 | über den MQTT-Broker und PUBLISH einen Befehl in Form von </br>__mosquitto_pub -h pi.local -t pi/camera -m "{'cmd':'delete'}"__ verschicken.      | MQTT-Teilnehmer #1 alle Videos und Bilder löscht.                |
<center> Tabelle: User Story - MQTT </center>


## Aufgabe 3: Docker-Container

Es ist ein Docker-Container aufzusetzen, der den RESTfull Webservice aus Aufgabe 1 und den MQTT-Broker sowie den MQTT-Teilnehmer #1 aus Aufgabe 2 enthält.

| Als          | will ich                                                                                                | damit                                                          |
|--------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| Studierender | selbständig, alle erforderlichen Libraries und Funktionalitäten studieren, überprüfen und installieren. | er den Server implementieren kann.                             |
| Studierender | ein Image PICAMERA mit den Anwendungen aus Aufgabe 1 und 2 über **docker build** generieren.            | die Anwendungen im Docker-Container ausgeführt werden können.  |
| Anwender     | über **docker run** das PICAMERA Image als Container starten.                                           | die Anforderungen aus Aufgabe 1 und 2 überprüft werden können. |

<center> Tabelle: User Story - Docker-Container </center>

### Überarbeitete User-Story

| Als          | will ich                                                                                                | damit                                                          |
|--------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| Studierender | selbständig, alle erforderlichen Libraries und Funktionalitäten studieren, überprüfen und installieren. | er den Server implementieren kann.                             |
| Studierender | ein Image __web__ für die Anwendung aus Aufgabe 1 sowie ein Image __mqtt__ mit der Anwendungen aus 2 jeweils über **docker build** generieren.            | die Anwendungen im Docker-Container ausgeführt werden können.  |
| Anwender     | über **docker run** die beiden Images als Container starten.                                           | die Anforderungen aus Aufgabe 1 und 2 überprüft werden können. |

<center> Tabelle: User Story - Docker-Container (überarbeitet)</center>
