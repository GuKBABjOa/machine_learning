def find_s_algorithm(examples):
    hypothesis = ['0', '0', '0', '0', '0', '0'] #최초 h0 초기화/출력
    print(hypothesis)
    for example in examples:
        attributes = example[:-1]
        label = example[-1]
        
        
        if label == '+': # 가설 업데이트
            for i, attr in enumerate(attributes):
                if hypothesis[i] == '0':
                    if attr != hypothesis[i]:
                        hypothesis[i] = attr
                elif hypothesis[i] != attr:
                    hypothesis[i] = '?'
            print(hypothesis) #각 단계에서 완성된 h(n)을 출력
    
    return hypothesis

examples = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', '+'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', '+'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', '-'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', '+'],
]

hypothesis = find_s_algorithm(examples)
print("결과:", hypothesis) #최종 h
