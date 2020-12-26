import re
from typing import List

import requests
from bs4 import BeautifulSoup

from DJVoteResult import DJVoteResult

SITE_ROOT = 'http://www.electronicdancemusic.cz'


def scrap_top_100_awards_links() -> List[str]:
    all_awards_page_url = SITE_ROOT + '/awards/top-100-dj-s'

    all_awards_page = requests.get(all_awards_page_url)

    all_awards_page_content = BeautifulSoup(
        all_awards_page.content,
        features='html.parser'
    )

    form_with_award_links = all_awards_page_content.find(id='adminForm')

    link_elements = form_with_award_links.find_all('a')

    hrefs = list(
        map(
            lambda link_element: link_element['href'],
            link_elements
        )
    )

    awards_links = list(filter(lambda href: href.startswith('/awards'), hrefs))

    return list(
        map(
            lambda link: SITE_ROOT + link,
            awards_links
        )
    )


def scrap_top_100_djs_voting_results(awards_link: str) -> List[DJVoteResult]:
    print('Scrap voting results for link:' + awards_link)

    awards_page = requests.get(awards_link)

    awards_page_content = BeautifulSoup(
        awards_page.content,
        features="html.parser"
    )

    voting_results_element = awards_page_content.find(class_='art-article')
    voting_result_lines = voting_results_element.find_all(text=re.compile('\\d+\\.\\s'))

    split_vote_result_lines = map(
        lambda result_line: re.split('\\.\\s', result_line),
        voting_result_lines
    )

    dj_vote_results = map(
        lambda vote_result: DJVoteResult(
            vote_result[0],
            vote_result[1]
        ),
        split_vote_result_lines
    )

    return list(dj_vote_results)


if __name__ == '__main__':
    top_100_awards_links = scrap_top_100_awards_links()

    print(top_100_awards_links)
