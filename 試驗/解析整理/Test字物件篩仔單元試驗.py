# -*- coding: utf-8 -*-
from unittest.case import TestCase
from unittest.mock import patch
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.集 import 集
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔


class 字物件篩仔單元試驗(TestCase):

    @patch('臺灣言語工具.基本物件.句.句.篩出字物件')
    def test_篩出字物件(self, 篩出字物件mock):
        物件 = 拆文分析器.分詞句物件('頭-家｜thau5-ke1 員-工｜uan5-kang1')
        篩出字物件mock.reset_mock()
        字物件篩仔.篩出字物件(物件)
        篩出字物件mock.assert_called_once_with()

    def test_篩字(self):
        型 = '媠'
        字物件 = 拆文分析器.建立字物件(型)
        self.assertEqual(字物件篩仔.篩出字物件(字物件), [字物件])

    def test_篩詞孤字(self):
        型 = '媠'
        字物件 = 拆文分析器.建立字物件(型)
        詞物件 = 拆文分析器.建立詞物件(型)
        self.assertEqual(字物件篩仔.篩出字物件(詞物件), [字物件])

    def test_篩詞無字(self):
        型 = ''
        詞物件 = 拆文分析器.建立詞物件(型)
        self.assertEqual(字物件篩仔.篩出字物件(詞物件), [])

    def test_篩詞濟字漢字(self):
        語句 = '椅仔'
        self.assertEqual(
            字物件篩仔.篩出字物件(拆文分析器.建立詞物件(語句)),
            [拆文分析器.建立字物件('椅'), 拆文分析器.建立字物件('仔')]
        )

    def test_篩詞濟字音標(self):
        語句 = 'tsit8-tiunn1'
        self.assertEqual(
            字物件篩仔.篩出字物件(拆文分析器.建立詞物件(語句)),
            [拆文分析器.建立字物件('tsit8'), 拆文分析器.建立字物件('tiunn1')]
        )

    def test_篩詞濟字漢羅(self):
        語句 = 'tsit8-張'
        self.assertEqual(
            字物件篩仔.篩出字物件(拆文分析器.建立詞物件(語句)),
            [拆文分析器.建立字物件('tsit8'), 拆文分析器.建立字物件('張')]
        )

    def test_篩組孤字(self):
        型 = '媠'
        字物件 = 拆文分析器.建立字物件(型)
        組物件 = 拆文分析器.建立組物件(型)
        self.assertEqual(字物件篩仔.篩出字物件(組物件), [字物件])

    def test_篩組無字(self):
        型 = ''
        組物件 = 拆文分析器.建立組物件(型)
        self.assertEqual(字物件篩仔.篩出字物件(組物件), [])

    def test_袂使是原本的字陣列(self):
        語句 = 'tsit8-張'
        詞物件 = 拆文分析器.建立詞物件(語句)
        self.assertIsNot(字物件篩仔.篩出字物件(詞物件), 詞物件.內底字)

    def test_愛是原本的字物件(self):
        語句 = 'tsit8-張'
        詞物件 = 拆文分析器.建立詞物件(語句)
        for 原來, 網出 in zip(詞物件.內底字, 字物件篩仔.篩出字物件(詞物件)):
            self.assertIs(原來, 網出)

    def 建立組檢查(self, 原來語句, 切好語句):
        字陣列 = []
        [字陣列.extend(字物件篩仔.篩出字物件(拆文分析器.建立詞物件(詞)))
         for 詞 in 切好語句]
        return (拆文分析器.建立組物件(原來語句), 字陣列)

    def test_篩組濟字(self):
        原來語句 = '我有一張椅仔！'
        切好語句 = ['我', '有', '一', '張', '椅', '仔', '！']
        組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
        self.assertEqual(字物件篩仔.篩出字物件(組物件), 詞陣列)

    # 為著通用佮一致性，這愛家己建立詞來鬥。大部份攏是無細字揤著，親像平行語料庫才另外閣包一層
    def test_篩組濟字配空白(self):
        原來語句 = '我 有 一張 椅仔！'
        切好語句 = ['我', '有', '一', '張', '椅', '仔', '！']
        組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
        self.assertEqual(字物件篩仔.篩出字物件(組物件), 詞陣列)

    def test_篩組濟音標(self):
        加空白後語句 = 'gua2 u7 tsit8-tiunn1 i2-a2'
        切好語句 = ['gua2', 'u7', 'tsit8-tiunn1', 'i2-a2']
        組物件, 詞陣列 = self.建立組檢查(加空白後語句, 切好語句)
        self.assertEqual(字物件篩仔.篩出字物件(組物件), 詞陣列)

    def test_篩組濟字輕聲(self):
        加空白後語句 = 'mi2-kiann7 boo5-0ki3 ah ! '
        切好語句 = ['mi2-kiann7', 'boo5-0ki3', 'ah', '!']
        組物件, 詞陣列 = self.建立組檢查(加空白後語句, 切好語句)
        self.assertEqual(字物件篩仔.篩出字物件(組物件), 詞陣列)

    def test_篩句濟字佮符號(self):
        原來語句 = '枋寮漁港「大條巷」上闊兩公尺。'
        切好語句 = ['枋', '寮', '漁', '港', '「', '大', '條',
                '巷', '」', '上', '闊', '兩', '公', '尺', '。']
        組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
        self.assertEqual(字物件篩仔.篩出字物件(
            拆文分析器.建立句物件(原來語句)), 詞陣列)
        組物件 = 組物件

    def test_篩章濟連字佮符號(self):
        原來語句 = '枋-寮漁-港「大-條-巷」。上-闊兩-公-尺'
        切好語句 = ['枋寮', '漁港', '「', '大條巷', '」', '。', '上闊', '兩公尺']
        組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
        self.assertEqual(字物件篩仔.篩出字物件(
            拆文分析器.建立章物件(原來語句)), 詞陣列)
        組物件 = 組物件

    def test_篩集濟組(self):
        原來語句 = '我有一張椅仔！'
        組陣列 = [拆文分析器.建立組物件(原來語句),
               拆文分析器.建立組物件(原來語句), ]
        self.assertRaises(解析錯誤, 字物件篩仔.篩出字物件, 集(組陣列))

    def test_篩集無字(self):
        型 = ''
        集物件 = 拆文分析器.建立集物件(型)
        self.assertEqual(字物件篩仔.篩出字物件(集物件), [])

    def test_篩句無字(self):
        型 = ''
        句物件 = 拆文分析器.建立句物件(型)
        self.assertEqual(字物件篩仔.篩出字物件(句物件), [])

    def test_篩章無字(self):
        型 = ''
        章物件 = 拆文分析器.建立章物件(型)
        self.assertEqual(字物件篩仔.篩出字物件(章物件), [])

    def test_烏白擲物件(self):
        self.assertRaises(型態錯誤, 字物件篩仔.篩出字物件, 2123)
        self.assertRaises(型態錯誤, 字物件篩仔.篩出字物件, '字物件篩仔')
        self.assertRaises(型態錯誤, 字物件篩仔.篩出字物件, None)
