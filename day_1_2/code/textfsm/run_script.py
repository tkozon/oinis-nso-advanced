import textfsm
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--template', type=str, help='Add a template file name', required=True)
parser.add_argument('-i', '--inputFile', type=str, help='Add an input file name', required=True)
parser.add_argument('--dict', action='store_true', help='Print parsed entries as dictionaries instead of raw results')
args = parser.parse_args()

# Load the template
with open(args.template) as template:
    fsm = textfsm.TextFSM(template)

# Load the input file data
with open(args.inputFile) as file:
    cliData = file.read()

# Parse the CLI data
results = fsm.ParseText(cliData)
field_names = fsm.header

# Option to print parsed entries as dictionaries if --dict is provided
if args.dict:
    parsed_entries = [dict(zip(field_names, entry)) for entry in results]
    for entry in parsed_entries:
        print(entry)
else:
    for entry in results:
        print(entry)
