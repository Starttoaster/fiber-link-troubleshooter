# fiber-link-troubleshooter
Takes dBm light level inputs and does calculations to solve the cause of a down fiber link. Runs in any shell with python installed.

This Python script assumes you have a certified fiber light testing device that can take readings in dBm. Additionally you should know how to access the relevant OS and switch to attain the readings from either SFP unit. Here is an example of the input-output of this script:

```
$ python fiber-troubleshooting.py
Enter the dBm reading of the SFP on the HOST side [ex. -2.8]-2.7
Enter the dBm reading of the CABLE on the HOST side [ex. -2.8]-2.3
Enter the dBm reading of the Switch SFP/Panel? [ex. -2.8]-2.7
Enter the dBm reading of the CABLE at the Switch SFP/Panel? [ex. -2.8]-2.3
Do these readings closely match the SFP/Switch output readings(+ or - 0.1 dB)? (0 = No, 1 = Yes, 2 = Unknown)1

The following is the prefab to send Support...


Hello,

Fiber and SFPs have been tested as follows:

Host Tx:  -2.7  dBm
Host Rx:  -2.3  dBm
Switch Tx:  -2.7  dBm
Switch Rx:  -2.3  dBm
dB Loss from Host to Switch:  -0.4  dB
dB Loss from Switch to Host:  -0.4  dB

Cabling passed test:  True
SFP transmitters are healthy:  True
SFP receivers are healthy:  True

No Layer 1 issues -> HBA is likely the culprit but doesn't rule out SFPs. Swap SFPs and monitor for additional issues, if issue persists schedule HBA replacement.
```
