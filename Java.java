class Node{
    int data;
    Node next;
    Node prev;

    Node(int data){
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

public class Java{

    static Node reverse(Node head){
        Node currNode = head;
        Node prevNode = null;

        while(currNode != null){
            prevNode = currNode.prev;
            currNode.prev = currNode.next;
            currNode.next = prevNode;

            currNode = currNode.prev;
        }

        head = prevNode.prev;
        return head;
    }

    static void printList(Node node){
        while(node != null){
            System.out.print(node.data + " ");
            node = node.next;
        }
        System.out.println();
    }

    public static void main(String[] args){
        Node head = new Node(1);
        head.next = new Node(2);
        head.next.prev = head;
        head.next.next = new Node(3);
        head.next.next.prev = head.next;
        head.next.next.next = new Node(4);
        head.next.next.next.prev = head.next.next;

        System.out.println("Original Linked List");
        printList(head);

        head = reverse(head);

        System.out.println("Reversed Linked List");
        printList(head);
    }
}