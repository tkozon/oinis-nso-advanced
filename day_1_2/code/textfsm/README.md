# How to Run the TextFSM Parsing Script

This guide explains how to run the provided TextFSM parsing script using input parameters.

## Prerequisites

Ensure you have the following installed:
- Python 3.9 or later
- The `textfsm` Python module

Install `textfsm` if not already installed:

```bash
pip install textfsm
```

## Running the Script

The script can be run with the following command:

```bash
python run_script.py -t <template_file> -i <input_file> [--dict]
```

### Parameters

- `-t` or `--template`: (Required) The path to the TextFSM template file.
- `-i` or `--inputFile`: (Required) The path to the input file containing the CLI data to parse.
- `--dict`: (Optional) If provided, outputs the parsed data as dictionaries.

### Example Usage

#### Example Input File (`input.txt`)

```
Interface          Status
GigabitEthernet1   up
GigabitEthernet2   down
```

#### Example Template File (`template.txt`)

```
Value INTERFACE (\S+)
Value STATUS (\S+)

Start
  ^${INTERFACE}\s+${STATUS} -> Record
```

#### Running the Script

Command:

```bash
python script.py -t template.txt -i input.txt
```

Output:

```
['GigabitEthernet1', 'up']
['GigabitEthernet2', 'down']
```

#### Using the `--dict` Option

Command:

```bash
python script.py -t template.txt -i input.txt --dict
```

Output:

```
{'INTERFACE': 'GigabitEthernet1', 'STATUS': 'up'}
{'INTERFACE': 'GigabitEthernet2', 'STATUS': 'down'}
```

## Notes

- Ensure the template file matches the format of your input data.
- The input file should contain CLI data that adheres to the template specifications.
