import argparse
import logging
from googlesearch import search
from utils import save_results

def parse_arguments():
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments."
    parser = argparse.ArgumentParser(description="Google Dorking Tool")
    parser.add_argument('-q', '--query', action='append', required=True, help='Google Dork query to execute')
    parser.add_argument('-o', '--output', help='File to save the results to')
    return parser.parse_args()

def perform_google_dork(queries):
    """
    Perform Google Dorking with the given queries.

    Args:
        queries (list): List of Google Dork queries.

    Returns:
        list: List of search results.
    """
    results = []
    for query in queries:
        try:
            logging.info(f"Searching for: {query}")
            query_results = search(query, num_results=10)
            results.extend(query_results)
        except Exception as e:
            logging.error(f"Failed to search for {query}: {e}")
    return results

def main():
    """
    Main function to execute the Google Dorking tool.
    "
    args = parse_arguments()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    results = perform_google_dork(args.query)
    if args.output:
        save_results(results, args.output)
        logging.info(f"Results saved to {args.output}")
    else:
        for result in results:
            print(result)

if __name__ == "__main__":
    main()