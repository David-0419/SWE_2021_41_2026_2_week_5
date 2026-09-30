def isHappy(n):
  HappyNumber = 0
  record = []
  while True:
    # Operation
    while n != 0: 
      HappyNumber += (n % 10) ** 2
      n = n // 10   
    # checking if it is happynumber  
    if HappyNumber == 1: 
      return True
    # checking if it loops endlessly
    for x in record: 
      if x == HappyNumber:
        return False
    record.append(HappyNumber) 
    n = HappyNumber
    HappyNumber = 0
    
if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)
    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")      
    print("Results saved to /app/bind_mount/output.txt")