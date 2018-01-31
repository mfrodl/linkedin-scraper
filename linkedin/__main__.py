#!/usr/bin/env python

import argparse
import sys
import os

from scrapy.crawler import CrawlerProcess
from linkedin.spiders import LinkedinSpider

# Constants
TOKEN_PATH = os.path.expanduser('~/.linkedin-access-token')
DESCRIPTION = (
    'Based on keywords defined by user, perform a LinkedIn query, extract '
    'user information from the first results page and store it to a CSV file'
)

def load_token():
    """ Load access token from file """
    try:
        with open(TOKEN_PATH) as f:
            token = f.read()
            return token
    except IOError:
        sys.stderr.write(
            'Please create file {0} containing a valid LinkedIn access '
            'token'.format(TOKEN_PATH) + os.linesep
        )
        sys.exit(1)

def parse_args():
    """ Process command-line arguments with argparse """
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        '-o', '--output',
        default='output.csv',
        metavar='FILE',
        help='output file (default: output.csv)',
    )
    parser.add_argument(
        'keyword',
        nargs='+',
        help='one or more keywords to search for',
    )
    return parser.parse_args()

def main():
    """ Main function """
    # Parse command-line arguments
    args = parse_args()
    keywords = ' '.join(args.keyword)

    # Load access token from file
    token = load_token()

    # Run scraper
    process = CrawlerProcess({'LOG_LEVEL': 'WARNING'})
    process.crawl(LinkedinSpider, token, keywords, args.output)
    process.start()

if __name__ == '__main__':
    main()

