def save_results(results, filename):
    """
    Save search results to a file.

    Args:
        results (list): List of search results.
        filename (str): Name of the file to save the results to.
    "try:
        with open(filename, 'w') as file:
            for result in results:
                file.write(result + '\n')
    except IOError as e:
        logging.error(f"Failed to write to file {filename}: {e}")