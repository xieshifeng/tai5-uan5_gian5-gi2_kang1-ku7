from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
import unittest

import Pyro4
import htsengine


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.語音合成.語音標仔轉換 import 語音標仔轉換
from 臺灣言語工具.語音合成.音檔頭前表 import 音檔頭前表
from 臺灣言語工具.表單.肯語句連詞 import 肯語句連詞
from 臺灣言語工具.斷詞.拄好長度辭典揣詞 import 拄好長度辭典揣詞
from 臺灣言語工具.斷詞.連詞揀集內組 import 連詞揀集內組
from 臺灣言語工具.解析整理.轉物件音家私 import 轉物件音家私
from 臺灣言語工具.語音合成 import 閩南語變調

class 語音合成整合試驗(unittest.TestCase):
	def setUp(self):
		self.粗胚 = 文章粗胚()
		self.分析器 = 拆文分析器()
		self.家私 = 轉物件音家私()
		
		self.揣詞 = 拄好長度辭典揣詞()
		self.揀集內組 = 連詞揀集內組()

		self.閩南語變調 = 閩南語變調()
		
		self.語音標仔轉換 = 語音標仔轉換()
		self.音檔頭前表 = 音檔頭前表()
	def tearDown(self):
		pass

	def test_字串轉聲音檔(self):
		閩南語模型 = 'HTSLSPtan5tso5.htsvoice'
		
		閩南語語句 = 'gua2 ai3 a1-sui2'
		
		處理減號 = self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 閩南語語句)
		章物件 = self.分析器.建立章物件(處理減號)
		標準章物件 = self.家私.轉音(臺灣閩南語羅馬字拼音, 章物件)
		音值物件 = self.家私.轉音(臺灣閩南語羅馬字拼音, 標準章物件, 函式='音值')
		變調物件=self.閩南語變調.變調(音值物件)
		標仔陣列 = self.語音標仔轉換.物件轉完整合成標仔(變調物件)
		愛合成標仔 = self.語音標仔轉換.跳脫標仔陣列(標仔陣列)
		一點幾位元組, 一秒幾點, 幾个聲道, 原始取樣 = \
			htsengine.synthesize(閩南語模型, 愛合成標仔)
		聲音檔 = self.音檔頭前表 .加起哩(原始取樣, 一點幾位元組, 一秒幾點, 幾个聲道)
		self.assertIsInstance(聲音檔, bytes)
		
	def test_字串斷詞後轉聲音檔(self):
		閩南語模型 = 'HTSLSPtan5tso5.htsvoice'
		閩南語辭典 = Pyro4.Proxy("PYRO:閩南語辭典@localhost:9839")
		閩南語連詞 = 肯語句連詞('語料/翻譯/閩.lm') 
		
		閩南語語句 = 'gua2 ai3 a1-sui2'
		
		處理減號 = self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 閩南語語句)
		章物件 = self.分析器.建立章物件(處理減號)
		標準章物件 = self.家私.轉音(臺灣閩南語羅馬字拼音, 章物件)
		斷好, _, _ = self.揣詞.揣詞(閩南語辭典, 標準章物件)
		標好, _, _ = self.揀集內組.揀(閩南語連詞, 斷好)
		音值物件 = self.家私.轉音(臺灣閩南語羅馬字拼音, 標好, 函式='音值')
		變調物件=self.閩南語變調.變調(音值物件)
		標仔陣列 = self.語音標仔轉換.物件轉完整合成標仔(變調物件)
		愛合成標仔 = self.語音標仔轉換.跳脫標仔陣列(標仔陣列)
		一點幾位元組, 一秒幾點, 幾个聲道, 原始取樣 = \
			htsengine.synthesize(閩南語模型, 愛合成標仔)
		聲音檔 = self.音檔頭前表 .加起哩(原始取樣, 一點幾位元組, 一秒幾點, 幾个聲道)
		self.assertIsInstance(聲音檔, bytes)
