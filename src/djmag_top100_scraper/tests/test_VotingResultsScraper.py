import os
import unittest

from djmag_top100_scraper.VotingResultsScraper import scrap_top_100_awards_links, scrap_top_100_djs_voting_results, \
    generate_file_name, scrap_all_voting_results

EXPECTED_TOP_100_AWARDS_LINKS = [
    'https://djmag.com/top100djs/2004',
    'https://djmag.com/top100djs/2005',
    'https://djmag.com/top100djs/2006',
    'https://djmag.com/top100djs/2007',
    'https://djmag.com/top100djs/2008',
    'https://djmag.com/top100djs/2009',
    'https://djmag.com/top100djs/2010',
    'https://djmag.com/top100djs/2011',
    'https://djmag.com/top100djs/2012',
    'https://djmag.com/top100djs/2013',
    'https://djmag.com/top100djs/2014',
    'https://djmag.com/top100djs/2015',
    'https://djmag.com/top100djs/2016',
    'https://djmag.com/top100djs/2017',
    'https://djmag.com/top100djs/2018',
    'https://djmag.com/top100djs/2019',
    'https://djmag.com/top100djs/2020',
    'https://djmag.com/top100djs/2021',
    'https://djmag.com/top100djs/2022',
    'https://djmag.com/top100djs/2023'
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

            if awards_link.__contains__('2004'):
                self.assert_awards(awards_link, scrapped_djs_count, 64)
            elif awards_link.__contains__('2007'):
                self.assert_awards(awards_link, scrapped_djs_count, 96)
            else:
                self.assert_awards(awards_link, scrapped_djs_count)

    def assert_awards(self, awards_link, scrapped_djs_count, expected_djs_count=100):
        self.assertEqual(expected_djs_count, scrapped_djs_count, 'Failed to scrap voting results for link:' + awards_link)


class GenerateFileNameTestCase(unittest.TestCase):
    def test_generate_file_name(self):
        file_name = generate_file_name(
            'https://www.electronicdancemusic.cz/awards/top-100-djs/dj-mag-top-100-djs-1997'
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
            # '../resources/dj-mag-top-100-djs-2013.csv', # Not exists anymore on SITE
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
