import argparse
from ttp import ttp

# Set up argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--template', type=str, help='Add a template file name', required=True)
parser.add_argument('-i', '--inputFile', type=str, help='Add an input file name', required=True)
parser.add_argument('--dict', action='store_true', help='Print parsed entries as dictionaries instead of raw results')
args = parser.parse_args()

# Load the template
with open(args.template, 'r') as template_file:
    template = template_file.read()

# Load the input file data
with open(args.inputFile, 'r') as input_file:
    cli_data = input_file.read()

# Create TTP parser instance
parser = ttp(data=cli_data, template=template)

# Parse the data
parser.parse()

# Get the parsed results
results = parser.result()
# Print raw results without formatting
print(results[0])
