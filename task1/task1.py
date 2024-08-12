
def circular_path(n, m):
    path = []
    current_position = 0
    
    while True:
        path.append(current_position + 1)
        current_position = (current_position + m) % n
        if current_position == 0:
            break
    
    return ''.join(map(str, path))

def main():
    n = 4  
    m = 3  
    
    result = circular_path(n, m)
    print(result)

if __name__ == "__main__":
    main()
