from forestanza import io

EXT = '.xhtml'

TSEC = """
<h3 id="s{index:04d}">{index:04d}</h3>
<p class="main origin">
  {origin:s}
</p><p class="phonet">
  : {phonetics:s}
</p><p class="transl">
  ~ {translation:s}
</p><table class="table"><tbody>
{syntable:s}
</tbody></table><br/>
"""

TSYN = """<tr>
<td><span class="origin">{!s:s}</span></td>
<!-- <td><span class="phonet">{!s:s}</span></td> -->
<td>{!s:s}</td>
</tr>\n"""

import re

rgx_kana = re.compile(u"([\u3041-\u3096\u30A0-\u30FA]+)")

class Exporter:
    def __init__(self, **kw):
        self.metainfo = kw
        self.template = io.load_around(__file__, 'xhtml.xml')
        self.style = io.load_around(__file__, 'xhtml.css')
        self.sections = []

    def dump(self):
        self.metainfo.update({'css': self.style,
                              'sections': ''.join(self.sections)})
        return self.template.format(**self.metainfo)

    def p_hl(self, nm, rgb):
        self.style += ".{nm:s} { color: {rgb:s}; }\n".format(locals())

    def p_section(self, ind, sec):
        # DEV: cover 'sec' into colored 'span' syntax
        hl = r'<span class="syn">\1</span>'
        self.sections.append(TSEC.format(
            syntable=''.join([TSYN.format(*row) for row in sec.rows]),
            index=ind, origin=rgx_kana.sub(hl, sec.origin),
            phonetics=sec.phonetics, translation=sec.translation))
