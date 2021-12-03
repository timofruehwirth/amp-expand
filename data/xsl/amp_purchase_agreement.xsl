<?xml version="1.0" encoding="UTF-8"?><!-- XML declaration -->
<xsl:stylesheet version="2.0"
xmlns:tei="http://www.tei-c.org/ns/1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"><!-- root element declaring document to be an XSL style sheet and pointing to W3C XSLT namespace; also pointing to TEI namespace -->
   
   <xsl:template match="/"><!-- `match="/"` associates the template with the root of the XML source doc = the entire XML doc -->
       <html xmlns="http://www.w3.org/1999/xhtml">
           <head>
               <title><xsl:value-of select="//tei:title"/></title><!-- `//` indicates longer path; so, this is short for `tei:TEI/tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title` -->
           </head>
           <body>
               <h1><xsl:value-of select="//tei:head"/></h1><!-- if there are several `head` elements: `tei:head[1]` addresses only first `head`, `tei:head[last()] addresses only last `head` etc. -->
           </body>
       </html>
   </xsl:template>
   
</xsl:stylesheet>