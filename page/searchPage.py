from page.basePage import Page
import urllib.parse
from utils.GetYaml import getyaml
from config import setting


def charParser(keyword):
    '''
    中文关键字转换为urlencoded
    '''
    name = urllib.parse.quote(keyword)
    return name.replace('%', '%25')


class searchPage(Page):
    elementData = getyaml(setting.TEST_Element_YAML + '/' + 'search.yaml')

    def __init__(self, driver, keyword):
        super().__init__(driver)
        self.url = '/nForum/#!s/board?b=' + charParser(keyword)
        self.results = self.elementData.get_element_from_data(0)

    def get_search_results(self):
        return self.find_elements(*self.results)

