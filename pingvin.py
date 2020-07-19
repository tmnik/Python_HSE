#напечатать n пингвинов в строчку
n = int(input())
str1 = "   _~_    "
str2 = "  (o o)   "
str3 = " /  V  \  "
str4 = "/(  _  )\ "
str5 = "  ^^ ^^   "
print(str1*n, str2*n, str3*n, str4*n, str5*n, sep='\n', end='\n\n')
