# Battery-Analysis
This project analyses Lithium-ion Battery test data to evaluate change in instantaneous votage drop and change in internal resistance with cycle count

This project loads the required data from the cycler's database using predefined sql queries and saves it as a csv. The calculations are then done by running instant_drop.py followed by delta_R.py. Plotting for analysis is done through plot.py.

## Features
-Instananeous Votage Drop
-Internal Resistance

## Installation

Clone the repository

```bash
git clone https://github.com/david-mathew-v/Battery-Analysis.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

## Usage
```bash
python instant_drop.py
python delta_R.py
python plot.py
```

Generated csv will be saved in

```
output/
```
## Requirements
-sqlalchemy
-pandas
-matplotlib
-numpy

## Author
David-Mathew-V