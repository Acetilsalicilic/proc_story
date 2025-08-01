# proc_gen readme
To run this, just excecute the _test_simulation.sh_ script. If you don't trust it, see what's inside. It's literally:
``` bash
python -m unittest test/proc/test_simulation.py
```

> **Beware!** This simulation, with the ten steps configured in test_simulation.py generates a results file with around 10,000 lines. The amount of info is, as you could have imagined, really absurd and increases exponentially.