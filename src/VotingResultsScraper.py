from typing import List, Tuple

import requests
from bs4 import BeautifulSoup

site_root = 'http://www.electronicdancemusic.cz'


def scrap_top_100_awards_links() -> List[str]:
    all_awards_page_url = site_root + '/awards/top-100-dj-s'

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
            lambda link: site_root + link,
            awards_links
        )
    )


if __name__ == '__main__':
    top_100_awards_links = scrap_top_100_awards_links()

    print(top_100_awards_links)
