import requests
import argparse
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)

# Function to check if a site is built on WordPress
def is_wordpress_site(domain):
    try:
        # Normalize domain URL
        if not domain.startswith("http://") and not domain.startswith("https://"):
            domain = "http://" + domain

        response = requests.get(domain, timeout=10)

        # Check the response headers and body for signs of WordPress
        headers = response.headers
        content = response.text

        if 'wp-content' in content or 'wp-includes' in content:
            return True
        if 'X-Powered-By' in headers and 'WordPress' in headers['X-Powered-By']:
            return True
        if 'Link' in headers and 'https://api.w.org/' in headers['Link']:
            return True
        return False

    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to connect to {domain}: {e}")
        return False

# Function to validate domains from a list
def validate_wordpress_sites(domain_list):
    wordpress_sites = []

    for domain in domain_list:
        logging.info(f"Checking {domain}...")
        if is_wordpress_site(domain):
            logging.info(f"{domain} is built on WordPress.")
            wordpress_sites.append(domain)
        else:
            logging.info(f"{domain} is not built on WordPress.")

    return wordpress_sites

# Main function to handle input and output
def main():
    parser = argparse.ArgumentParser(description="Validate if domains are built on WordPress.")
    parser.add_argument("-d", "--domains", type=str, help="File containing list of domains", required=True)
    parser.add_argument("-o", "--output", type=str, help="Output file for WordPress sites", required=False)

    args = parser.parse_args()

    # Read domains from the input file
    with open(args.domains, 'r') as file:
        domain_list = [line.strip() for line in file.readlines()]

    # Validate domains and get the list of WordPress sites
    wordpress_sites = validate_wordpress_sites(domain_list)

    # Determine the output file name
    if args.output:
        output_file = args.output
    else:
        output_file = 'wordpress_sites.txt'

    # Ensure the output file has a .txt extension
    if not output_file.endswith('.txt'):
        output_file += '.txt'

    # Write the WordPress sites to the output file
    with open(output_file, 'w') as outfile:
        outfile.write("\n".join(wordpress_sites) + "\n")

    logging.info(f"WordPress sites found: {len(wordpress_sites)}")
    logging.info(f"Results written to {output_file}")

if __name__ == "__main__":
    main()
