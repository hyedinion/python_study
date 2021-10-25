phone_book = [ "97674223", "1195524421","119"]

def solution(phone_book):
    answer = True
    phone_book.sort()
    for p in phone_book:
        
        pdict = {}
        for p in phone_book:
            key = hash(p[0:i+1])
            if p[key] not in pdict.keys():
                pdict[key] = [p]
            else:
                pdict[key].append(p)
    
    check_hash(pdict)
    

    return answer

def check_hash(pdict):
    n_pdict = {}
    for k,v in pdict.items():
        if len(v)>1:

    

solution(phone_book)