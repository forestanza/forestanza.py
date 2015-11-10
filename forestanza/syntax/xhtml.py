SYNFMT = '<span class="fza {!s:s}">\\1</span>'
HLFMT = ".fza.{group:s} {{ color: {guifg:s}; }}\n"
COPTS = ['ctermfg', 'guifg', 'ctermbg', 'guibg']

import re


class SynGenXHTML:
    def __init__(self, dom):
        self._dom = dom
        self.origin = list(self.make_from(2))
        self.phonet = list(self.make_from(3))

    # WARNING: can't use dict, as I need fixed order on function calls!
    def pygment_origin(self, text):
        for r, s in self.origin:
            text = r.sub(s, text)
        return text

    def pygment_phonet(self, text):
        for r, s in self.phonet:
            text = r.sub(s, text)
        return text

    def make_from(self, idx):
        for entry in self._dom.data():
            rgx = ('|'.join(entry[idx])).replace('<', r'\b').replace('>', r'\b')
            print(rgx)
            if rgx:
                yield (re.compile('(' + rgx + ')'), SYNFMT.format(entry[1]))

    def colors(self):
        for grp, clr in sorted(self._dom.colors()):
            # WARNING: clr[1] -- out index! need dict!
            yield HLFMT.format(group=grp, guifg=clr[1])