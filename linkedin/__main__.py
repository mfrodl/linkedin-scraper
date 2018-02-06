#!/usr/bin/env python

import argparse

from linkedin.spiders import LinkedinSpider
from scrapy.crawler import CrawlerProcess

# Constants
DESCRIPTION = (
    'Based on keywords defined by user, perform a LinkedIn query, extract '
    'user information from the first results page and store it to a CSV file'
)

def parse_args():
    """ Process command-line arguments with argparse """
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        '-o', '--output',
        default='output.csv',
        metavar='FILE',
        help='Output file (default: output.csv)',
    )
    parser.add_argument(
        '-u', '--user',
        help='LinkedIn user name'
    )
    parser.add_argument(
        '-p', '--password',
        help='LinkedIn password'
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

    # Run scraper
    process = CrawlerProcess({'LOG_LEVEL': 'WARNING'})
    process.crawl(
        LinkedinSpider, keywords, args.output, args.user, args.password
    )
    process.start()

if __name__ == '__main__':
    main()
