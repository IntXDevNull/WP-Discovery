# WordPress Domain Checker

This Python script checks if a list of domains are built on WordPress by analyzing the content and headers returned by each domain. It can handle large lists of domains, log the results, and save the output to a file. 

## Features

- Detects if a site is built on WordPress by looking for WordPress-specific markers in HTML content and HTTP headers.
- Handles connection errors gracefully and logs the process.
- Supports input and output via files. Logic includes normalizing domain URL by adding "http://" if the domain, or domain list does not include this.
- Output can be used with for example https://github.com/rivsec/wordpress-rest-enum

## Requirements

- Python 3.x
- `requests` library

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/WordPressDomainChecker.git
   cd WordPressDomainChecker

## How to use
-d, --domains (required): Path to the file containing the list of domains to check.
-o, --output (optional): Path to the file where the results (WordPress sites) will be saved. If not specified, results will be saved to wordpress_sites.txt.
