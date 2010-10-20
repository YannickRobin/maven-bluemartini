<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="xml" indent="yes" version="1.0" omit-xml-declaration="no"/>
  <xsl:template match="/">
    <dna:dna xmlns="http://bluemartini.com/eng/arch/dna/name/"
             xmlns:dna="http://bluemartini.com/eng/arch/dna/type/"
             xmlns:bo="http://bluemartini.com/eng/arch/dna/type/bo/">
      <dna:boarray name="CART_TOTALS">
      <dna:bo botype="CART_ITEM">
	    <xsl:choose>
              <xsl:when test="configuration/P[.!='']">
            	<dna:currency name="salePriceAmt"><xsl:value-of select="configuration/P"/></dna:currency>
                <dna:currency name="priceOverrideAmt"><xsl:value-of select="configuration/P"/></dna:currency>
	      </xsl:when>
              <xsl:otherwise>
                <dna:currency name="salePriceAmt">0</dna:currency>
            	<dna:currency name="priceOverrideAmt">0</dna:currency>
              </xsl:otherwise>
	     </xsl:choose>
	    <dna:string name="ATR_resource_power"><xsl:value-of select="configuration/PW"/></dna:string>
	    <dna:string name="ATR_idm_selections"><xsl:value-of select="configuration/idmselections"/></dna:string>
	        
      </dna:bo>
      </dna:boarray>
      <dna:boarray name="ADD_CART_ITEM_ARRAY">
        <xsl:for-each select="configuration/part">
          <dna:bo botype="CART_ITEM">
            <dna:string name="skuCode"><xsl:value-of select="partno"/></dna:string>
            <dna:string name="longDesc"><xsl:value-of select="description"/></dna:string>
            <xsl:choose>
              <xsl:when test="qty[.!='']">
                <dna:integer name="qtyToBuy"><xsl:value-of select="qty"/></dna:integer>
              </xsl:when>
              <xsl:otherwise>
                <dna:integer name="qtyToBuy">1</dna:integer>
              </xsl:otherwise>
            </xsl:choose>
	     <xsl:choose>
              <xsl:when test="P[.!='']">
            	<dna:currency name="salePriceAmt"><xsl:value-of select="P"/></dna:currency>
            	<dna:currency name="priceOverrideAmt"><xsl:value-of select="P"/></dna:currency>
	      </xsl:when>
              <xsl:otherwise>
                <dna:currency name="salePriceAmt">0</dna:currency>
            	<dna:currency name="priceOverrideAmt">0</dna:currency>
              </xsl:otherwise>
	     </xsl:choose>
	    <dna:string name="ATR_resource_power"><xsl:value-of select="PW"/></dna:string>
          </dna:bo>
        </xsl:for-each>
      </dna:boarray>
    </dna:dna>
  </xsl:template>
</xsl:stylesheet>
