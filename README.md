# hackmit2020
Voter purging, or the erroneous removal of eligible voters from registration rosters, has revealed itself to be a concerning issue in the state of Georgia in the last five years. Investigations<sup>1</sup> into publicized voter purging lists have concluded that an alarming number of registered voters were removed on incorrect accounts of moving to a different state or county. Combined with Georgia's voting laws which mandate that all citizens register within 2 weeks of voting and unreliable systems of alerting removed voters, this problem demands a better solution. Our project, VoterAlertGA, is a notification system that emails members upon detection of changes to their voting registration status.

<sup>1</sup>sources:
<br>https://www.acluga.org/sites/default/files/georgia_voter_roll_purge_errors_report.pdf
<br>https://www.ajc.com/news/state--regional-govt--politics/many-eligible-georgia-voters-were-canceled-nation-largest-purge/jRlixHpVs0I9wVQYdDjxvM/

Our project is split into two parts: the front end (webapp accessed via the "run.py" file) where users input their email and relevant info, and the back end (the database "app.db" and the crucial script "hackmit_main.py") which stores the data and (in theory) runs a script daily to find the users whose registration status has changed in order to send them an email notification. 
