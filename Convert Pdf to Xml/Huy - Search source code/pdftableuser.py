#----------------------------------#
# Usage of PDFTable API            #
#----------------------------------#
import pdftables_api

c = pdftables_api.Client('ufm16gt0133n')
c.xml('input.pdf', 'output.xml')