class sort:
    def __init__(self) -> None:
        pass
    
    def bubble(self,arr):
        n= len(arr)
        for i in range(n-1):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1] ,arr[j]
        
        print ("Sorted array is:") 
        for i in range(len(arr)): 
            print ("%d" %arr[i],end=" ")

    def calling(self):
        n = int(input("Enter the range of the array:"))
        arr = [] 
        print("Enter the values:")
        for i in range(0, n): 
            ele = int(input()) 
            arr.append(ele) # adding the element to the end of the list
  
        self.bubble(arr) 
  
        

# object instantiating
srt = sort()
srt.calling()                  