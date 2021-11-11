# 딕셔너리를 이용한 팝송 가사의 알파벳 카운팅

# {a: 38, b: 22, ..... z:12 }



lyrics = '''
I will always remember
The day you kissed my lips
Light as a feather
And it went just like this
No, it's never been better
Than the summer of 2002
We were only eleven
But acting like grownups
Like we are in the present
Drinking from plastic cups
Singing love is forever and ever
Well, I guess that was true

Dancing on the hood in the middle of the woods
On an old Mustang, where we sang
Songs with all our childhoods friends
And it went like this, say

Oops I got 99 problems singing bye, bye, bye
Hold up, if you wanna go and take a ride with me
Better hit me, baby, one more time
Paint a picture for you and me
Of the days when we were young
Singing at the top of both our lungs

Now we're under the covers
Fast forward to eighteen
We are more than lovers
Yeah, we are all we need
When we're holding each other
I'm taken back to 2002

Dancing on the hood in the middle of the woods
On an old Mustang, where we sang
Songs with all our childhoods friends
And it went like this, say

Oops I got 99 problems singing bye, bye, bye
Hold up, if you wanna go and take a ride with me
Better hit me, baby, one more time
Paint a picture for you and me
Of the days when we were young
Singing at the top of both our lungs
On the day we fell in love
On the day we fell in love

Dancing on the hood in the middle of the woods
On an old Mustang, where we sang
Songs with all our childhoods friends
Oh, now

Oops I got 99 problems singing bye, bye, bye
Hold up, if you wanna go and take a ride with me
Better hit me, baby, one more time
Paint a picture for you and me
Of the days when we were young
Singing at the top of both our lungs
On the day we fell in love
On the day we fell in love
On the day we fell in love
On the day we fell in love, love, love
'''

# 알파벳과 그 횟수를 저장할 딕셔너리 생성
alphabet = {}

# 노래가사를 한글자씩 반복순회한다.

for c in lyrics:
    # 가사에서 알파벳이 아닌 특수문자나 공백은 관심대상이 아님
    # 건너뛰어야 한다.
    if not c.isalpha():
        continue
    # 만약에 알파벳이라면 대소문자를 통일한다.
    c = c.lower()
    
    # 현재 등장한 알파벳이 처음 등장했다면, 1이라는 카운트와 함께 
    # 딕셔너리에 추가

    if c not in alphabet:
        alphabet[c] = 1   
    else:
        alphabet[c] += 1
# 결과 출력
print(alphabet)

# 정렬을 하려면 리스트를 이용합니다.

keylist = []

for k in alphabet:
    keylist.append(k)

keylist.sort()
print(keylist)

print('======== 노래가사 알파벳 빈도 =======')

for k in keylist:
    count = alphabet[k]
    print(f'# {k} => {count}')