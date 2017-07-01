####
# 英文の単語数を数えるプログラム
#
# 1.ファイル（英文）をコマンドライン引数で読み込んで単語ごとに区切った配列をtextに代入
# 2.新しいハッシュを生成
# 3.textのそれぞれの要素に対して単語を数える処理
# 4.単語数の多い順にsortして並び替えて、その単語と共に単語数を出力させた
#####

puts "英文の単語数を数えるプログラム"
datafile = ARGV[0]
text = File.open(datafile).gets(nil).split
puts "この英文の単語数は#{text.size}です。"
words = Hash.new(0)
#p words
text.each do |word|
  words[word] += 1
end
#exit
# p words
words.sort_by{|word,count|[-count,word]}.each do |word,count|
  print "#{word}\t#{count}\n"
end

