# Project Plan

## Title
<!-- Give your project a short title. -->
Effects of household income level and country purchase power on depression 

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. How do household income and the purchasing power of a country relate to something as significant as feeling down or depressed? 

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
This project aims to investigate the intricate relationship between economic income and mental health outcomes in various European countries. This research is motivated by the need to understand and address mental health disparities in a rapidly changing socioeconomic landscape. 
To accomplish this, we will gather income data from multiple European nations, and complement this with assessments of mental health outcomes, including depression rates and power of purchase indicators. 
## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Purchase Power in Europe
* Metadata URL: https://ec.europa.eu/eurostat/cache/metadata/en/sdg_10_10_esmsip2.htm
* Data URL: https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/sdg_10_10/1.0/*.*.*.*.*?c[freq]=A&c[na_item]=EXP_PPS_EU27_2020_HAB&c[ppp_cat]=GDP&c[unit]=PC&c[geo]=EU27_2020,EU28,EU27_2007,EA20,EA19,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,BA,ME,MK,AL,RS,TR,US,JP&compress=true&format=csvdata&formatVersion=2.0&c[TIME_PERIOD]=2019,2014
* Data Type: CSV

Eurostat is the statistical office of the European Union responsible for collecting, harmonizing, and disseminating statistical data on across EU member states. Gross domestic product (GDP) is a measure for the economic activity.  GDP per capita is calculated as the ratio of GDP to the average population in a specific year. Basic figures are expressed in purchasing power standards (PPS), which represents a common currency that eliminates the differences in price levels between countries to allow meaningful volume comparisons of GDP.

### Datasource2: Depression Level in Europe
* Metadata URL: https://ec.europa.eu/eurostat/cache/metadata/en/hlth_det_esms.htm
* Data URL: https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/hlth_ehis_mh1i/1.0/*.*.*.*.*.*.*?c[freq]=A&c[unit]=PC&c[hlth_pb]=DPR,DPR_MJR,DPR_OTH&c[quant_inc]=QU1,QU2,QU4,QU5,QU3&c[sex]=M,F&c[age]=Y15-19,Y15-24,Y15-29,Y15-64,Y18-24,Y18-44,Y18-64,Y20-24,Y25-29,Y25-34,Y25-64,Y35-44,Y45-54,Y45-64,Y55-64,Y65-74&c[geo]=EU27_2020,EU28,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,UK,RS,TR&compress=true&format=csvdata&formatVersion=2.0&c[TIME_PERIOD]=2019,2014
* Data Type: CSV

The European Health Interview Survey (EHIS) aims at measuring on a harmonised basis and with a high degree of comparability among Member States (MS) the health status (including disability), health determinants (lifestyle) of the EU citizens and use of health care services and limitations in accessing it.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Explore Datasources [#1][i1]
2. Analyze Data [#2][i2]
3. Report Findings [#3][i3]
4. Refine Datasources Notebook [#4][i4]
5. Make Repository Submission-Ready [#5][i5]

[i1]:https://github.com/ramisyakar/made-template/issues/1
[i2]:https://github.com/ramisyakar/made-template/issues/2
[i3]:https://github.com/ramisyakar/made-template/issues/3
[i4]:https://github.com/ramisyakar/made-template/issues/4
[i5]:https://github.com/ramisyakar/made-template/issues/5

