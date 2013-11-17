#!/usr/bin/python
# -*- coding: utf8 -*-

import web
from pyquery import PyQuery as pyq
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# -*- coding: utf-8 -*-

urls = (
    '/search', 'search',
    '/.*', 'search'
)


class search:
    def GET(self):
        path = web.ctx.fullpath
        url = r'http://dict.youdao.com' + path
        doc = pyq(url)
        doc('#custheme').remove()
        doc('.c-topbar').remove()
        doc('.c-subtopbar').remove()
        doc('.c-header').remove()
        doc('#c_footer').remove()
        doc('.c-bsearch').remove()
        doc('#ads').remove()
        doc('#rel-search').remove()
        doc('.error-wrapper').remove()
        doc('#topImgAd').remove()
        doc('#container').css('margin', '0')
        doc('#results-contents').css('width', '500px')
        doc('#results-contents').css('margin', '0')
        doc('#result_navigator').css('left', '550px')
        web.header('Content-Type', 'text/html; charset=utf-8', unique=True)
        return doc.outerHtml()


class index:
    def GET(self):
        path = web.ctx.fullpath
        raise web.redirect(r'http://dict.youdao.com' + path)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()
