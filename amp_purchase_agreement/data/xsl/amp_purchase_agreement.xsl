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
                <link href="../css/amp_purchase_agreement.css" type="text/css" rel="stylesheet"></link>
                <title><xsl:value-of select="//tei:title"/></title><!-- `//` indicates longer path; so, this is short for `tei:TEI/tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title` -->
                <link rel="icon" type="image/x-icon" href="https://amp.acdh.oeaw.ac.at/images/Auden_Musulin_Papers_Logo_rechteckig_web.png" />
                <meta name="description">
                    <xsl:attribute name="content">
                        <xsl:value-of select="//tei:titleStmt/tei:title"/>
                    </xsl:attribute>
                </meta>
                <meta name="date of origin">
                    <xsl:attribute name="content">
                        <xsl:value-of select="//tei:origin/tei:origDate/@when-iso"/>
                    </xsl:attribute>
                </meta>    
                <meta name="date of publication">
                    <xsl:attribute name="content">
                        <xsl:value-of select="//tei:publicationStmt/tei:date/@when-iso"/>
                    </xsl:attribute>
                </meta>
                <meta name="author">
                    <xsl:attribute name="content">
                        <xsl:value-of select="//tei:respStmt/tei:name"/>
                    </xsl:attribute>
                </meta>
            </head>
            <body>
                <nav>
                    <ul>
                        <li>
                            <a href="https://amp.acdh.oeaw.ac.at/index.html">
                                <img src="https://amp.acdh.oeaw.ac.at/images/Auden_Musulin_Papers_Logo_rechteckig_web.png" title="Auden Musulin Papers Logo" alt="Auden Musulin Papers Logo" class="navbar_img" />
                            </a>
                        </li>
                        <li>
                            <span id="header"><xsl:value-of select="//tei:title"/></span>
                        </li>
                    </ul>
                </nav>
                <xsl:apply-templates select="tei:TEI/tei:text/tei:body/tei:div"/><!-- 1st step: this path targets the highest-level `div` element -->
            </body>
        </html>
    </xsl:template>
   
    <!--<xsl:template match="tei:div">
        <div><xsl:apply-templates/></div>
    </xsl:template>-->
    
    <xsl:template match="tei:div">
        <!--<xsl:choose>
            <xsl:when test="@type='addition'">-->
                <div><xsl:attribute name="class"><xsl:value-of select="data(@type)"/></xsl:attribute><xsl:apply-templates/></div><!-- 2nd step: `<xsl:apply-templates/>` makes transformation process look for further templates at lower levels  -->
            <!--</xsl:when>
            <xsl:otherwise>
                <div><xsl:apply-templates/></div>
            </xsl:otherwise>
        </xsl:choose>-->
    </xsl:template>
    
    <xsl:template match="tei:ab"><!-- 3rd step: `<xsl:template match="tei:ab">`, `<xsl:template match="tei:p">`, `<xsl:template match="tei:lb">`, etc. applied -->
        <p><xsl:apply-templates/></p>
    </xsl:template>
    
    <xsl:template match="tei:p">
        <p><xsl:apply-templates/></p>
    </xsl:template>
    
    <xsl:template match="tei:lb">
        <br />
    </xsl:template>
    
    <xsl:template match="tei:sic">
        <span><xsl:attribute name="class">tooltip</xsl:attribute><xsl:apply-templates/></span>
    </xsl:template>
    
    <xsl:template match="tei:note">
        <span><xsl:attribute name="class">tooltiptext</xsl:attribute><xsl:apply-templates/></span>
    </xsl:template>
    
    <xsl:template match="tei:head">
        <div><xsl:attribute name="class"><xsl:value-of select="data(@rend)"/></xsl:attribute><xsl:apply-templates/></div>
    </xsl:template>
    
    <xsl:template match="tei:space">
        <xsl:value-of select="string-join((for $i in 1 to @quantity return '&#x00A0;'),'')"/>
    </xsl:template>
    <!-- replacing this earlier, less simple solution:
        <xsl:template match="tei:space">
            <xsl:choose>
                <xsl:when test="@quantity='1'">&#x00A0;</xsl:when>
                <xsl:when test="@quantity='2'">&#x00A0;&#x00A0;</xsl:when>
            </xsl:choose>
        </xsl:template>
    -->
    
    <xsl:template match="tei:del">
        <del><xsl:apply-templates/></del>
    </xsl:template>
    
    <xsl:template match="tei:unclear">
        <abbr title="unclear"><xsl:apply-templates/></abbr>
    </xsl:template>
    
    <xsl:template match="tei:gap">
        <xsl:choose>
            <xsl:when test="@reason='deleted'">
                <del><abbr><xsl:attribute name="title"><xsl:value-of select="data(@reason)"/></xsl:attribute>[<xsl:apply-templates/>]</abbr></del>  
            </xsl:when>
            <xsl:when test="@reason='illegible'">
                <abbr><xsl:attribute name="title"><xsl:value-of select="data(@reason)"/></xsl:attribute>[<xsl:apply-templates/>]</abbr>
            </xsl:when>
        </xsl:choose>
    </xsl:template>
    
    <xsl:template match="tei:pb">
        <hr />
    </xsl:template>
    
</xsl:stylesheet>