# proc_gen readme
To run this, just excecute the _test_simulation.sh_ script. If you don't trust it, see what's inside. It's literally:
``` bash
python -m unittest ./test/proc/test_simulation.py
```

Note: I had some problems excecuting the test case with unittest. Discovered that I was using my system's python all the time, and when I tried the conda environment, couldn't get this to run. I don't know how to use conda it seems, but addind the period in the path seems to solve it.

> **Beware!** This simulation, with the ten steps configured in test_simulation.py generates a results file with around 10,000 lines. The amount of info is, as you could have imagined, really absurd and increases exponentially.