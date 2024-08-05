#7a. Develop a python program to create two classes called as Stack and Queue. Provide the necessary data members and methods to display the operations that can be performed on stacks and queues. Test for all type of conditions.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else "Stack is empty"

    def peek(self):
        return self.items[-1] if self.items else "Stack is empty"

    def display(self):
        print("Stack:", self.items)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if self.items else "Queue is empty"

    def peek(self):
        return self.items[0] if self.items else "Queue is empty"

    def display(self):
        print("Queue:", self.items)

def main():
    choice = input("Choose stack or queue: ").strip().lower()
    if choice == "stack":
        ds = Stack()
        while True:
            action = input("Enter action (push, pop, peek, display, quit): ").strip().lower()
            if action == "push":
                item = int(input("Enter item to push: "))
                ds.push(item)
            elif action == "pop":
                print("Popped item:", ds.pop())
            elif action == "peek":
                print("Top item:", ds.peek())
            elif action == "display":
                ds.display()
            elif action == "quit":
                break
            else:
                print("Invalid action")
    elif choice == "queue":
        ds = Queue()
        while True:
            action = input("Enter action (enqueue, dequeue, peek, display, quit): ").strip().lower()
            if action == "enqueue":
                item = int(input("Enter item to enqueue: "))
                ds.enqueue(item)
            elif action == "dequeue":
                print("Dequeued item:", ds.dequeue())
            elif action == "peek":
                print("Front item:", ds.peek())
            elif action == "display":
                ds.display()
            elif action == "quit":
                break
            else:
                print("Invalid action")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
