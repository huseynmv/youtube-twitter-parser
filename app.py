from dateutil import parser
from datetime import datetime
yourdate = parser.parse('2022-04-16T10:30:02Z')
now = datetime.now()
diff = now - yourdate.replace(tzinfo=None) 
# print(str(diff)[0])


print(now)


print(yourdate.replace(tzinfo=None))
