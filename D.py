def is_correct(tags):
    open_tags = []
    mistakes_count = 0
    wrong_tag = ''
    for tag in tags:
        if tag[1] != '/':
            open_tags.append(tag)
        else:
            if not open_tags:
                #incorrect
                mistakes_count += 1
                if mistakes_count == 1:
                    wrong_tag = tag
                continue
                
            if open_tags[-1][1:] == tag[2:]:
                open_tags.pop()     
            else:
                #incorrect
                mistakes_count += 1
                if mistakes_count == 1:
                    if len(open_tags) == 1:
                        wrong_tag = tag
                    elif open_tags[-2][1:] == tag[2:]:
                        wrong_tag = open_tags.pop()
                        open_tags.pop()
                    else:
                        wrong_tag = tag
                        
                
        if mistakes_count > 1:
            break
    
    if open_tags:
        mistakes_count += len(open_tags)
        if mistakes_count == 1:
            wrong_tag = open_tags[-1]
        
    return mistakes_count, wrong_tag

def main():
    x = int(input())
    for _ in range(x):
        s = int(input())
        tags = []
        for _ in range(s):
            tags.append(input().upper())
        mistakes_count, wrong_tag = is_correct(tags)
        if mistakes_count == 0:
            print('CORRECT')
        elif mistakes_count == 1:
            print("ALMOST {}".format(wrong_tag))
        else:
            print("INCORRECT")
            
if __name__ == "__main__":
    main()
