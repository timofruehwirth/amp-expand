<xsl:stylesheet 
    xmlns="http://www.w3.org/1999/xhtml"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:tei="http://www.tei-c.org/ns/1.0"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="#all" version="2.0"><!-- root element declaring document to be an XSL style sheet and pointing to W3C XSLT namespace; also pointing to TEI namespace; third, `xmlns="http://www.w3.org/1999/xhtml"` is default xhtml namespace -->
    <xsl:output encoding="UTF-8" media-type="text/html" method="xhtml" version="1.0" indent="yes" omit-xml-declaration="yes"/>
   
   <xsl:template match="/"><!-- `match="/"` associates the template with the root of the XML source doc = the entire XML doc -->
       <html xmlns="http://www.w3.org/1999/xhtml">
           <head>
               <title><xsl:value-of select="//tei:title"/></title><!-- `//` indicates longer path; so, this is short for `tei:TEI/tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title` -->
           </head>
           <body>
               <xsl:apply-templates select="//tei:div"/>
           </body>
       </html>
   </xsl:template>
   
    <xsl:template match="tei:div">
        <div><xsl:apply-templates/></div><!-- 2nd step: `<xsl:apply-templates/>` makes transformation process look for further templates at lower levels  -->
    </xsl:template>
    
    <xsl:template match="tei:ab"><!-- 3rd step: `<xsl:template match="tei:ab">`, `<xsl:template match="tei:p">` and `<xsl:template match="tei:lb">` applied -->
        <p><xsl:apply-templates/></p>
    </xsl:template>
    
    <xsl:template match="tei:p">
        <p><xsl:apply-templates/></p>
    </xsl:template>
    
    <xsl:template match="tei:lb">
        <br />
    </xsl:template>
    
</xsl:stylesheet>