import json
d={"ANDHRAPRADESH":"AMARAVATI","ARUNACHAL PRADESH":"ITANAGAR","ASSAM":"DISPUR","PUNJAB":"CHANDIGARH","CHATTISGARH":"RAIPUR","PATNA":"BIHAR","GOA":"PANAJI"}
with open("indian_capital.json",'w')as f:
 json.dump(d,f,indent=5)
print("json got appended")

