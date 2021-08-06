class sorting:
    def __init__(self) -> None:
        pass
    
    def selection(self,arr):
        n= len(arr)
        for i in range(n-1):
            min=i
            for j in range(i+1,n):
                if arr[min]>arr[j]:
                    min=j
            arr[i],arr[min]=arr[min],arr[i]
        
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
  
        self.selection(arr) 
  
        

# object instantiating
srt = sorting()
srt.calling()                  