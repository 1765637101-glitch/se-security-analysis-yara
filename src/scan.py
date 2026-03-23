import yara 

rule = yara.compile("test_rule.yara")
result = rule.match("test_sample.txt")
if result:
    print("匹配成功！找到规则：“,result)
else:
    print("未匹配")