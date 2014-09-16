# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國103年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
import unittest
from 試驗.基本元素.基本元素試驗 import 基本元素試驗
from 試驗.解析整理.程式掠漏試驗 import 程式掠漏試驗
from 試驗.解析整理.文章粗胚試驗 import 文章粗胚試驗
from 試驗.解析整理.拆文分析器建立試驗 import 拆文分析器建立試驗
from 試驗.解析整理.拆文分析器對齊試驗 import 拆文分析器對齊試驗
from 試驗.解析整理.拆文分析器轉做試驗 import 拆文分析器轉做試驗
from 試驗.解析整理.轉物件音家私試驗 import 轉物件音家私試驗
from 試驗.解析整理.物件譀鏡試驗 import 物件譀鏡試驗
from 試驗.解析整理.字物件篩仔試驗 import 字物件篩仔試驗
from 試驗.解析整理.詞物件網仔試驗 import 詞物件網仔試驗
from 試驗.解析整理.集內組照排試驗 import 集內組照排試驗
from 試驗.解析整理.揀集內組試驗 import 揀集內組試驗
from 試驗.解析整理.羅馬音仕上げ試驗 import 羅馬音仕上げ試驗
from 試驗.音標系統.教會系羅馬音標試驗 import 教會系羅馬音標試驗
from 試驗.音標系統.臺灣語言音標試驗 import 臺灣語言音標試驗
from 試驗.音標系統.臺灣閩南語羅馬字拼音試驗 import 臺灣閩南語羅馬字拼音試驗
from 試驗.音標系統.臺灣閩南語羅馬字拼音轉方音符號吳守禮改良式模組試驗 import 臺灣閩南語羅馬字拼音轉方音符號吳守禮改良式模組試驗
from 試驗.音標系統.臺灣閩南語羅馬字拼音轉音值模組試驗 import 臺灣閩南語羅馬字拼音轉音值模組試驗
from 試驗.音標系統.教會羅馬字音標試驗 import 教會羅馬字音標試驗
from 試驗.音標系統.通用拼音音標試驗 import 通用拼音音標試驗
from 試驗.音標系統.臺灣客家話拼音試驗 import 臺灣客家話拼音試驗
from 試驗.音標系統.臺灣客家話拼音轉音值模組試驗 import 臺灣客家話拼音轉音值模組試驗
from 試驗.音標系統.官話注音符號試驗 import 官話注音符號試驗
from 試驗.綜合標音.句綜合標音試驗 import 句綜合標音試驗
from 試驗.綜合標音.集綜合標音試驗 import 集綜合標音試驗
from 試驗.綜合標音.詞組綜合標音試驗 import 詞組綜合標音試驗
from 試驗.綜合標音.閩南語字綜合標音試驗 import 閩南語字綜合標音試驗
from 試驗.綜合標音.客話字綜合標音試驗 import 客話字綜合標音試驗
from 試驗.綜合標音.官話字綜合標音試驗 import 官話字綜合標音試驗
from 試驗.表單.型音辭典試驗 import 型音辭典試驗
from 試驗.表單.現掀辭典試驗 import 現掀辭典試驗
from 試驗.表單.尾字辭典試驗 import 尾字辭典試驗
from 試驗.表單.實際語句連詞試驗 import 實際語句連詞試驗
from 試驗.正規.阿拉伯數字試驗 import 阿拉伯數字試驗
from 試驗.斷詞.上長詞優先辭典揣詞試驗 import 上長詞優先辭典揣詞試驗
from 試驗.斷詞.拄好長度辭典揣詞試驗 import 拄好長度辭典揣詞試驗
from 試驗.斷詞.連詞揀集內組試驗 import 連詞揀集內組試驗
# from 試驗.斷詞.辭典連詞斷詞試驗 import 辭典連詞斷詞試驗
from 試驗.斷詞.中研院工具試驗 import 中研院工具試驗
from 試驗.語音合成.句物件轉合成標仔試驗 import 句物件轉合成標仔試驗
from 試驗.語音合成.生決策樹仔問題試驗 import 生決策樹仔問題試驗
from 試驗.語音合成.音檔頭前表試驗 import 音檔頭前表試驗
from 試驗.語音辨識.加短恬試驗 import 加短恬試驗
from 試驗.音標系統.官話注音符號轉音值模組試驗 import 官話注音符號轉音值模組試驗
# from 試驗.字音字型出題.揣閩南語辭典試驗 import 揣閩南語題目試驗

if __name__ == '__main__':
	基本元素試驗
	
	程式掠漏試驗
	文章粗胚試驗
	拆文分析器建立試驗
	拆文分析器對齊試驗
	拆文分析器轉做試驗
	轉物件音家私試驗
	物件譀鏡試驗
	字物件篩仔試驗
	詞物件網仔試驗
	集內組照排試驗
	揀集內組試驗
	羅馬音仕上げ試驗
	
	教會系羅馬音標試驗
	臺灣語言音標試驗
	臺灣閩南語羅馬字拼音試驗
	臺灣閩南語羅馬字拼音轉方音符號吳守禮改良式模組試驗
	臺灣閩南語羅馬字拼音轉音值模組試驗
	教會羅馬字音標試驗
	通用拼音音標試驗
	臺灣客家話拼音試驗
	臺灣客家話拼音轉音值模組試驗
	官話注音符號試驗
	官話注音符號轉音值模組試驗
	
	句綜合標音試驗
	集綜合標音試驗
	詞組綜合標音試驗
	閩南語字綜合標音試驗
	客話字綜合標音試驗
	官話字綜合標音試驗
	
	型音辭典試驗
	現掀辭典試驗
	尾字辭典試驗
	實際語句連詞試驗
	
	阿拉伯數字試驗
	
	上長詞優先辭典揣詞試驗
	拄好長度辭典揣詞試驗
	連詞揀集內組試驗
# 	辭典連詞斷詞試驗
	中研院工具試驗

	句物件轉合成標仔試驗
	生決策樹仔問題試驗
	音檔頭前表試驗

	加短恬試驗
# 	揣閩南語題目試驗
	
	unittest.main()
