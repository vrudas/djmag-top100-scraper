import csv
import os
from typing import List

import requests
from bs4 import BeautifulSoup

from djmag_top100_scraper.DJVoteResult import DJVoteResult

SITE_ROOT = 'https://djmag.com/top100djs'
RESOURCES_DIR_PATH = '../resources'


def scrap_top_100_awards_links() -> List[str]:
    all_awards_page = requests.get(SITE_ROOT)

    all_awards_page_content = BeautifulSoup(
        all_awards_page.content,
        features='html.parser'
    )

    form_with_award_links = all_awards_page_content.find(id='edit-year')

    available_years = list(
        map(
            lambda option: option.text,
            form_with_award_links.contents
        )
    )

    awards_links = list(
        map(
            lambda year: f'{SITE_ROOT}/{year}',
            available_years
        )
    )

    return awards_links


def scrap_top_100_djs_voting_results(awards_link: str) -> List[DJVoteResult]:
    print('Scrap voting results for link: ' + awards_link)

    awards_page = requests.get(awards_link)

    awards_page_content = BeautifulSoup(
        awards_page.content,
        features="html.parser"
    )

    awards_year = extract_awards_year_from_link(awards_link)
    voting_result_lines = extract_voting_result_lines_from_page_content(
        awards_page_content,
        awards_year
    )

    dj_vote_results = map(
        lambda vote_result: DJVoteResult(
            vote_result[0],
            vote_result[1]
        ),
        voting_result_lines
    )

    return list(dj_vote_results)


def extract_voting_result_lines_from_page_content(awards_page_content, awards_year) -> List[tuple[int, str]]:
    voting_results_elements = awards_page_content.find_all(class_='top100dj-name')
    voting_results_link_elements = [element.find('a') for element in voting_results_elements]

    return list(
        map(
            lambda element: (
                element.attrs['href'].replace(f'/top100djs/{awards_year}/', '').split('/')[0],
                element.text.replace('\n', '')
            ),
            voting_results_link_elements
        )
    )


def generate_file_name(awards_link: str) -> str:
    awards_year = extract_awards_year_from_link(awards_link)
    return 'dj-mag-top-100-djs-' + awards_year + '.csv'


def extract_awards_year_from_link(awards_link):
    awards_year = awards_link[-4:]
    return awards_year


def save_scraped_voting_results_to_file(file_name: str, voting_results: List[DJVoteResult]):
    path_to_file = RESOURCES_DIR_PATH + '/' + file_name
    with open(path_to_file, mode='w') as results_file:
        results_writer = csv.writer(results_file, lineterminator=os.linesep)

        for vote_result in voting_results:
            vote_result_row = [vote_result.position, vote_result.dj_name]
            results_writer.writerow(vote_result_row)


def scrap_all_voting_results():
    top_100_awards_links = scrap_top_100_awards_links()

    print(len(top_100_awards_links), 'awards links will be scrapped')

    for awards_link in top_100_awards_links:
        scrapped_voting_results = scrap_top_100_djs_voting_results(awards_link)

        file_name = generate_file_name(awards_link)
        save_scraped_voting_results_to_file(file_name, scrapped_voting_results)


if __name__ == '__main__':
    scrap_all_voting_results()