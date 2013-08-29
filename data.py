from datetime import date
import munge

FROM_DATE = date(2013,6,3)
TO_DATE = date(2013,6,30)

articles = munge.munge(FROM_DATE, TO_DATE)