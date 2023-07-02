stream = open('./demo.txt', 'at', encoding='utf-8')
stream.write(' h')
stream.writelines('\ncghkasdfdasghjk\n')
names = ["4687106", "过段时间卡箍覅苦厄以撒官方", "vghdsaf"]
# stream.writelines(names)

stream.writelines('\n'.join(names))
stream.writelines('\np9o7trevc67890orkefm,d9trgopdfbjkxcn tsr')
stream.flush()

stream.close()
