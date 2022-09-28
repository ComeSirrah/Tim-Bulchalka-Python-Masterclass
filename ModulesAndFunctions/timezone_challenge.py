import datetime as dt
from datetime import datetime
import zoneinfo

# Display paris timezone
paris_tz = zoneinfo.ZoneInfo('Europe/Paris')
paris_time= datetime.now(tz=paris_tz).strftime('%H:%M:%S, %Z')
print(f'The current time in Paris is {paris_time}.\n', '-'*80, '\n')

# Display London timezone
london_tz = zoneinfo.ZoneInfo('Europe/London')
london_time = datetime.now(tz=london_tz).strftime('%H:%M:%S, %Z')
print(f'The current time in London is {paris_time}.\n', '-'*80, '\n')

# Display Hong Kong timezone
hong_kong_tz = zoneinfo.ZoneInfo('Asia/Hong_Kong')
hong_kong_time = datetime.now(tz=hong_kong_tz).strftime('%H:%M:%S, %Z')
print(f'The current time in Hong Kong is {hong_kong_time}.\n', '-'*80, '\n')

# Display Nairobi timezone
nairobi_tz = zoneinfo.ZoneInfo('Africa/Nairobi')
nairobi_time = datetime.now(tz=nairobi_tz).strftime('%H:%M:%S, %Z')
print(f'The current time in Nairobi is {nairobi_time}.\n', '-'*80, '\n')
