# https://untangle.readthedocs.io/en/latest/
# https://github.com/stchris/untangle
import untangle
import mycsv

xmltxt = mycsv.getdata()

xml = untangle.parse(xmltxt)
