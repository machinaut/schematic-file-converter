<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="5.91">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="15" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="6" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="no"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="allegro">
<description>&lt;b&gt;Allegro MicroSystems, Inc&lt;/b&gt;&lt;p&gt;
www.allegromicro.com&lt;br&gt;
&lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
<package name="QFN20">
<description>&lt;b&gt;ES Package, 20-Contact QFN with Exposed Thermal Pad&lt;/b&gt;&lt;p&gt;
&lt;a href="http://www.allegromicro.com/en/Products/Part_Numbers/3906/3906.pdf"&gt; Data sheet &lt;/a&gt;</description>
<wire x1="-1.8984" y1="-1.8984" x2="1.8984" y2="-1.8984" width="0.2032" layer="51"/>
<wire x1="1.8984" y1="-1.8984" x2="1.8984" y2="1.8984" width="0.2032" layer="51"/>
<wire x1="1.8984" y1="1.8984" x2="-1.8984" y2="1.8984" width="0.2032" layer="51"/>
<wire x1="-1.8984" y1="1.8984" x2="-1.8984" y2="-1.8984" width="0.2032" layer="51"/>
<wire x1="-1.8984" y1="1.8984" x2="-1.8984" y2="1.3016" width="0.2032" layer="21"/>
<wire x1="-1.3016" y1="1.8984" x2="-1.8984" y2="1.8984" width="0.2032" layer="21"/>
<wire x1="-1.8984" y1="-1.8984" x2="-1.3016" y2="-1.8984" width="0.2032" layer="21"/>
<wire x1="-1.8984" y1="-1.3016" x2="-1.8984" y2="-1.8984" width="0.2032" layer="21"/>
<wire x1="1.8984" y1="-1.8984" x2="1.8984" y2="-1.3016" width="0.2032" layer="21"/>
<wire x1="1.3016" y1="-1.8984" x2="1.8984" y2="-1.8984" width="0.2032" layer="21"/>
<wire x1="1.8984" y1="1.8984" x2="1.3016" y2="1.8984" width="0.2032" layer="21"/>
<wire x1="1.8984" y1="1.3016" x2="1.8984" y2="1.8984" width="0.2032" layer="21"/>
<smd name="1" x="-2.05" y="1" dx="0.95" dy="0.3" layer="1" stop="no" cream="no"/>
<smd name="2" x="-2.05" y="0.5" dx="0.95" dy="0.3" layer="1" stop="no" cream="no"/>
<smd name="3" x="-2.05" y="0" dx="0.95" dy="0.3" layer="1" stop="no" cream="no"/>
<smd name="4" x="-2.05" y="-0.5" dx="0.95" dy="0.3" layer="1" stop="no" cream="no"/>
<smd name="5" x="-2.05" y="-1" dx="0.95" dy="0.3" layer="1" stop="no" cream="no"/>
<smd name="EXP" x="0" y="0" dx="2.45" dy="2.45" layer="1" stop="no" cream="no"/>
<smd name="6" x="-1" y="-2.05" dx="0.95" dy="0.3" layer="1" rot="R90" stop="no" cream="no"/>
<smd name="7" x="-0.5" y="-2.05" dx="0.95" dy="0.3" layer="1" rot="R90" stop="no" cream="no"/>
<smd name="8" x="0" y="-2.05" dx="0.95" dy="0.3" layer="1" rot="R90" stop="no" cream="no"/>
<smd name="9" x="0.5" y="-2.05" dx="0.95" dy="0.3" layer="1" rot="R90" stop="no" cream="no"/>
<smd name="10" x="1" y="-2.05" dx="0.95" dy="0.3" layer="1" rot="R90" stop="no" cream="no"/>
<smd name="11" x="2.05" y="-1" dx="0.95" dy="0.3" layer="1" rot="R180" stop="no" cream="no"/>
<smd name="12" x="2.05" y="-0.5" dx="0.95" dy="0.3" layer="1" rot="R180" stop="no" cream="no"/>
<smd name="13" x="2.05" y="0" dx="0.95" dy="0.3" layer="1" rot="R180" stop="no" cream="no"/>
<smd name="14" x="2.05" y="0.5" dx="0.95" dy="0.3" layer="1" rot="R180" stop="no" cream="no"/>
<smd name="15" x="2.05" y="1" dx="0.95" dy="0.3" layer="1" rot="R180" stop="no" cream="no"/>
<smd name="16" x="1" y="2.05" dx="0.95" dy="0.3" layer="1" rot="R270" stop="no" cream="no"/>
<smd name="17" x="0.5" y="2.05" dx="0.95" dy="0.3" layer="1" rot="R270" stop="no" cream="no"/>
<smd name="18" x="0" y="2.05" dx="0.95" dy="0.3" layer="1" rot="R270" stop="no" cream="no"/>
<smd name="19" x="-0.5" y="2.05" dx="0.95" dy="0.3" layer="1" rot="R270" stop="no" cream="no"/>
<smd name="20" x="-1" y="2.05" dx="0.95" dy="0.3" layer="1" rot="R270" stop="no" cream="no"/>
<text x="-2.5" y="3" size="1.27" layer="25">&gt;NAME</text>
<text x="-2.5" y="-4" size="1.27" layer="27">&gt;VALUE</text>
<rectangle x1="-2.575" y1="0.825" x2="-1.525" y2="1.175" layer="29"/>
<rectangle x1="-2.5" y1="0.875" x2="-1.6" y2="1.125" layer="31"/>
<rectangle x1="-2.575" y1="0.325" x2="-1.525" y2="0.675" layer="29"/>
<rectangle x1="-2.5" y1="0.375" x2="-1.6" y2="0.625" layer="31"/>
<rectangle x1="-2.575" y1="-0.175" x2="-1.525" y2="0.175" layer="29"/>
<rectangle x1="-2.5" y1="-0.125" x2="-1.6" y2="0.125" layer="31"/>
<rectangle x1="-2.575" y1="-0.675" x2="-1.525" y2="-0.325" layer="29"/>
<rectangle x1="-2.5" y1="-0.625" x2="-1.6" y2="-0.375" layer="31"/>
<rectangle x1="-2.575" y1="-1.175" x2="-1.525" y2="-0.825" layer="29"/>
<rectangle x1="-2.5" y1="-1.125" x2="-1.6" y2="-0.875" layer="31"/>
<rectangle x1="-1.525" y1="-2.225" x2="-0.475" y2="-1.875" layer="29" rot="R90"/>
<rectangle x1="-1.45" y1="-2.175" x2="-0.55" y2="-1.925" layer="31" rot="R90"/>
<rectangle x1="-1.025" y1="-2.225" x2="0.025" y2="-1.875" layer="29" rot="R90"/>
<rectangle x1="-0.95" y1="-2.175" x2="-0.05" y2="-1.925" layer="31" rot="R90"/>
<rectangle x1="-0.525" y1="-2.225" x2="0.525" y2="-1.875" layer="29" rot="R90"/>
<rectangle x1="-0.45" y1="-2.175" x2="0.45" y2="-1.925" layer="31" rot="R90"/>
<rectangle x1="-0.025" y1="-2.225" x2="1.025" y2="-1.875" layer="29" rot="R90"/>
<rectangle x1="0.05" y1="-2.175" x2="0.95" y2="-1.925" layer="31" rot="R90"/>
<rectangle x1="0.475" y1="-2.225" x2="1.525" y2="-1.875" layer="29" rot="R90"/>
<rectangle x1="0.55" y1="-2.175" x2="1.45" y2="-1.925" layer="31" rot="R90"/>
<rectangle x1="1.525" y1="-1.175" x2="2.575" y2="-0.825" layer="29" rot="R180"/>
<rectangle x1="1.6" y1="-1.125" x2="2.5" y2="-0.875" layer="31" rot="R180"/>
<rectangle x1="1.525" y1="-0.675" x2="2.575" y2="-0.325" layer="29" rot="R180"/>
<rectangle x1="1.6" y1="-0.625" x2="2.5" y2="-0.375" layer="31" rot="R180"/>
<rectangle x1="1.525" y1="-0.175" x2="2.575" y2="0.175" layer="29" rot="R180"/>
<rectangle x1="1.6" y1="-0.125" x2="2.5" y2="0.125" layer="31" rot="R180"/>
<rectangle x1="1.525" y1="0.325" x2="2.575" y2="0.675" layer="29" rot="R180"/>
<rectangle x1="1.6" y1="0.375" x2="2.5" y2="0.625" layer="31" rot="R180"/>
<rectangle x1="1.525" y1="0.825" x2="2.575" y2="1.175" layer="29" rot="R180"/>
<rectangle x1="1.6" y1="0.875" x2="2.5" y2="1.125" layer="31" rot="R180"/>
<rectangle x1="0.475" y1="1.875" x2="1.525" y2="2.225" layer="29" rot="R270"/>
<rectangle x1="0.55" y1="1.925" x2="1.45" y2="2.175" layer="31" rot="R270"/>
<rectangle x1="-0.025" y1="1.875" x2="1.025" y2="2.225" layer="29" rot="R270"/>
<rectangle x1="0.05" y1="1.925" x2="0.95" y2="2.175" layer="31" rot="R270"/>
<rectangle x1="-0.525" y1="1.875" x2="0.525" y2="2.225" layer="29" rot="R270"/>
<rectangle x1="-0.45" y1="1.925" x2="0.45" y2="2.175" layer="31" rot="R270"/>
<rectangle x1="-1.025" y1="1.875" x2="0.025" y2="2.225" layer="29" rot="R270"/>
<rectangle x1="-0.95" y1="1.925" x2="-0.05" y2="2.175" layer="31" rot="R270"/>
<rectangle x1="-1.525" y1="1.875" x2="-0.475" y2="2.225" layer="29" rot="R270"/>
<rectangle x1="-1.45" y1="1.925" x2="-0.55" y2="2.175" layer="31" rot="R270"/>
<polygon width="0.15" layer="29">
<vertex x="-1.2" y="0.95" curve="87.140274"/>
<vertex x="-0.95" y="1.2"/>
<vertex x="1.2" y="1.2"/>
<vertex x="1.2" y="-1.2"/>
<vertex x="-1.2" y="-1.2"/>
</polygon>
<polygon width="0.15" layer="31">
<vertex x="-1.075" y="0.875" curve="56.144974"/>
<vertex x="-0.875" y="1.075"/>
<vertex x="1.075" y="1.075"/>
<vertex x="1.075" y="-1.075"/>
<vertex x="-1.075" y="-1.075"/>
</polygon>
</package>
</packages>
<symbols>
<symbol name="A3906">
<wire x1="-10.16" y1="15.24" x2="10.16" y2="15.24" width="0.254" layer="94"/>
<wire x1="10.16" y1="15.24" x2="10.16" y2="-25.4" width="0.254" layer="94"/>
<wire x1="10.16" y1="-25.4" x2="-10.16" y2="-25.4" width="0.254" layer="94"/>
<wire x1="-10.16" y1="-25.4" x2="-10.16" y2="15.24" width="0.254" layer="94"/>
<text x="-10.16" y="16.51" size="1.778" layer="95" font="vector">&gt;NAME</text>
<text x="-10.16" y="-27.94" size="1.778" layer="96" font="vector">&gt;VALUE</text>
<pin name="IN1" x="-12.7" y="-2.54" length="short" direction="in"/>
<pin name="IN2" x="-12.7" y="-5.08" length="short" direction="in"/>
<pin name="IN3" x="-12.7" y="-7.62" length="short" direction="in"/>
<pin name="IN4" x="-12.7" y="-10.16" length="short" direction="in"/>
<pin name="OUT1A" x="12.7" y="-2.54" length="short" direction="out" rot="R180"/>
<pin name="OUT1B" x="12.7" y="-5.08" length="short" direction="out" rot="R180"/>
<pin name="OUT2A" x="12.7" y="-12.7" length="short" direction="out" rot="R180"/>
<pin name="OUT2B" x="12.7" y="-15.24" length="short" direction="out" rot="R180"/>
<pin name="GND" x="-12.7" y="-22.86" length="short" direction="pwr"/>
<pin name="VBB" x="-12.7" y="12.7" length="short" direction="pwr"/>
<pin name="EXP" x="12.7" y="-22.86" length="short" direction="pas" rot="R180"/>
<pin name="!SLEEP" x="-12.7" y="2.54" length="short" direction="in"/>
<pin name="FL1" x="-12.7" y="-15.24" length="short" direction="in"/>
<pin name="FL2" x="-12.7" y="-17.78" length="short" direction="in"/>
<pin name="SENSE1" x="12.7" y="-7.62" length="short" direction="in" rot="R180"/>
<pin name="SENSE2" x="12.7" y="-17.78" length="short" direction="in" rot="R180"/>
<pin name="VCP" x="-12.7" y="7.62" length="short" direction="pas"/>
<pin name="CP1" x="12.7" y="12.7" length="short" direction="pas" rot="R180"/>
<pin name="CP2" x="12.7" y="10.16" length="short" direction="pas" rot="R180"/>
<pin name="CP3" x="12.7" y="5.08" length="short" direction="pas" rot="R180"/>
<pin name="CP4" x="12.7" y="2.54" length="short" direction="pas" rot="R180"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="A3906" prefix="IC">
<description>&lt;b&gt;Low Voltage Stepper and Single/Dual DC Motor Driver&lt;/b&gt;&lt;p&gt;
&lt;a href="http://www.allegromicro.com/en/Products/Part_Numbers/3906/3906.pdf"&gt; Data Sheet &lt;/a&gt;</description>
<gates>
<gate name="G$1" symbol="A3906" x="0" y="0"/>
</gates>
<devices>
<device name="" package="QFN20">
<connects>
<connect gate="G$1" pin="!SLEEP" pad="3"/>
<connect gate="G$1" pin="CP1" pad="19"/>
<connect gate="G$1" pin="CP2" pad="1"/>
<connect gate="G$1" pin="CP3" pad="18"/>
<connect gate="G$1" pin="CP4" pad="20"/>
<connect gate="G$1" pin="EXP" pad="EXP"/>
<connect gate="G$1" pin="FL1" pad="8"/>
<connect gate="G$1" pin="FL2" pad="9"/>
<connect gate="G$1" pin="GND" pad="2"/>
<connect gate="G$1" pin="IN1" pad="4"/>
<connect gate="G$1" pin="IN2" pad="5"/>
<connect gate="G$1" pin="IN3" pad="6"/>
<connect gate="G$1" pin="IN4" pad="7"/>
<connect gate="G$1" pin="OUT1A" pad="16"/>
<connect gate="G$1" pin="OUT1B" pad="14"/>
<connect gate="G$1" pin="OUT2A" pad="10"/>
<connect gate="G$1" pin="OUT2B" pad="12"/>
<connect gate="G$1" pin="SENSE1" pad="15"/>
<connect gate="G$1" pin="SENSE2" pad="11"/>
<connect gate="G$1" pin="VBB" pad="13"/>
<connect gate="G$1" pin="VCP" pad="17"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="IC1" library="allegro" deviceset="A3906" device=""/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="IC1" gate="G$1" x="40.64" y="53.34"/>
</instances>
<busses>
</busses>
<nets>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
</eagle>
