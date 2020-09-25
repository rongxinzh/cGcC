# cGcC
A simple python3 implementation of cGcC score algorithm.
cGcC is an algorithm proposed by Jean-Denis Beaudoin *et al.* in 2013 that can be used to characterized the formation capabilities of RNA G-quadruplexes.

The script can be easily executed under the **python3** environment (**python3.6 is recommended**, for that other python versions are not tested).

**STEP**

**s1: Download the source code of cGcC from github.**

**s2: Execute the python script.**
```python3
# -i inputfile path
# -o outputfile path
python cGcC.py -i input.txt -o output.txt 
```
please note, the input file should contains one column, for each line including one sequence.
Below is the example of input file
```
ACTGCATCACATCAGGGGACTGGGGACACAGGGGACGGGGGACTATCATCACAT
ACAGGGCAGGGCACGGAGGACAGGGACATGCCGGCCC
GAGCCTGGGCACGGGACCACACCATCGGGCACTAGCCACACACAC
GGGCAGGGAGGGAAGGGGAAAGGGGCACGAGGGCGAGCGAGCGAGACA
```
The script will output two columns into your output file. Column 2 indicates the cGcC score.
```
ACTGCATCACATCAGGGGACTGGGGACACAGGGGACGGGGGACTATCATCACAT	7.384615384615385
ACAGGGCAGGGCACGGAGGACAGGGACATGCCGGCCC	2.15
GAGCCTGGGCACGGGACCACACCATCGGGCACTAGCCACACACAC	1.2692307692307692
GGGCAGGGAGGGAAGGGGAAAGGGGCACGAGGGCGAGCGAGCGAGACA	12.428571428571429
```

*cGcC citation: Nucleic Acids Res. 2014 Jan;42(2):1209-23. doi: 10.1093/nar/gkt904. Epub 2013 Oct 10.*

Bug report: rongxinzhang@seu.edu.cn

