# Google Dorking Tool

## Description
This tool performs Google Dorking, a technique used to search for specific information on the internet using advanced Google search operators. The tool allows users to specify search queries and outputs the results.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/google-dorking-tool.git
   cd google-dorking-tool
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Examples
1. Basic search:
   ```bash
   python main.py -q "site:example.com filetype:pdf"
   ```
2. Search with multiple queries:
   ```bash
   python main.py -q "site:example.com filetype:pdf" -q "site:example.com intitle:index.of"
   ```
3. Save results to a file:
   ```bash
   python main.py -q "site:example.com filetype:pdf" -o results.txt
   ```

## Options
- `-q, --query`: Google Dork query to execute. Can be specified multiple times.
- `-o, --output`: File to save the results to. If not specified, results are printed to the console.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.