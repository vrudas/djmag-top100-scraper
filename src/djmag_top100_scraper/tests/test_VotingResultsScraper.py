import os
import unittest

from djmag_top100_scraper.VotingResultsScraper import scrap_top_100_awards_links, scrap_top_100_djs_voting_results, \
    generate_file_name, scrap_all_voting_results

EXPECTED_TOP_100_AWARDS_LINKS = [
    'http://www.electronicdancemusic.cz/awards/top-100-dj-s/706-dj-mag-top-100-dj-s-2021',
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


class GenerateFileNameTestCase(unittest.TestCase):
    def test_generate_file_name(self):
        file_name = generate_file_name(
            'http://www.electronicdancemusic.cz/awards/top-100-dj-s/316-dj-mag-top-100-dj-s-1997'
        )

        self.assertEqual('dj-mag-top-100-djs-1997.csv', file_name)


@unittest.skip("This test should be run only for manual check, but not onn CI")
class ScrapAllVotingResultsTestCase(unittest.TestCase):
    def test_scrap_all_voting_results(self):
        scrap_all_voting_results()

        file_paths = [
            '../resources/dj-mag-top-100-djs-1997.csv',
            '../resources/dj-mag-top-100-djs-1998.csv',
            '../resources/dj-mag-top-100-djs-1999.csv',
            '../resources/dj-mag-top-100-djs-2000.csv',
            '../resources/dj-mag-top-100-djs-2001.csv',
            '../resources/dj-mag-top-100-djs-2002.csv',
            '../resources/dj-mag-top-100-djs-2003.csv',
            '../resources/dj-mag-top-100-djs-2004.csv',
            '../resources/dj-mag-top-100-djs-2005.csv',
            '../resources/dj-mag-top-100-djs-2006.csv',
            '../resources/dj-mag-top-100-djs-2007.csv',
            '../resources/dj-mag-top-100-djs-2008.csv',
            '../resources/dj-mag-top-100-djs-2009.csv',
            '../resources/dj-mag-top-100-djs-2010.csv',
            '../resources/dj-mag-top-100-djs-2011.csv',
            '../resources/dj-mag-top-100-djs-2012.csv',
            '../resources/dj-mag-top-100-djs-2013.csv',
            '../resources/dj-mag-top-100-djs-2014.csv',
            '../resources/dj-mag-top-100-djs-2015.csv',
            '../resources/dj-mag-top-100-djs-2016.csv',
            '../resources/dj-mag-top-100-djs-2017.csv',
            '../resources/dj-mag-top-100-djs-2018.csv',
            '../resources/dj-mag-top-100-djs-2019.csv',
            '../resources/dj-mag-top-100-djs-2020.csv',
            '../resources/dj-mag-top-100-djs-2021.csv',
        ]

        for file_path in file_paths:
            self.assertGreater(os.path.getsize(file_path), 0, 'File ' + file_path + ' is empty')


if __name__ == '__main__':
    unittest.main()
