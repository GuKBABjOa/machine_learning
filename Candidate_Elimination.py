examples = [
    ('Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', '+'),
    ('Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', '+'),
    ('Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', '-'),
    ('Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', '+'),
] # 데이터

S = ['0', '0', '0', '0', '0', '0'] 
G = ['?', '?', '?', '?', '?', '?']

domains = [('Rainy', 'Sunny'), # 도메인 선언
 ('Cold', 'Warm'),
 ('High', 'Normal'),
 ('Strong', 'Nstrong'),
 ('Cool', 'Warm'),
 ('Change', 'Same'),
 ('N', 'Y')]

def changeATT(domain_list, input_tuple): #인데스가 -일때 속성들을 도메인의 다른 속성으로 변경 시키는 함수
    changed_tuple = []
    
    for element in input_tuple:
        # 요소가 도메인 리스트에 있는지 확인하고 다른 요소로 변경
        for domain in domain_list:
            if element in domain:
                # 현재 도메인 리스트에서 다른 요소를 선택
                new_element = next((item for item in domain if item != element), '?')
                changed_tuple.append(new_element)
                break
    
    return tuple(changed_tuple)



def make_g(g, s): #g를 만드는 함수
    
    result_s = []
    
    
    for i in range(len(g)):
        result = []
        flag = 0
        for k in range(len(g)):
            if g[k] == s[k] and i == k:
                    if flag == 0:
                        result.append(g[k])
                        flag = 1
                    else:
                        result.append('?')
            else:
                result.append('?')
        if  not all(elem == '?' for elem in result):
            result_s.append(result)

    return result_s
def update_G(g,s):
    for i, sublist in enumerate (g[:]):
        for k in range(len(s)):
            if sublist[k] != '?' and sublist[k] != s[k]:
                del g[i]
    return g
        
def CE_algorithm(examples):

    global G
    global S
    count = 1
    for example in examples:
        attributes = example[:-1]
        label = example[-1]
        
        
        if label == '+': # 가설 업데이트
            for i, attr in enumerate(attributes):
                if S[i] == '0':
                    if attr != S[i]:
                        S[i] = attr
                elif S[i] != attr:
                    S[i] = '?'
            if not all(elem == '?' for elem in G):
                G = update_G(G,S)
            print(f'S[{count}] = {S}')
            print(f'G[{count}] = {G}')
            count += 1
        else:
            G = changeATT(domains, attributes)
            G = make_g(G,S)
            print(f'S[{count}] = {S}')
            print(f'G[{count}] = {G}')
            count += 1

print(f'S[0] = {S}')
print(f'G[0] = {G}')
CE_algorithm(examples)