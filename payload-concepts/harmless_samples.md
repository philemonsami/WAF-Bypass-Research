# Harmless Payload Samples

These payloads act as a control. If a WAF blocks these known harmless requests, the WAF is producing a false positive, and its testing models are overly eager.

## General Test Cases

-   `GET /search?q=select+some+shoes` (Contains the keyword `select`, often flagged by poorly written regex)
-   `GET /profile?name=O'Connor` (Contains a single quote `'`, a common SQLi trigger)
-   `POST /comment` Body: `<script> This is not actual code. I am just writing a script about a play.` (Contains brackets and the word script, testing context-aware vs dumb matching)
-   `GET /download?file=../../../../usr/local/temp/my_doc.txt` (Contains consecutive dots and slashes; a robust WAF might analyze if the path resolves to an allowed directory instead of instantly flagging it as an attack.)

## Verification Utility

The purpose of these samples is to calibrate fuzzing runs. Before throwing malicious payloads, confirming that the WAF allows standard inputs prevents wasting time on a WAF that acts as a blunt force filter blocking everything.
