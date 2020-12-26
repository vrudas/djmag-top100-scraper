import unittest

from src.VotingResultsScraper import scrap_top_100_awards_links, scrap_top_100_djs_voting_results

EXPECTED_TOP_100_AWARDS_LINKS = [
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/672-dj-mag-top-100-dj-s-2020',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/578-dj-mag-top-100-dj-s-2019',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/464-dj-mag-top-100-dj-s-2018',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/214-dj-mag-top-100-dj-s-2017',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/18-dj-mag-top-100-dj-s-2016',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/62-dj-mag-top-100-dj-s-2015',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/65-dj-mag-top-100-dj-s-2014',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/64-dj-mag-top-100-dj-s-2013',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/335-dj-mag-top-100-dj-s-2012',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/334-dj-mag-top-100-dj-s-2011',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/333-dj-mag-top-100-dj-s-2010',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/332-dj-mag-top-100-dj-s-2009',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/331-dj-mag-top-100-dj-s-2008',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/330-dj-mag-top-100-dj-s-2007',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/329-dj-mag-top-100-dj-s-2006',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/328-dj-mag-top-100-dj-s-2005',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/327-dj-mag-top-100-dj-s-2004',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/326-dj-mag-top-100-dj-s-2003',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/321-dj-mag-top-100-dj-s-2002',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/320-dj-mag-top-100-dj-s-2001',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/319-dj-mag-top-100-dj-s-2000',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/318-dj-mag-top-100-dj-s-1999',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/317-dj-mag-top-100-dj-s-1998',
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/316-dj-mag-top-100-dj-s-1997',
]


class ScrapAwardsLinksTestCase(unittest.TestCase):
    def test_scrap_top_100_awards_links(self):
        top_100_awards_links = scrap_top_100_awards_links()

        self.assertEqual(EXPECTED_TOP_100_AWARDS_LINKS, top_100_awards_links)


class ScrapTop100DJsVoteResultsTestCase(unittest.TestCase):
    def test_scrap_top_100_djs_voting_results(self):
        for awards_link in EXPECTED_TOP_100_AWARDS_LINKS:
            scrapped_voting_results = scrap_top_100_djs_voting_results(awards_link)
            scrapped_djs_count = len(scrapped_voting_results)

            self.assertEqual(100, scrapped_djs_count, 'Failed to scrap voting results for link:' + awards_link)


if __name__ == '__main__':
    unittest.main()
