s = input("Введите число: ")

##############
# Пунк А
##############

m_i = 0
m_num = -1
for i in range(0, len(s)):
    num = int(s[i])
    if m_num<num:
        m_num = num
        m_i = i

print(m_num, m_i)

m_i = 0
m_num = -1
for i in range(len(s)-1, 0, -1):
    num = int(s[i])
    if m_num<num:
        m_num = num
        m_i = i

print(m_num, m_i)

##############
# Пунк Б
##############

m_i = 0
m_num = 10
for i in range(0, len(s)):
    num = int(s[i])
    if m_num>num:
        m_num = num
        m_i = i

print(m_num, m_i)

m_i = 0
m_num = 10
for i in range(len(s)-1, 0, -1):
    num = int(s[i])
    if m_num>num:
        m_num = num
        m_i = i

print(m_num, m_i)
