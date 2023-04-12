class Node:
    def __init__(self,d):
        self.data=d
        self.nextref=None
    
if __name__=="__main__":
    node1=Node(10)
    node2=Node(20)
    node3=Node(30)

    node1.nextref=node2
    node2.nextref=node3

    head=node1
    temp=head

    print("The data in the linked list is:")
    while temp!=None:
        print(temp.data,end=" ")
        temp=temp.nextref
