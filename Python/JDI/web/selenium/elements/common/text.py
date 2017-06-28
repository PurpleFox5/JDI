import re

from JDI.web.selenium.elements.actions.waiter import waiter_decorator
from JDI.web.selenium.elements.base.element import Element

class Text(Element):

    def __init__(self, by_locator=None, web_element=None):
        super(Text, self).__init__(by_locator)

    def _get_text(self):
        el = self.get_web_element()
        res = el.get_attribute("value") if el.text in [None, ""] else el.text
        return "" if res is None else res

    def get_text(self):
        return self._get_text()

    def get_value(self):
        return self._get_text()

    @waiter_decorator
    def wait_match_text(self, reg_exp):
        return re.search(reg_exp, self._get_text()) != None

    @waiter_decorator
    def wait_contain_text(self, text):
        return self._get_text().find(text) != -1


