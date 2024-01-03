from data_pipeline import run_pipeline
import unittest

class TestDataPipeline(unittest.TestCase):
    def test_pipeline(self):
        depression_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/hlth_ehis_mh1i/1.0/*.*.*.*.*.*.*?c[freq]=A&c[unit]=PC&c[hlth_pb]=DPR,DPR_MJR,DPR_OTH&c[quant_inc]=QU1,QU2,QU4,QU5,QU3&c[sex]=M,F&c[age]=Y15-19,Y15-24,Y15-29,Y15-64,Y18-24,Y18-44,Y18-64,Y20-24,Y25-29,Y25-34,Y25-64,Y35-44,Y45-54,Y45-64,Y55-64,Y65-74&c[geo]=EU27_2020,EU28,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,UK,RS,TR&compress=true&format=csvdata&formatVersion=2.0&c[TIME_PERIOD]=2019,2014"
        gdp_url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/sdg_10_10/1.0/*.*.*.*.*?c[freq]=A&c[na_item]=EXP_PPS_EU27_2020_HAB&c[ppp_cat]=GDP&c[unit]=PC&c[geo]=EU27_2020,EU28,EU27_2007,EA20,EA19,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,NO,CH,UK,BA,ME,MK,AL,RS,TR,US,JP&compress=true&format=csvdata&formatVersion=2.0&c[TIME_PERIOD]=2019,2014"
        df = run_pipeline(depression_url, gdp_url)
        self.assertIsNotNone(df)
     

if __name__ == '__main__':
    unittest.main()
