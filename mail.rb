###
# メールのヘッダを解読するプログラム
#
# 1.メールのtxtファイルを一括読み込み
# 2.正規表現でエンコードされた部分のみをscanで取り出した
# 3.scanは配列。joinを使って文字列に変換してUTF-8に変換
# 4.もう一度配列に戻して式展開させ出力した
###



require 'kconv'
print <<-EDS
***************************************************************************
メールのヘッダを解読します。
このプログラムでは実行時、ターミナルに(例)「ruby mail.rb spam.txt」のように
コマンドライン引数として解読したいメール（txtファイル）を入力してから実行してください。

エンコードされた部分の項目の順番はFrom,Subject,Toの順である必要があります。
**************************************************************************
EDS

datafile = ARGV[0]
#p datafile
#exit
text = File.open(datafile).gets(nil)
#p text
#exit
mail = text.scan(/\=\?.+\=*\?\=+/)
#p mail
#exit
mail = mail.join(",")
str =  mail.toutf8
#p str
ar =  str.split(",")

print <<-EDS
このメールは…
差出人→#{ar[0]}さん
件名→#{ar[1]}
宛先→#{ar[2]}さん
のメールです。
EDS

 
