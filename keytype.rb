#071keytype2.rb
words = ["Pig","Lion","Panda","Dragon"]
keywords = words.shuffle
puts "全部で#{words.size}問です！！頑張りましょう！！"
puts "3.."
sleep(1)
puts "2.."
sleep(1)
puts "1.."
sleep(1)
print <<-EOS
\n
スタートです!!
正しくタイプして、ENTERを押してください。
EOS
t0 = Time.now
count = 0
keywords.each do |keyword|
  puts keyword
  print ">"
  typed = gets.chomp
  if typed != keyword then
    puts "ちがいます！小文字から始めていませんか？"
    redo
  end
  count += 1
  str = "その調子です！ 頑張ってください！ ファイト！！"
  fight = str.split(" ").shuffle
  puts fight[0]
end
puts 
puts "***********************************************************"
puts "★おめでとう！よくできました★"

printf(" %3.2f 秒かかりました", Time.now - t0)
printf("一問あたりの平均時間は%3.2f秒です",(Time.now - t0) /(count))
puts



